# MongoDB Recovery Runbook

## Symptoms

- Connection failure
- Write errors
- Query timeout

---

## Check Pods

```bash
kubectl get pods -n database
```

---

## Restart MongoDB

```bash
kubectl rollout restart sts mongodb -n database
```

---

## Verify Logs

```bash
kubectl logs mongodb-0 -n database
```

---

## Backup

```bash
mongodump
```

---

## Restore

```bash
mongorestore backup/
```

---

## Verify

```bash
kubectl exec -it mongodb-0 -n database -- mongosh
```

---

## Success Criteria

- Database reachable
- Queries successful