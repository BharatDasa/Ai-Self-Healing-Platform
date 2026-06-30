# Kubernetes Ingress

Ingress is the external entry point for the platform.

## Responsibilities

* expose services
* route traffic
* centralize access
* integrate with Istio

---

## Traffic Flow

```text
External Users
      ↓
Ingress Controller
      ↓
Istio Gateway
      ↓
VirtualService
      ↓
Applications
```

---

## Exposed Services

* Fraud Detection API
* Airflow UI
* Grafana
* Prometheus

---

## Verify

```bash
kubectl get ingress -A
```

Ingress acts as the north-south entry point for the platform.
