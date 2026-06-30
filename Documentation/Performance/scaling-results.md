# Scaling Results

## KEDA Autoscaling Results

---

# Configuration

Minimum Replicas:

1

Maximum Replicas:

5

Polling Interval:

15 seconds

Cooldown:

60 seconds

---

# AI Metrics

Metric:

ai_target_replicas

Source:

Prometheus

Consumer:

KEDA

---

# Scaling Scenarios

## Normal

Event Rate:

0-4

Decision:

NORMAL

Replicas:

1

---

## Elevated

Event Rate:

5-14

Decision:

ELEVATED

Replicas:

2

---

## Scale

Event Rate:

15-19

Decision:

SCALE

Replicas:

3

---

## High Load

Event Rate:

20-29

Decision:

SCALE

Replicas:

4

---

## Extreme Load

Event Rate:

30+

Decision:

SCALE

Replicas:

5

---

# Observations

KEDA scaling remained stable.

No scaling storms observed.

Cooldown protection prevented rapid oscillations.

Average scale-up time:

15-30 seconds.

Average scale-down time:

60 seconds.