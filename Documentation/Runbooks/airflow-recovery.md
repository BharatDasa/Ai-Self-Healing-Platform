# Airflow Recovery Runbook

## Symptoms

- DAG failures
- Scheduler unavailable
- Webserver inaccessible

---

## Check Pods

```bash
kubectl get pods -n airflow
```

---

## Restart Webserver

```bash
kubectl rollout restart deploy airflow-webserver -n airflow
```

---

## Restart Scheduler

```bash
kubectl rollout restart deploy airflow-scheduler -n airflow
```

---

## Verify DAGs

```bash
kubectl exec -it POD_NAME -n airflow -- airflow dags list
```

---

## Verify Logs

```bash
kubectl logs POD_NAME -n airflow
```

---

## Success Criteria

- DAGs visible
- Scheduler healthy
- Tasks executing