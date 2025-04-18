FROM python:3.12-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set working directory
WORKDIR /app
# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
# Copy project files
COPY . /app/
# Create all necessary migrations and then run migrations
RUN python manage.py makemigrations accounts weather energy_forecast dashboard && python manage.py migrate
# Collect static files
RUN python manage.py collectstatic --noinput
# Set permissions for static files
RUN chmod -R 755 /app/staticfiles
# Expose the port
EXPOSE 8000
# Run the server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
