# Pressure Score

## Event Thresholds

LOW_PRESSURE_EVENTS = 5

MEDIUM_PRESSURE_EVENTS = 10

HIGH_PRESSURE_EVENTS = 15

---

## Risk Thresholds

MEDIUM_RISK_SCORE = 0.85

HIGH_RISK_SCORE = 0.95

---

## Score Calculation

Event pressure:

5 events

+1

10 events

+2

15 events

+3

---

Risk score:

0.85

+1

0.95

+2

---

## Final Decision

Pressure < 2

NORMAL

---

Pressure ≥ 2

ELEVATED

---

Pressure ≥ 4

SCALE