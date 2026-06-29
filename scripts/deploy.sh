#!/bin/bash

set -e

echo "🚀 Deploying AI Self-Healing Platform..."

kubectl apply -f k8s/namespace/namespace.yaml

kubectl apply -f k8s/base/

kubectl apply -f k8s/keda/

kubectl apply -f k8s/argo-rollouts/

echo "⏳ Waiting for deployments..."
kubectl argo rollouts get rollout fraud-detection -n ai-platform
kubectl rollout status deploy/self-healing -n ai-platform
kubectl rollout status deploy/transaction-simulator -n ai-platform

echo "✅ Deployment complete"

kubectl get pods -n ai-platform

