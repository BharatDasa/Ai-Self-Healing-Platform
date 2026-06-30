# RBAC

## Purpose

Controls permissions inside Kubernetes.

---

## Resources

- ServiceAccounts
- Roles
- ClusterRoles
- RoleBindings
- ClusterRoleBindings

---

## Verify

```bash
kubectl get sa -A

kubectl get roles -A

kubectl get rolebindings -A
```

---

## Benefits

- Least privilege
- Secure access