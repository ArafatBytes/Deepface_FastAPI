# Use Python 3.10 base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5001

# Run FastAPI using Uvicorn
CMD ["uvicorn", "face_verify_service:app", "--host", "0.0.0.0", "--port", "5001"]
