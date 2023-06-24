FROM madhuakula/hacker-container:latest

MAINTAINER Erdemstar

WORKDIR /app

COPY app.py /app

COPY requirements.txt /app

RUN python3 -m venv /app/venv

RUN /app/venv/bin/pip install -r /app/requirements.txt 

EXPOSE 4444

CMD . /app/venv/bin/activate && exec python app.py