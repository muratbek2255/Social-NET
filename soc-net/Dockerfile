FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/Social-NET

COPY ./req.txt /usr/src/Social-NET
RUN pip install -r req.txt

COPY . /usr/src/Social-NET

#EXPOSE 8080
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
