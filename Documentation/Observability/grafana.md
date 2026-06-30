# Grafana

Grafana provides visualization and dashboards.

## Dashboards

* AI Metrics
* Kubernetes Cluster
* Kafka
* Airflow
* Istio Service Mesh
* Loki Logs
* Tempo Traces
* Self-Healing Dashboard

## Panels

* Event Rate
* AI Model Score
* Target Replicas
* CPU Usage
* Memory Usage
* Restart Count
* KEDA Scaling
* Pod Recovery Timeline

## Access

```bash
kubectl port-forward svc/grafana 3000:3000
```

Open:

```text
http://localhost:3000
```

Grafana is the visualization layer of the platform.
