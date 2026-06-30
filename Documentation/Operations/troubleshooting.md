# Troubleshooting Guide

# Pods Not Starting

```bash
kubectl get pods -A

kubectl describe pod POD_NAME

kubectl logs POD_NAME
```

---

# CrashLoopBackOff

```bash
kubectl logs POD_NAME --previous
```

---

# Kafka Issues

```bash
kubectl get pods -n messaging

kubectl logs kafka-0 -n messaging
```

---

# MongoDB Problems

```bash
kubectl get pods -n database

kubectl logs mongodb-0
```

---

# PostgreSQL Problems

```bash
kubectl logs postgres-0
```

---

# Argo Rollout Problems

```bash
kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

# KEDA Problems

```bash
kubectl describe scaledobject fraud-prometheus-keda -n ai-platform

kubectl get hpa -A
```

---

# Prometheus Targets

```bash
kubectl port-forward svc/prometheus-operated 9090

http://localhost:9090/targets
```

---

# Grafana

Verify dashboards.

---

# Loki

Verify logs.

---

# Tempo

Verify traces.

---

# Alertmanager

Verify Slack notifications.
