FROM python:3.8-alpine

# running the website
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app


RUN apt-get update
RUN apt-get install gcc

# install the dependencies and packages in the requirements file
RUN pip install -r website-requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]