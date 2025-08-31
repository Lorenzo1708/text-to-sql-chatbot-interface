```
py -m venv .venv
py -m pip install -r ./requirements.txt
```

```
docker network create client-server
docker build -t client .
docker run --env-file ./.env --name client --network client-server --publish 7860:7860 --rm client
```
