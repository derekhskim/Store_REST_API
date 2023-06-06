# CONTRIBUTING

## How to run the Dockerfile locally

```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" site-flask sh -c "flask run --host 0.0.0.0"
```

## .env Not Available in Github repository

```
Must add DATABASE_URL information in newly created .env
add
DATABASE_URL={your PostgreSQL database link}
```