"""
Observer Pattern — Real-world: Stock price notifications.

Java devs: think 'Listeners' (like ActionListener) or java.util.Observer.
Node devs: think EventEmitter — Observer is its conceptual foundation.

One Subject (Stock) notifies many Observers (subscribers) when state changes.
"""
from abc import ABC, abstractmethod


# --- Observer Interface ---
class Observer(ABC):
    @abstractmethod
    def update(self, symbol: str, price: float) -> None:
        ...


# --- Subject (Observable) ---
class Stock:
    def __init__(self, symbol: str, price: float) -> None:
        self._symbol = symbol
        self._price = price
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify(self) -> None:
        """Push new state to all subscribers."""
        for observer in self._observers:
            observer.update(self._symbol, self._price)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Setting a new price auto-notifies all observers."""
        self._price = new_price
        self._notify()


# --- Concrete Observers ---
class MobileAppObserver(Observer):
    def __init__(self, user: str) -> None:
        self._user = user
        self.last_message = ""

    def update(self, symbol: str, price: float) -> None:
        self.last_message = f"[Mobile:{self._user}] {symbol} is now ${price}"


class EmailAlertObserver(Observer):
    def __init__(self, email: str) -> None:
        self._email = email
        self.last_message = ""

    def update(self, symbol: str, price: float) -> None:
        self.last_message = f"[Email:{self._email}] {symbol} changed to ${price}"


class DashboardObserver(Observer):
    def __init__(self) -> None:
        self.history: list[str] = []

    def update(self, symbol: str, price: float) -> None:
        self.history.append(f"{symbol}=${price}")