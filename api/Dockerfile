FROM python:3.9

WORKDIR /app

COPY * /app/

RUN pip3 install -r requirements.txt

CMD [ "uvicorn", "main:api", "--port 8000", "--reload" ]