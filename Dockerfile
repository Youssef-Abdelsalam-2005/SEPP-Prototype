# First Stage - Build frontend with Nginx
FROM nginx:alpine as frontend-build

# Copy the frontend files into the Nginx container
COPY frontend/ /usr/share/nginx/html/

# Second Stage - Build Backend with Python and Flask
FROM python:3.10-slim as backend-build

# Install required system dependencies (including virtualenv)
RUN apt-get update && apt-get install -y python3-venv

# Set working directory
WORKDIR /app

# Copy the backend files into the container
COPY backend/requirements.txt /app/
COPY backend/app.py /app/

# Create a virtual environment
RUN python3 -m venv /app/venv

# Install dependencies inside the virtual environment
RUN /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

# Final Stage - Combining Frontend and Backend into the Final Image
FROM nginx:alpine

# Copy the frontend build from the previous stage
COPY --from=frontend-build /usr/share/nginx/html /usr/share/nginx/html

# Copy the backend code and virtual environment
COPY --from=backend-build /app /app

# Expose the required ports
EXPOSE 80 5000

# Start the Flask app in the background and run Nginx
CMD ["sh", "-c", "/app/venv/bin/python /app/app.py & nginx -g 'daemon off;'"]
