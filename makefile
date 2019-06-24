.PHONY: .env
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

createrds:
	aws --profile default rds create-db-instance \
	--db-instance-identifier "ig-photos" --db-name "photos" \
	--region "us-east-2" \
	--db-instance-class "db.t2.micro" --engine "postgres" \
	--master-username "postgres" --master-user-password ${DB_PASSWORD} \
	--allocated-storage 20 --vpc-security-group-ids "sg-4f29f821" \
	--tags Key='name',Value='ig-photos'

deleterds:
	aws --profile default rds delete-db-instance \
	--db-instance-identifier "ig-photos" --skip-final-snapshot \
	--delete-automated-backups

	aws --profile default rds wait db-instance-deleted \
	--db-instance-identifier "ig-photos"


recreaterds:
	make deleterds

	make createrds
