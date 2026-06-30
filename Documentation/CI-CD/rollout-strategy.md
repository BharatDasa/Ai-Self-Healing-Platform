# Argo Rollout Strategy

## Overview

The platform uses Argo Rollouts for progressive delivery.

---

## Features

- Canary deployments
- Safe upgrades
- Zero downtime
- Rollback capability

---

## Deployment Flow

GitHub Push

↓

Jenkins

↓

Docker Build

↓

Push DockerHub

↓

Argo Rollouts

↓

Traffic Shift

↓

Production

---

## Verify

```bash
kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

## History

```bash
kubectl argo rollouts history fraud-detection -n ai-platform
```

---

## Benefits

- Progressive delivery
- Reduced risk
- Safer releases