# CONTRIBUTING

## How to run the Dockerfile locally

```
docker build -t rest-api-email .
docker run -p 5000:5000 -w /app -v "$(pwd):/app" rest-api-email sh -c "flask run --host 0.0.0.0"
```

## .env Not Available in Github repository

```
Must add DATABASE_URL information in newly created .env
add
DATABASE_URL={your PostgreSQL database link}
```