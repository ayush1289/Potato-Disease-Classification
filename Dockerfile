# Base image
FROM python:3.9-slim-buster as base

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev

# Install Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

# Copy ReactJS code
COPY ./app/src /app/src
COPY ./app/public /app/public
WORKDIR /app
COPY package*.json /app
RUN npm install
COPY . .
RUN npm run build

# Copy FastAPI code
COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt

# Expose port
EXPOSE 8000

# Start server
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
