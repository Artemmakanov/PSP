FROM python:3.10-slim

COPY ./src /src
COPY ./run.py /
COPY ./requirements.txt /

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]