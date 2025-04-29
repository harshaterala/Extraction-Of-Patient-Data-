FROM python:3.10

# Install tesseract-ocr
RUN apt-get update && apt-get install -y tesseract-ocr

# Set workdir
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE http://127.0.0.1:8000/docs

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
