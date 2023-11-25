FROM python:3.8-bullseye

WORKDIR /common_information
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "common_information_service.py"]