#!/bin/bash

echo "🧪 Running platform validation..."

echo ""
echo "📦 Pods"
kubectl get pods -n ai-platform

echo ""
echo "📊 Services"
kubectl get svc -n ai-platform

echo ""
echo "📈 HPA / KEDA"
kubectl get scaledobject -n ai-platform

echo ""
echo "🧠 ServiceMonitor"
kubectl get servicemonitor -n monitoring

echo ""
echo "🔥 Recent self-healing logs"
kubectl logs deploy/self-healing -n ai-platform --tail=20

echo ""
echo "✅ Validation complete"
