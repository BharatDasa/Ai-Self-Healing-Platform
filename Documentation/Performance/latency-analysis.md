# Latency Analysis

## Request Flow

Client

↓

Ingress

↓

Istio Gateway

↓

Envoy Sidecar

↓

Fraud Detection Service

↓

Kafka

↓

MongoDB

↓

Response

---

# Average Latency

API Response:

20 ms

Kafka Publish:

5 ms

MongoDB Write:

10 ms

Prometheus Scrape:

15 seconds

Grafana Refresh:

5 seconds

---

# Trace Analysis

Measured using:

- Tempo
- OpenTelemetry
- Grafana

---

# Bottlenecks

Potential latency sources:

- Kafka congestion
- Database writes
- Network delays
- High CPU utilization

---

# Recommendations

- Increase Kafka partitions
- Optimize indexes
- Horizontal scaling
- Enable caching