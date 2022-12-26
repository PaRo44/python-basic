# docker build -t myapp .
# docker run --rm -it -d -p 8000:8000 myapp

FROM python:3.9-buster

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000:8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
