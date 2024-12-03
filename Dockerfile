# Use a multi-stage build to keep the final image lightweight

# Stage 1: Build the frontend
FROM node:14 as build-frontend

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Set up the backend
FROM python:3.9-slim as build-backend

WORKDIR /app/backend
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./

# Stage 3: Combine frontend and backend
FROM nginx:alpine

# Copy frontend build to Nginx
COPY --from=build-frontend /app/frontend/build /usr/share/nginx/html

# Copy backend application
COPY --from=build-backend /app/backend /app/backend

# Expose ports
EXPOSE 80 5000

# Start Nginx and Flask
CMD ["sh", "-c", "nginx -g 'daemon off;' & python /app/backend/app.py"]