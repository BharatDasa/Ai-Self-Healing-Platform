# Kubernetes Namespaces

## Overview

The platform is divided into isolated namespaces.

---

## Namespaces

| Namespace | Purpose |
|------------|---------|
| ai-platform | AI services |
| airflow | MLOps |
| monitoring | Prometheus stack |
| messaging | Kafka |
| ingress-nginx | Ingress controller |
| istio-system | Service mesh |
| cert-manager | TLS certificates |

---

## Verify

```bash
kubectl get ns
```

---

## Benefits

- Isolation
- Security
- Resource management