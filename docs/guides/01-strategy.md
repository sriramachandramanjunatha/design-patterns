# 01 — Strategy Pattern

## 🎯 Problem
E-commerce checkout must support many payment methods (Card, PayPal, Crypto)
that grow over time. Using `if/else` violates the **Open/Closed Principle**.

## ✅ Solution
Encapsulate each algorithm behind a common interface; swap at runtime.

## 🐍 Pythonic Notes (vs Java/Node)
| Aspect | Java | Python |
|--------|------|--------|
| Interface | `interface PaymentStrategy` | `ABC` or `Protocol` |
| Implements | `implements` keyword | inherit from ABC |
| Duck typing | Not available | ✅ Any object with `.pay()` works |

> **Pythonic shortcut:** You can even skip the ABC and pass any callable —
> Python's duck typing makes Strategy almost trivial. But ABC gives clarity.

## When to Use
- Multiple interchangeable algorithms chosen at runtime
- Avoid large conditional blocks
- Isolated, testable algorithms

## When NOT to Use
- Only 1–2 stable variations (overkill)

## Real-World Examples
- Payment gateways
- Compression (zip/gzip)
- Auth strategies (OAuth/SAML/JWT)

## Interview Q&A
**Q: Strategy vs State?**
A: Same structure, different intent. Strategy = client picks algorithm.
State = object changes its own behavior internally.

**Q: How is this different in Python vs Java?**
A: Python's duck typing means you don't strictly need an interface —
any object with the right method works. ABC is used for explicit contracts.

## Run
```bash
uv run pytest tests/behavioral/test_strategy.py -v
```