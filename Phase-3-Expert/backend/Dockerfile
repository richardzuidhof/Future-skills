FROM alpine:latest

# update to show best practices
RUN apk update && apk add --no-cache curl python3 py3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --break-system-packages --upgrade pip setuptools
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY app.py .

# Expose port 80 just clarity, not required
EXPOSE 5000
HEALTHCHECK --interval=10s --timeout=2s CMD curl -f http://localhost:5000/api/health || exit 1

CMD ["python", "app.py"]
