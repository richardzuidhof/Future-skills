FROM alpine:latest

RUN apk add --no-cache nginx openssl

COPY ./certs/cert.pem /etc/ssl/certs/cert.pem
COPY ./certs/key.pem /etc/ssl/private/key.pem
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]