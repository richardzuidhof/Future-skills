# Phase 1: Basic Level

## Objective

This phase focuses on building a minimal local web platform using containers. The setup consists of a reverse proxy (NGINX) and one or more web server containers serving static HTML content.

## Project Structure

- **Reverse Proxy (NGINX)**: The single entry point for all HTTP traffic.
- **Web Server Container**: Serves static HTML content.

## Tasks

1. **Build a Web Server Container**
   - Create a `Dockerfile` that installs and configures a basic web server.
   - Use `nginx`, `httpd`, or a minimal alternative.
   - The server must serve a simple HTML file (e.g., "Hello from Web Server via Reverse Proxy!").
   - Do not use full prebuilt images; start from `alpine` or `debian`.

2. **Build a Reverse Proxy Container**
   - Create a second container with NGINX configured as a reverse proxy.
   - It must:
     - Listen on ports `80` and `443`.
     - Forward all incoming traffic to the internal web server(s).
   - Direct access to web server(s) must not be exposed to the host.

3. **Docker Compose Setup**
   - Use `docker-compose.yml` to define both the reverse proxy and the web server container(s).
   - Define a custom Docker network so containers communicate by name.
   - Only expose the **reverse proxy** to the outside world.
   - You may choose to scale the web server component (e.g., `--scale web=2`), but it's not required.

4. **Security Configuration**
   - Add the following hardening to the reverse proxy:
     - Block HTTP methods like `TRACE` and `OPTIONS`.
     - Set headers including:
       - `X-Frame-Options: DENY`
       - `Content-Security-Policy: default-src 'self'`
   - Ensure no other containers are accessible directly from the host.

5. **Linux Fundamentals**
   - Demonstrate command-line skills by:
     - Managing file permissions with `chmod` and `chown`.
     - Using tools like `curl`, `ping`, and `ip a` to test connectivity.
     - Using Docker CLI commands to verify network isolation.

6. **Verification**
   - Start the environment with `docker-compose up`.
   - Run a `curl` command against `http://localhost` and confirm:
     - The response comes from the web server.
     - The NGINX proxy is the entry point (confirm via headers or logs).
   - Do **not** expose or access the web server directly.

## Example Test Command

```bash
curl -i http://localhost
# Expected Output: HTML content from the webserver, with NGINX headers visible
```

## Conclusion

This phase sets the foundation for understanding containerization, reverse proxying, and basic web serving. Ensure to follow the tasks and objectives closely to achieve a successful setup.