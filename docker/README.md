# Mini-RAG Application
A `docker-compose.yml` file is provided under `docker/docker-compose.yml` to set up MongoDB.

To start MongoDB using Docker Compose, run:

```sh
cd docker
cp .env.example .env
```
update `.env` with your credintials

set the following variables with your username and password

```
MONGO_INITDB_ROOT_USERNAME=username
MONGO_INITDB_ROOT_PASSWORD=password
```


```
docker-compose -f docker-compose.yml up -d
```

This will start a MongoDB service in the background.