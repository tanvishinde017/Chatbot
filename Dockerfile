# Use lightweight Python image
FROM python:3.11-slim

# Prevent Python from creating .pyc files 
ENV PYTHONDONTWRITEBYTECODE=1

# Enable unbuffered logs
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
