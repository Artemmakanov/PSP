all:
	docker compose -f docker-compose-pg.yml
	docker compose -f docker-compose-pg.yml

stop:
	docker stop postgres_container
	docker stop app

rm:
	docker rm postgres_container
	docker rm app
	docker rmi app