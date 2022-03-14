# django-microservice-graphql
## features
- django model only
- starlette
- graphql with strawberry

## debug run command
```
uvicorn asgi:app --reload
```

## run with docker
```
docker build . -t test
docker run -t -i --rm -p 8000:8000 test
```
