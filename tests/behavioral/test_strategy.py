from src.behavioral.strategy import (
    CheckoutService,
    CreditCardPayment,
    PayPalPayment,
    CryptoPayment,
)


def test_pay_with_credit_card():
    checkout = CheckoutService(CreditCardPayment("1234567812345678"))
    result = checkout.checkout(100)
    assert "Credit Card ****5678" in result


def test_pay_with_paypal():
    checkout = CheckoutService(PayPalPayment("user@mail.com"))
    assert "PayPal" in checkout.checkout(50)

def test_pay_with_crypto():
    checkout = CheckoutService(CryptoPayment("0xABCDEF123456"))
    assert "Crypto" in checkout.checkout(75)

def test_switch_strategy_at_runtime():
    checkout = CheckoutService(PayPalPayment("user@mail.com"))
    assert "PayPal" in checkout.checkout(50)

    checkout.set_strategy(CryptoPayment("0xABCDEF123456"))
    assert "Crypto" in checkout.checkout(75)