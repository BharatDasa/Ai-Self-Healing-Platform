#!/bin/bash

set -euo pipefail

# =====================================================
# 🔥 AI SELF-HEALING PLATFORM
# 🔥 PERSISTENT MLOPS PIPELINE DEPLOYMENT
# =====================================================

echo ""
echo "====================================================="
echo "🚀 DEPLOYING PERSISTENT ML PIPELINES"
echo "====================================================="

# =====================================================
# CONFIG
# =====================================================

NAMESPACE="airflow"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ML_BASE="$BASE_DIR/airflow"

AIRFLOW_BASE="/opt/airflow/dags/ml-pipelines"

# =====================================================
# GET AIRFLOW PODS
# =====================================================

WEBSERVER_POD=$(kubectl get pod \
  -n $NAMESPACE \
  -l app=airflow-webserver \
  -o jsonpath='{.items[0].metadata.name}')

SCHEDULER_POD=$(kubectl get pod \
  -n $NAMESPACE \
  -l app=airflow-scheduler \
  -o jsonpath='{.items[0].metadata.name}')

WORKER_POD=$(kubectl get pod \
  -n $NAMESPACE \
  -l app=airflow-worker \
  -o jsonpath='{.items[0].metadata.name}')

# =====================================================
# SHOW PODS
# =====================================================

echo ""
echo "📦 AIRFLOW PODS"
echo ""

echo "🌐 Webserver : $WEBSERVER_POD"
echo "🧠 Scheduler : $SCHEDULER_POD"
echo "⚙️ Worker    : $WORKER_POD"

# =====================================================
# CREATE PERSISTENT DIRECTORIES
# =====================================================

echo ""
echo "📁 Creating persistent ML directories..."

for POD in \
  $WEBSERVER_POD \
  $SCHEDULER_POD \
  $WORKER_POD
do

kubectl exec -n $NAMESPACE $POD -- \
mkdir -p \
$AIRFLOW_BASE/dags \
$AIRFLOW_BASE/scripts \
$AIRFLOW_BASE/models \
$AIRFLOW_BASE/analytics/exports \
$AIRFLOW_BASE/analytics/reports

done

echo ""
echo "✅ Persistent directories created"

# =====================================================
# COPY DAGS
# =====================================================

echo ""
echo "📤 Copying DAG files..."

kubectl cp \
$ML_BASE/dags/. \
$NAMESPACE/$WEBSERVER_POD:$AIRFLOW_BASE/dags/

echo ""
echo "✅ DAG files copied"

# =====================================================
# COPY ML FILES
# =====================================================

echo ""
echo "📤 Copying ML scripts/models/analytics..."

for POD in \
  $WEBSERVER_POD \
  $SCHEDULER_POD \
  $WORKER_POD
do

echo ""
echo "➡ Deploying to $POD"

kubectl cp \
$ML_BASE/scripts/. \
$NAMESPACE/$POD:$AIRFLOW_BASE/scripts/

kubectl cp \
$ML_BASE/models/. \
$NAMESPACE/$POD:$AIRFLOW_BASE/models/

kubectl cp \
$ML_BASE/analytics/. \
$NAMESPACE/$POD:$AIRFLOW_BASE/analytics/

done

echo ""
echo "✅ ML files deployed"

# =====================================================
# INSTALL PYTHON PACKAGES
# =====================================================

echo ""
echo "📦 Installing ML Python packages..."

for POD in \
  $WEBSERVER_POD \
  $SCHEDULER_POD \
  $WORKER_POD
do

echo ""
echo "➡ Installing inside $POD"

kubectl exec -n $NAMESPACE $POD -- \
bash -c "
python -m pip install \
--break-system-packages \
pandas \
numpy \
scikit-learn \
pymongo \
psycopg2-binary \
joblib
"

done

echo ""
echo "✅ Python packages installed"

# =====================================================
# VALIDATE DEPLOYMENT
# =====================================================

echo ""
echo "🔍 Validating persistent ML deployment..."

kubectl exec -n $NAMESPACE $WEBSERVER_POD -- \
ls -R $AIRFLOW_BASE

echo ""
echo "✅ Validation completed"

# =====================================================
# VERIFY AIRFLOW DAGS
# =====================================================

echo ""
echo "📊 Checking Airflow DAG visibility..."

kubectl exec -n $NAMESPACE $WEBSERVER_POD -- \
airflow dags list | grep pipeline || true

# =====================================================
# FINAL STATUS
# =====================================================

echo ""
echo "====================================================="
echo "✅ PERSISTENT ML PIPELINES DEPLOYED"
echo "====================================================="

echo ""
echo "📊 ACTIVE AIRFLOW PODS"
echo ""

kubectl get pods -n $NAMESPACE

echo ""
echo "🔥 AVAILABLE ML PIPELINES"
echo ""

echo "✔ feature_pipeline"
echo "✔ analytics_export_pipeline"
echo "✔ fraud_training_pipeline"
echo "✔ scaling_training_pipeline"
echo "✔ drift_detection_pipeline"
echo "✔ retraining_pipeline"
echo "✔ cleanup_pipeline"

echo ""
echo "🌐 OPEN AIRFLOW UI"
echo ""

echo "🔥 RUN PIPELINES IN THIS ORDER:"
echo ""
echo "1️⃣ feature_pipeline"
echo "2️⃣ analytics_export_pipeline"
echo "3️⃣ fraud_training_pipeline"
echo "4️⃣ scaling_training_pipeline"
echo "5️⃣ drift_detection_pipeline"
echo "6️⃣ retraining_pipeline"
echo "7️⃣ cleanup_pipeline"

echo ""
echo "====================================================="
echo "🧠 MLOPS PLATFORM READY"
echo "====================================================="
echo ""
