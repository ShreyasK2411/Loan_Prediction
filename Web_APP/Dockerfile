# configuring spark
FROM datamechanics/spark:3.2.1-hadoop-3.3.1-java-11-scala-2.12-python-3.8-alpine

USER root

WORKDIR /opt/spark

RUN pip install --upgrade pip

COPY  spark-requirements.txt .
RUN pip3 install -r spark-requirements.txt

# running the website
COPY ./website-requirements.txt /app/website-requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r website-requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]