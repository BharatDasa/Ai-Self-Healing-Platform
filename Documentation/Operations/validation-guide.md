# Validation Guide

## Kubernetes

```bash
kubectl get pods -A

kubectl get svc -A
```

---

## KEDA

```bash
kubectl get scaledobject -A

kubectl get hpa -A
```

---

## Argo Rollouts

```bash
kubectl argo rollouts list rollouts -A

kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

## Kafka

```bash
kubectl get pods -n messaging
```

---

## Airflow

```bash
kubectl get pods -n airflow

airflow dags list
```

---

## Monitoring

```bash
kubectl get pods -n monitoring
```

Verify:

* Prometheus
* Grafana
* Loki
* Tempo
* Alertmanager
* Promtail

---

## Istio

```bash
kubectl get pods -n istio-system
```

Verify:

* ingress gateway
* envoy sidecars
* service mesh

---

## Metrics Validation

Verify:

* ai_event_rate
* ai_model_score
* ai_target_replicas
* scaling_actions_total
* restart_actions_total
