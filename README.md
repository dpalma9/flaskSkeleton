# Intro
This an easy Flask project. It's meant to be a skeleton for more Flask projects.

## Objetive
The base project will run without data base. It will do some simple things on `modules` and it will be serve always on '/'. `routes.py` will only have to render the index.html template.

# Run
The app is meant to run with Docker:
```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```