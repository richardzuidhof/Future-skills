# Future Skills assignment log

## Introduction

I will try to develop the assesment on Ubuntu 24 WSL with docker-ce installed. Afterwards I could run the containers on my Raspberry Pi 3B, which is quite slow and has only 1 GB of RAM. But a one page site it can handle.

The Pi is running containerd and uses nerdctl with an alias so I can use it like docker.

Of course I will try to make optimal use of Copilot while still applying my own skills

## Phase 1.

The containers would not start: Creating network "phase-1-basic_webnet" with driver "bridge"
ERROR: all predefined address pools have been fully subnetted, so I had to add a custom subnet.
```yaml
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

The I had some trouble overwriting the default Nginx config, so first my container only produced 404. For some reason my normal Nginx uses conf.d but this was using http.d, probably Alpine related.

```bash
rzuidhof@WINKPN-F0G8XL3:(main)~/mcp/Future-skills/Phase-1-Basic$ curl -i http://localhost
HTTP/1.1 200 OK
Server: nginx/1.27.5
Date: Sun, 27 Apr 2025 11:19:14 GMT
Content-Type: text/html
Content-Length: 256
Connection: keep-alive
Last-Modified: Sun, 27 Apr 2025 10:18:20 GMT
ETag: "680e046c-100"
Accept-Ranges: bytes
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Server</title>
</head>
<body>
    <h1>Hello from Web Server via Reverse Proxy!</h1>
</body>
</html>
```

I think the requirement to "Ensure no other containers are accessible directly from the host." is sufficiently covered by the custom bridge network and not exposing the web container by port forwarding.

Used "docker exec -it" and "curl" to troubleshoot an initial 404 error. chmod and chown did not seem very relevant for this assignment. Used "docker network ls" to show the different networks.

Phase 1 took about 1,5 hours to finish.

## Phase 2.

For Phase 2 I had to rework some of Phase 1. My choice to use subdirectories for each phase caused 30 minutes of trial and error before the Github actions worked as expected.
Time for Phase 2 was 2 hours.

## Phase 3.

### 3.1

Generated self-signed certs
```openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout certs/key.pem \
  -out certs/cert.pem \
  -subj "/CN=futskill.com"
```

```rzuidhof@WINKPN-F0G8XL3:(main)~/mcp/Future-skills/Phase-3-Expert$ curl -ik https://localhost:443
HTTP/1.1 200 OK
Server: nginx/1.27.5
Date: Thu, 29 May 2025 17:46:45 GMT
Content-Type: text/html
Content-Length: 350
Connection: keep-alive
Last-Modified: Sun, 27 Apr 2025 10:18:30 GMT
ETag: "680e0476-15e"
Accept-Ranges: bytes
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert Phase Web Server</title>
</head>
<body>
    <h1>Hello from the Expert Phase Web Server via Reverse Proxy!</h1>
    <p>This page is served through the NGINX reverse proxy.</p>
</body>
</html>


rzuidhof@WINKPN-F0G8XL3:(main)~/mcp/Future-skills/Phase-3-Expert$ curl -ik http://localhost
HTTP/1.1 301 Moved Permanently
Server: nginx/1.27.5
Date: Thu, 29 May 2025 17:48:01 GMT
Content-Type: text/html
Content-Length: 169
Connection: keep-alive
Location: https://localhost/

<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.27.5</center>
</body>
</html>
```

### 3.2

Used example from elastic.co site to add ELK containers. At first logs did not show up because the default Discover index pattern did not match logstash-*, indeed logstash is being replaced by filebeat. Naming the index log-backend did not help, for some reason the index was not auto-created. So finally named it filebeat-backend.

### 3.3

Alpine based backed image was 60 MB smaller than default Python image
phase-3-expert-backend                          latest             b864ffe0e76d   4 minutes ago   103MB
<none>                                          <none>             e58e111e61d3   2 weeks ago     161MB

### 3.4

Unit test built into the backend container image
Nginx test built into the nginx container
Separate tests to run after the platform has been launched:
    docker compose --profile tests run --rm test1
    docker compose --profile tests run --rm test2

### 3.5

