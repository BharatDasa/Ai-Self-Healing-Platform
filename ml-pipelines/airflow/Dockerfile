FROM apache/airflow:2.9.3-python3.11

# =====================================================
# ROOT SETUP
# =====================================================

USER root

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    build-essential \
    curl \
    && apt-get clean

# =====================================================
# WORKDIR
# =====================================================

WORKDIR /opt/airflow

# =====================================================
# COPY REQUIREMENTS
# =====================================================

COPY requirements.txt .

# =====================================================
# SWITCH TO AIRFLOW USER
# =====================================================

USER airflow

# =====================================================
# INSTALL PYTHON PACKAGES
# =====================================================

RUN pip install --no-cache-dir -r requirements.txt

# =====================================================
# SWITCH BACK TO ROOT
# =====================================================

USER root

# =====================================================
# CREATE SHARED NFS DIRECTORIES
# =====================================================

RUN mkdir -p \
/opt/airflow/dags/ml-pipelines/dags \
/opt/airflow/dags/ml-pipelines/scripts \
/opt/airflow/dags/ml-pipelines/models \
/opt/airflow/dags/ml-pipelines/analytics/exports \
/opt/airflow/dags/ml-pipelines/analytics/reports

# =====================================================
# FIX OWNERSHIP
# =====================================================

RUN chown -R airflow:root \
/opt/airflow/dags/ml-pipelines

# =====================================================
# FINAL USER
# =====================================================

USER airflow
