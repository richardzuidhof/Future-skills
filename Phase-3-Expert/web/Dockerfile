FROM alpine:latest

# update to show best practices
RUN apk update && apk add nginx curl

COPY default.conf /etc/nginx/http.d/default.conf

COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 just clarity, not required
EXPOSE 80
HEALTHCHECK --interval=10s --timeout=2s CMD curl -f http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
