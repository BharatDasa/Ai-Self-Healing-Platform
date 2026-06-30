# Tempo

## Overview

Tempo provides distributed tracing for the platform.

It enables end-to-end request visibility across services.

---

# Trace Flow

```text
Applications
       ↓
Istio Envoy Sidecars
       ↓
OpenTelemetry SDK
       ↓
OTEL Collectors
       ↓
Tempo
       ↓
Grafana
```

---

# Trace Sources

* Fraud Detection API
* Self-Healing Engine
* Kafka Consumers
* Airflow DAGs
* Istio Sidecars

---

# Responsibilities

* distributed tracing
* latency analysis
* request visibility
* service dependency analysis

---

# Verify

```bash
kubectl get pods -n monitoring
```

Port forward Grafana:

```bash
kubectl port-forward svc/grafana 3000:3000
```

---

# Benefits

* request debugging
* latency analysis
* dependency visualization
* production observability
