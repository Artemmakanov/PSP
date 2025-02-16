FROM python:3.10-slim

WORKDIR /backend

RUN echo 'deb http://deb.debian.org/debian testing main' >> /etc/apt/sources.list \
    && apt-get update && apt-get install -y --no-install-recommends -o APT::Immediate-Configure=false gcc g++

COPY ./requirements.txt /backend

COPY ./backend /backend

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "fill_paper_table.py"]

CMD ["python", "run.py"]