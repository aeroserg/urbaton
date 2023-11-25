FROM python:3.8-bullseye

WORKDIR /send_email
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 9001
CMD ["python", "-u", "sender_server.py"]