# Sliding Window

Window:

60 seconds

---

Flow

Incoming Events

↓

Append to event_buffer

↓

Remove expired events

↓

Keep recent events only

↓

Calculate load

↓

Generate prediction

---

Example

0 sec

5 events

↓

20 sec

8 events

↓

60 sec

Old events removed

↓

Current active events

7

---

Benefits

- near real-time analysis
- smooth scaling
- anomaly detection