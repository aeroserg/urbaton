FROM python:3.8-bullseye

WORKDIR /orders
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "orders_server.py"]