# AI Self-Healing Architecture

## Overview

The AI self-healing engine continuously analyzes fraud events and infrastructure pressure.

It performs:

- anomaly detection
- predictive scaling
- restart decisions
- autonomous recovery
- AI metrics export

---

## Architecture

Transaction Events

↓

Kafka Consumer

↓

Sliding Event Window

↓

Feature Engineering

↓

AI Prediction Engine

↓

Pressure Score

↓

Decision Engine

↓

Prometheus Metrics

↓

KEDA

↓

Argo Rollouts

↓

Kubernetes Pods

---

## Components

### Kafka Consumer

Receives fraud events.

### Predict Scale

Calculates pressure.

### Decision Engine

Determines action.

### Metrics Exporter

Publishes AI metrics.

### Restart Engine

Performs rollout restart.

---

## Autonomous Actions

- NORMAL
- ELEVATED
- SCALE
- RESTART