.PHONY: .env

# Set the AWS profile you have stored in your .aws/credentials file.
aws-profile = default
s3-bucket-name = strib-ig-photos

# database name goes after 5432/
env:
	echo 'DJANGO_SECRET_KEY=dev123' >> .env
	echo 'DATABASE_URL=psql://'`whoami`':@127.0.0.1:5432/senate' >> .env
	echo 'DEBUG=True' >> .env

syncdb:
	dropdb ig
	createdb ig
	rm -rf minutes_search/migrations
	python manage.py makemigrations ig_photos
	python manage.py migrate

# AWS CLI Command to create an RDS instance
createrds:
	aws --profile $(aws-profile) rds create-db-instance \
	--db-instance-identifier "ig-photos" --db-name "photos" \
	--region "us-east-2" \
	--db-instance-class "db.t2.micro" --engine "postgres" \
	--master-username "postgres" --master-user-password ${DB_PASSWORD} \
	--allocated-storage 20 --vpc-security-group-ids "sg-4f29f821" \
	--tags Key='name',Value='ig-photos'

deleterds:
	aws --profile $(aws-profile) rds delete-db-instance \
	--db-instance-identifier "ig-photos" --skip-final-snapshot \
	--delete-automated-backups

	aws --profile $(aws-profile) rds wait db-instance-deleted \
	--db-instance-identifier "ig-photos"

recreaterds:
	make deleterds
	make createrds

# AWS CLI command to create a public S3 bucket with folders for both static files and media assets
createbucket:
	aws --profile $(aws-profile) s3api create-bucket \
	--bucket $(s3-bucket-name) \
	--region us-east-2 \
	--create-bucket-configuration LocationConstraint=us-east-2

setbucketpermissions:
	aws --profile $(aws-profile) s3api put-bucket-acl \
	--acl public-read \
	--bucket $(s3-bucket-name)

	aws --profile $(aws-profile) s3api put-object-acl \
	--acl public-read \
	--bucket $(s3-bucket-name) \
	--key static/

	aws --profile $(aws-profile) s3api put-object-acl \
	--acl public-read-write \
	--bucket $(s3-bucket-name) \
	--key media/

createfolders:
	aws --profile $(aws-profile) s3api put-object \
	--bucket $(s3-bucket-name) \
	--key static/

	aws --profile $(aws-profile) s3api put-object \
	--bucket $(s3-bucket-name) \
	--key media/

igbucket:
	make createbucket
	make createfolders
	make setbucketpermissions
