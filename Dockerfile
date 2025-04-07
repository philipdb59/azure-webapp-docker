# Use an official Python image
FROM python:3.10-slim

# Create app directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 7000 (for local clarity; Azure will also read WEBSITE_PORT)
EXPOSE 7000

# Run the Flask app
CMD ["python", "app.py"]
