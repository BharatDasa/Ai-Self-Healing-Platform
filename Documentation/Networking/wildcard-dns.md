# Wildcard DNS

The platform uses wildcard DNS.

## Domain

```text
*.platform.local
```

Examples:

```text
grafana.platform.local

airflow.platform.local

fraud.platform.local

prometheus.platform.local
```

---

## Flow

```text
User Request
      ↓
Wildcard DNS
      ↓
Ingress Controller
      ↓
Istio Gateway
```

---

## Benefits

* centralized routing
* easy service exposure
* scalable architecture
* simplified management
