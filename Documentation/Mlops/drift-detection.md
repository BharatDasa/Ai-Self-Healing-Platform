# Drift Detection

The platform continuously evaluates model quality.

## Drift Signals

* changing fraud patterns
* unusual event rates
* prediction instability
* feature distribution changes

## Drift Flow

```text
Current Events
      ↓
Compare With Baseline
      ↓
Calculate Drift Score
      ↓
Generate Report
      ↓
Trigger Retraining
```

## Outputs

Generated reports:

```text
drift_report.txt
```

Metrics exported:

* ai_model_score
* ai_event_rate

Retraining is triggered automatically through Airflow.

Reports are stored on NFS.
