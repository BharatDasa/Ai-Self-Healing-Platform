# Istio VirtualService

## Overview

VirtualService controls routing inside the service mesh.

It defines:

* host names
* destination services
* ports
* traffic routing rules

---

# Request Flow

```text
External Request
       ↓
Ingress Controller
       ↓
Istio Gateway
       ↓
VirtualService
       ↓
Kubernetes Service
       ↓
Pods
```

---

# Platform Services

## Fraud Detection

```text
fraud.platform.local
```

Destination:

```text
fraud-detection
```

---

## Grafana

```text
grafana.platform.local
```

Destination:

```text
grafana
```

---

## Airflow

```text
airflow.platform.local
```

Destination:

```text
airflow-webserver
```

---

## Prometheus

```text
prometheus.platform.local
```

Destination:

```text
prometheus-operated
```

---

# Example Resource

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
```

---

# Verify

List all VirtualServices:

```bash
kubectl get virtualservice -A
```

Describe:

```bash
kubectl describe virtualservice
```

---

# Features

* host-based routing
* traffic control
* canary support
* service discovery

---

# Benefits

VirtualService provides flexible routing inside the service mesh.
