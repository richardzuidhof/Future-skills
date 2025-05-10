# Future Skills Assignment – DevOps Engineer (Modernisation)

## 🔹 Phase 3: Expert Level

### 🎯 Objective

In this phase, you will design a production-like system that includes HTTPS, observability, and robust deployment automation.

### 📌 Tasks

1. **Enable HTTPS**
   - Configure the NGINX reverse proxy to serve over HTTPS.
   - Use a self-signed certificate for local testing or simulate Let's Encrypt with Certbot if applicable.
   - Ensure HTTP traffic is redirected to HTTPS (301).

2. **Centralized logging**
   - Integrate a log stack such as ELK (Elasticsearch, Logstash, Kibana) or Loki + Promtail + Grafana.
   - Ensure all containers forward logs to the central logging system, including both application logs and access logs.

3. **Custom backend image**
   - Build a backend image from scratch, avoiding base images like `python:3` or `node:18`.
   - Use minimal base images like `alpine` and install only the necessary dependencies.

4. **Extended testing**
   - Add unit tests for the backend application using testing frameworks like `pytest` or `jest`.
   - Validate the NGINX configuration with `nginx -t`.
   - Perform functional tests to ensure the homepage loads and the `/api/health` endpoint responds with a 200 status.

5. **Advanced CI/CD pipeline**
   - Implement a fully automated GitHub Actions pipeline that includes:
     - Linting, testing, building, and deploying.
     - Running the test suite.
     - Tagging Docker images.
     - Automatically redeploying on pushes to the `main` branch.

6. **Failure handling**
   - Configure auto-restart for containers in case of failure.
   - Implement load balancing across multiple backend containers using NGINX upstream configuration.

### 🧪 Example Test Commands

- To test the HTTPS setup:
  ```bash
  curl -k https://localhost
  # Expected Output: HTML content from the webserver, with NGINX headers visible
  ```

- To validate the health endpoint:
  ```bash
  curl -i https://localhost/api/health
  # Expected Output: { status: "ok" }
  ```

### 📦 Deliverables

Ensure that all components are properly documented and structured as per the project requirements.