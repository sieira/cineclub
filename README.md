# Cineclub

This is a test project using client_corleone

# Requirements

You will need to install docker-compose

# Install

Use the botfather to create a telegram bot. This will give you a token
Create your .env file based on the .env.tpl file
run the following commands:

```
docker-compose up -d
```

```
docker-compose exec cineclub ./manage.py migrate
```

Create a superuser

```
docker-compose exec cineclub ./manage.py createsuperuser --email admin@example.com --username admin
```

If everything is OK, you should be able to access http://localhost:1234/admin/ with your username
and password
