# cert-manager

cert-manager automates TLS certificate management.

## Responsibilities

* issue certificates
* renew certificates
* manage secrets

---

## Components

* Certificate
* ClusterIssuer
* Secret

---

## Verify

```bash
kubectl get pods -n cert-manager

kubectl get certificate -A

kubectl get clusterissuer
```

---

## Benefits

* automated TLS
* secure traffic
* certificate renewal
* production-grade HTTPS
