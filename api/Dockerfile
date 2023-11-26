FROM python:3.9

WORKDIR /app

RUN apt-get install pkg-config

# Install wait-for-it
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

COPY * /app/

RUN pip3 install -r requirements.txt
RUN pip3 install pytest

EXPOSE 8000

# Use wait-for-it before starting the application
CMD ["wait-for-it", "db:3306", "--", "uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000", "--reload"]
