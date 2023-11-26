FROM python:3.8-bullseye

WORKDIR /message
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "message_server.py"]