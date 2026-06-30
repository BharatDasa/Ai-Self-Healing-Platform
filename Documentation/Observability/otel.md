# OpenTelemetry

## Overview

OpenTelemetry provides telemetry collection for metrics, logs, and traces.

---

# Pipeline

```text
Applications
      ↓
OpenTelemetry SDK
      ↓
OTEL Collector
      ↓
Prometheus
      ↓
Tempo
      ↓
Grafana
```

---

# Responsibilities

* trace export
* metric export
* telemetry collection
* observability integration

---

# Components

## OTEL SDK

Embedded inside applications.

## OTEL Collector

Processes telemetry.

## Exporters

* Prometheus
* Tempo

---

# Integration

```text
Istio Sidecars
      ↓
OTEL Collector
      ↓
Tempo
      ↓
Grafana
```

---

# Verify

```bash
kubectl get pods -n monitoring
```

---

# Benefits

* vendor-neutral telemetry
* distributed tracing
* observability standardization
