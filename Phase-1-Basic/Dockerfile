FROM alpine:latest

RUN apk add nginx

COPY default.conf /etc/nginx/http.d/default.conf

COPY web/index.html /usr/share/nginx/html/index.html

CMD ["nginx", "-g", "daemon off;"]
