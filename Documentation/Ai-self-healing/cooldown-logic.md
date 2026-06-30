# Cooldown Logic

Purpose:

Prevent scaling storms.

---

WINDOW_SECONDS = 60

COOLDOWN_SECONDS = 60

---

Flow

Action executed

↓

Cooldown starts

↓

Ignore repeated actions

↓

Cooldown expires

↓

AI resumes decisions

---

Benefits

- stability
- avoids flapping
- protects cluster