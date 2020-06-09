# Dockerfile
# Pull base image
FROM python:3.8
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /mailster
#Copy dependencies
COPY requirements.txt /tmp/
# Install dependencies
RUN pip install --requirement /tmp/requirements.txt
# Copy project
COPY . /mailster/

