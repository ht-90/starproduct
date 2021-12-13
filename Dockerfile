# Base image
FROM python:3.10-slim

# Update os and install git
RUN apt-get update && \
    apt-get install -y git

# Install pip and setuptools
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools

# Install dependecies
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy files
COPY . .
