# Kubernetes Secrets

## Overview

Secrets store sensitive information used by applications.

---

## Secrets Used

### MongoDB

```text
mongodb-secret
```

Contains:

- username
- password

---

### PostgreSQL

```text
postgres-secret
```

Contains:

- user
- password

---

### DockerHub

```text
dockerhub-secret
```

Used for image pulls.

---

### Slack Webhook

```text
slack-webhook-secret
```

Used by Alertmanager.

---

### GitHub SSH

Used by Jenkins.

---

## Verify

```bash
kubectl get secrets -A
```

---

## Describe

```bash
kubectl describe secret SECRET_NAME
```

---

## Benefits

- secure credentials
- centralized management
- encrypted storage