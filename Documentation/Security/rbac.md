# RBAC Architecture

## Overview

Role-Based Access Control (RBAC) restricts permissions inside Kubernetes.

---

## Namespaces

- ai-platform
- monitoring
- airflow
- database
- messaging

---

## RBAC Components

### Roles

Define namespace permissions.

### ClusterRoles

Provide cluster-wide permissions.

### RoleBindings

Associate roles with users.

### ServiceAccounts

Used by workloads.

---

## Verify

```bash
kubectl get roles -A

kubectl get rolebindings -A

kubectl get clusterroles
```

---

## Benefits

- least privilege
- namespace security
- workload isolation
- controlled access