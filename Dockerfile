FROM python:3.10-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && pip3 install -U pyrogram tgcrypto

COPY . .
CMD ["python3", "main.py"]
