all:
	sudo docker compose -f docker-compose-pg.yml up -d
	sudo docker compose -f docker-compose-app.yml up -d

app: 
	sudo docker compose -f docker-compose-app.yml up -d --build
stop:
	sudo docker stop postgres_container
	sudo docker stop app

rm:
	sudo docker rm postgres_container
	sudo docker rm app
	sudo docker rmi psp-app