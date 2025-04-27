# Phase 2: Intermediate Level

## 🎯 Objective

In this phase, you will extend your solution by adding a backend application and automating deployment using CI/CD pipelines.

## 📌 Tasks

1. **Add a backend application container**
   - Write a simple API in Flask (Python) or Express (Node.js).
   - Must include a health endpoint (e.g. `GET /api/health → { status: "ok" }`).
   - Build your own image starting from a minimal base.

2. **Update NGINX to proxy both web and API traffic**
   - Static site served at `/`
   - API routed to `/api`
   - Example:
     ```nginx
     location /api {
       proxy_pass http://backend:5000;
     }
     ```

3. **Manage services with Docker Compose**
   - Update `docker-compose.yml` to include the new backend.
   - Keep reverse proxy as the single exposed component.

4. **Health checks**
   - Add Docker `HEALTHCHECK` for both the backend and web server.
   - Use HTTP probes to `/` and `/api/health`.

5. **Environment variable usage**
   - Use `.env` files to inject values like ports, service names, and debug flags.

6. **CI/CD Pipeline with GitHub Actions**
   - On every push:
     - Build all Docker images
     - Lint configuration files
     - Validate Compose config with `docker-compose config`
     - Test container availability via `curl` or equivalent

## 🧪 Example Test Command

```bash
curl -i http://localhost/api/health
# Expected Output: { status: "ok" }
```

## 📦 Deliverables

- Update your `docker-compose.yml` to include the backend service.
- Ensure NGINX is configured to route traffic correctly.
- Document any changes made to the architecture or services.

## 🧾 Evaluation Criteria

- **Technical Skill**: Use of Docker, NGINX, Compose, CI/CD.
- **Security**: Proper routing and access controls.
- **Clarity**: Clear documentation of changes and architecture.
- **Problem Solving**: Effective debugging and testing strategies.
- **Documentation**: Comprehensive coverage of the new features and configurations.

