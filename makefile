all:
	docker compose -f docker-compose-pg.yml up -d
	docker compose -f docker-compose-app.yml up -d

stop:
	docker stop postgres_container
	docker stop app

rm:
	docker rm postgres_container
	docker rm app
	docker rmi psp-app