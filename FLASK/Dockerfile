# Use official Ptyhon Image
FROM python:3.9

#set working directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

#Expose Flas port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
