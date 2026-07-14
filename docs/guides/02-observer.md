# 02 — Observer Pattern

## 🎯 Problem
A stock platform must notify many subscribers (mobile, email, dashboard)
instantly when a price changes. Subscribers join/leave dynamically.
Hard-coding each notification creates tight coupling.

## ✅ Solution
Define a one-to-many dependency: when the **Subject** changes state,
all registered **Observers** are notified automatically.

## 🐍 Pythonic Notes (vs Java/Node)
| Aspect | Java | Node | Python |
|--------|------|------|--------|
| Built-in | `java.util.Observer` (deprecated) | `EventEmitter` | property setter + list |
| Interface | `interface Observer` | callback funcs | `ABC` or `Protocol` |
| Trigger | `notifyObservers()` | `.emit('event')` | property `setter` auto-fires |

> **Pythonic touch:** Using a `@price.setter` makes notification automatic —
> just assigning `stock.price = 155` fires all observers. Very clean.

> **Node parallel:** `EventEmitter` IS the Observer pattern. If you've used
> `emitter.on('event', cb)` — you already know Observer.

## When to Use
- One object's change must reflect in many others
- You don't know how many observers exist upfront
- Loose coupling between subject and subscribers (event-driven systems)

## When NOT to Use
- Simple 1-to-1 relationship (direct call is simpler)
- Risk of notification cascades / performance issues with many observers

## Real-World Examples
- Stock/price tickers
- Pub/Sub systems (Kafka, RabbitMQ conceptually)
- UI event listeners (button clicks)
- Reactive frameworks (RxJS, React state)
- Node.js `EventEmitter`

## Interview Q&A
**Q: Observer vs Pub/Sub?**
A: Observer = subject knows its observers directly (tightly linked).
Pub/Sub = decoupled via a message broker; publishers/subscribers don't
know each other.

**Q: Push vs Pull model?**
A: Push = subject sends data to observers (our example: sends price).
Pull = observer queries the subject for details after being notified.

**Q: How does Node relate?**
A: `EventEmitter` is a built-in Observer implementation.
`.on()` = subscribe, `.emit()` = notify.

## Run
```bash
uv run pytest tests/behavioral/test_observer.py -v
```