FROM python:3.8-bullseye

WORKDIR /auth
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "auth_server.py"]