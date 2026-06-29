#!/bin/bash

set -e

echo ""
echo "=================================================="
echo "🚀 ENTERPRISE KAFKA TOPIC SETUP"
echo "=================================================="
echo ""

# =====================================================
# CONFIG
# =====================================================

KAFKA_POD="kafka-0"

NAMESPACE="messaging"

BOOTSTRAP="localhost:9092"

TOPICS=(
  "transactions"
  "fraud_alerts"
)

# =====================================================
# DELETE EXISTING TOPICS
# =====================================================

echo "🧹 Cleaning old Kafka topics..."

for topic in "${TOPICS[@]}"
do

  echo ""
  echo "🗑 Deleting topic: ${topic}"

  kubectl exec -i ${KAFKA_POD} -n ${NAMESPACE} -- \
  /opt/kafka/bin/kafka-topics.sh \
  --delete \
  --topic ${topic} \
  --bootstrap-server ${BOOTSTRAP} \
  || true

done

# =====================================================
# WAIT FOR FULL DELETION
# =====================================================

echo ""
echo "⏳ Waiting for Kafka topic cleanup..."

for topic in "${TOPICS[@]}"
do

  while kubectl exec -i ${KAFKA_POD} -n ${NAMESPACE} -- \
  /opt/kafka/bin/kafka-topics.sh \
  --list \
  --bootstrap-server ${BOOTSTRAP} \
  | grep -w ${topic} > /dev/null
  do

    echo "⌛ Topic still exists: ${topic}"

    sleep 5

  done

  echo "✅ Topic deleted: ${topic}"

done

# =====================================================
# CREATE TRANSACTIONS TOPIC
# =====================================================

echo ""
echo "📦 Creating transactions topic..."

kubectl exec -i ${KAFKA_POD} -n ${NAMESPACE} -- \
/opt/kafka/bin/kafka-topics.sh \
--create \
--topic transactions \
--bootstrap-server ${BOOTSTRAP} \
--partitions 3 \
--replication-factor 1 \
--config retention.ms=21600000 \
--config segment.ms=3600000 \
--config cleanup.policy=delete

# =====================================================
# CREATE FRAUD ALERTS TOPIC
# =====================================================

echo ""
echo "🚨 Creating fraud_alerts topic..."

kubectl exec -i ${KAFKA_POD} -n ${NAMESPACE} -- \
/opt/kafka/bin/kafka-topics.sh \
--create \
--topic fraud_alerts \
--bootstrap-server ${BOOTSTRAP} \
--partitions 3 \
--replication-factor 1 \
--config retention.ms=7200000 \
--config segment.ms=1800000 \
--config cleanup.policy=delete

# =====================================================
# VERIFY CONFIGURATION
# =====================================================

echo ""
echo "📋 FINAL TOPIC CONFIGURATION"
echo "=================================================="

kubectl exec -i ${KAFKA_POD} -n ${NAMESPACE} -- \
/opt/kafka/bin/kafka-topics.sh \
--describe \
--bootstrap-server ${BOOTSTRAP}

echo ""
echo "=================================================="
echo "✅ ENTERPRISE KAFKA SETUP COMPLETED"
echo "=================================================="
echo ""
