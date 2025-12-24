FROM python:3.12-slim

# -------------------------
# System dependencies
# -------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    unzip \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# Set working directory
# -------------------------
WORKDIR /app

# -------------------------
# Copy requirements and install Python packages
# -------------------------
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# Copy application code
# -------------------------
COPY . .

# Expose FastAPI port
EXPOSE 8000

# -------------------------
# Run the application
# -------------------------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
