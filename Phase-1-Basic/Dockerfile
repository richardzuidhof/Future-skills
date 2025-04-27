FROM alpine:latest

# update to show best practices
RUN apk update && apk add nginx

COPY default.conf /etc/nginx/http.d/default.conf

COPY web/index.html /usr/share/nginx/html/index.html

# Expose port 80 just clarity, not required
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
