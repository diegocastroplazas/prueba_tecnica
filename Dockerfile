FROM python:3.7
ENV PYTHONBUFFERED 1

RUN mkdir /prueba_tecnica
WORKDIR /prueba_tecnica

ADD . /prueba_tecnica/

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./contrasena.py"]
ENTRYPOINT ["python", "./domingos.py"]