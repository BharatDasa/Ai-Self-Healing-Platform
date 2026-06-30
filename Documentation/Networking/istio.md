# Istio Service Mesh

## Overview

The AI Self-Healing Kubernetes Platform uses Istio as the service mesh layer.

Istio provides:

* traffic management
* service discovery
* telemetry collection
* distributed tracing
* security policies
* observability integration

---

# Architecture

```text
External User
      ↓
Ingress Controller
      ↓
Istio Gateway
      ↓
VirtualService
      ↓
Envoy Sidecars
      ↓
Platform Services
```

---

# Components

## Istiod

Control plane responsible for:

* service discovery
* sidecar configuration
* routing policies

---

## Ingress Gateway

Acts as the entry point into the mesh.

Provides:

* HTTP routing
* HTTPS termination
* external access

---

## Envoy Sidecars

Injected into workloads.

Responsibilities:

* traffic interception
* metrics generation
* distributed tracing
* policy enforcement

---

# Observability Integration

```text
Envoy Sidecars
       ↓
OpenTelemetry
       ↓
Tempo
       ↓
Grafana
```

Metrics:

```text
Envoy
   ↓
Prometheus
   ↓
Grafana
```

Logs:

```text
Applications
     ↓
Promtail
     ↓
Loki
     ↓
Grafana
```

---

# Verify Istio

Check control plane:

```bash
kubectl get pods -n istio-system
```

Verify sidecars:

```bash
kubectl get pods -A -o wide
```

Describe pod:

```bash
kubectl describe pod POD_NAME
```

---

# Service Mesh Features

* traffic management
* retries
* fault injection
* telemetry
* tracing
* security
* observability

---

# Benefits

* runtime visibility
* distributed tracing
* centralized traffic control
* production-grade networking
