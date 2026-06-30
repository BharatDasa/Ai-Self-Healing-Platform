# PostgreSQL Recovery Runbook

## Symptoms

- Airflow failures
- Connection errors
- Metadata unavailable

---

## Check Pod

```bash
kubectl get pods -n database
```

---

## Restart PostgreSQL

```bash
kubectl rollout restart sts postgres -n database
```

---

## Verify Logs

```bash
kubectl logs postgres-0 -n database
```

---

## Backup

```bash
pg_dump postgres > backup.sql
```

---

## Restore

```bash
psql postgres < backup.sql
```

---

## Verify

```bash
kubectl exec -it postgres-0 -n database -- psql
```

---

## Success Criteria

- PostgreSQL reachable
- Airflow metadata restored