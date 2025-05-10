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

