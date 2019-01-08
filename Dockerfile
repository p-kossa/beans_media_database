# base image
FROM python:latest

# add app
RUN mkdir -p /opt
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt

# run server
RUN python setup.py develop
CMD python main_app/app.py
EXPOSE 8000
