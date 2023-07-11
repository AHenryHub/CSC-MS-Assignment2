FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python","main.py","flask","run","--host","0.0.0.0","--port","8000:8000" ]

COPY requirements.txt requirements.txt