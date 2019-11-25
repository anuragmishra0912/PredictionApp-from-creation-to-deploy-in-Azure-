#Use python as base image 
FROM python:3.5-slim

#Use working directory 
WORKDIR /app

#Copy all content form workinf directory to /app
ADD . /app

#installing required packages 
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME OpentoAll

#Run python program
CMD ["python", "app.py"]
