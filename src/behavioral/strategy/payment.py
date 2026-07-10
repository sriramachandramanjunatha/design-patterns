"""
Strategy Pattern — Real-world: E-commerce payment methods.
"""
from abc import ABC, abstractmethod


# Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        ...


# --- Concrete Strategies ---
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str) -> None:
        self._card_number = card_number

    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Credit Card ****{self._card_number[-4:]}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str) -> None:
        self._email = email

    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using PayPal ({self._email})"


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet: str) -> None:
        self._wallet = wallet

    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Crypto wallet {self._wallet[:6]}..."


# --- Context ---
class CheckoutService:
    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """Swap payment method at runtime."""
        self._strategy = strategy

    def checkout(self, amount: float) -> str:
        return self._strategy.pay(amount)