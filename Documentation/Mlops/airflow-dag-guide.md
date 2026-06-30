# Airflow DAG Guide

The AI Self-Healing Kubernetes Platform uses Apache Airflow to orchestrate MLOps workflows.

## DAG Flow

```text
feature_pipeline_dag
        ↓
fraud_training_dag
        ↓
scaling_training_dag
        ↓
drift_detection_dag
        ↓
retraining_pipeline_dag
        ↓
analytics_export_dag
        ↓
cleanup_pipeline_dag
```

## DAG Descriptions

### feature_pipeline_dag

Performs:

* feature engineering
* dataset preparation
* normalization

### fraud_training_dag

Builds:

* fraud_model.pkl

### scaling_training_dag

Builds:

* scaling_model.pkl

### drift_detection_dag

Detects:

* feature drift
* prediction instability

### retraining_pipeline_dag

Automatically retrains models.

### analytics_export_dag

Exports:

* fraud_history.csv
* anomaly_history.csv
* scaling_history.csv

### cleanup_pipeline_dag

Performs retention cleanup.

## Components

* Airflow Webserver
* Airflow Scheduler
* Airflow Workers
* PostgreSQL Metadata Database
* NFS Shared Storage
