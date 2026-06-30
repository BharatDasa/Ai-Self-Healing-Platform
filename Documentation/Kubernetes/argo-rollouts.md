# Argo Rollouts

## Overview

Fraud Detection uses Argo Rollouts for progressive delivery.

---

## Verify

```bash
kubectl argo rollouts get rollout fraud-detection -n ai-platform
```

---

## Rollout History

```bash
kubectl argo rollouts history fraud-detection -n ai-platform
```

---

## Restart

```bash
kubectl argo rollouts restart fraud-detection -n ai-platform
```

---

## Undo

```bash
kubectl argo rollouts undo fraud-detection -n ai-platform
```

---

## Benefits

- Canary deployments
- Safe upgrades
- Rollbacks