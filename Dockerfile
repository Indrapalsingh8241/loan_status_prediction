
# Base Image
FROM python:3.9

# Set Working Directory
WORKDIR /app

# Copy Files
COPY . /app

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI Port

RUN chmod +x start.sh 
EXPOSE 8000 
EXPOSE 8501 

CMD ["./start.sh"]
