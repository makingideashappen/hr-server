# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /guestbook

# Copy the requirements file
COPY requirements.txt /guestbook/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . /guestbook/

# Expose the necessary port
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]