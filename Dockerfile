# Use the official Python image.
# Use python:3.9-slim or another version if you need a specific version.
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run Django development server
# If you’re using Gunicorn in production, you may want to start it here instead.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]