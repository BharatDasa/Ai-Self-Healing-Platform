#!/bin/bash

set -e

echo "🚀 Building Docker images..."

docker build --no-cache -t bharatdasa/transaction-simulator:v1 .
docker push bharatdasa/transaction-simulator:v1

docker build --no-cache -t bharatdasa/fraud_ai_ml:latest .
docker push bharatdasa/fraud_ai_ml:latest

docker build --no-cache -t bharatdasa/self-healing_ai_ml:v2 .
docker push bharatdasa/self-healing_ai_ml:v2

docker build --no-cache -t bharatdasa/enterprise-airflow:latest .
docker push bharatdasa/enterprise-airflow:latest


echo "✅ Build complete"
