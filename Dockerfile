<<<<<<< HEAD
FROM python:3.8-slim-buster 

WORKDIR /app

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY . .

=======
FROM python:3.8-slim-buster 

WORKDIR /app

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY . .

>>>>>>> 4b4f00d6cb72a07a10395db5d57d9c3ba8819398
CMD ["python", "manage.py", "runserver"]