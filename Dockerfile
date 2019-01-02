# base image
FROM python:latest

# add app
RUN mkdir -p /opt/app
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt

# run server
RUN python setup.py develop
CMD python rest_api_demo/app.py
EXPOSE 8000