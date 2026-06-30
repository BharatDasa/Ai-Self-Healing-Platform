# Health Endpoints

## Overview

Health endpoints are used by Kubernetes readiness and liveness probes.

---

# Fraud Detection Health

## Request

```http
GET /health
```

---

## Response

```json
{
  "status": "healthy",
  "service": "fraud-detection"
}
```

---

# Verify

```bash
curl http://localhost:8000/health
```

---

# Kubernetes Integration

Used by:

- readiness probes
- liveness probes
- service monitoring

---

# Example Probe

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000

readinessProbe:
  httpGet:
    path: /health
    port: 8000
```

---

# Benefits

- automatic recovery
- pod health validation
- high availability