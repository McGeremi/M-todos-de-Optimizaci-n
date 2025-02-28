# Use the official Python 3.13 image from the Docker Hub
FROM python:3.13

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
#COPY . /app

# Specify the command to run on container start
#CMD ["python", "app.py"]