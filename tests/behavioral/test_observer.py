from src.behavioral.observer import (
    Stock,
    MobileAppObserver,
    EmailAlertObserver,
    DashboardObserver,
)


def test_observers_are_notified_on_price_change():
    stock = Stock("AAPL", 150.0)
    mobile = MobileAppObserver("john")
    email = EmailAlertObserver("john@mail.com")

    stock.subscribe(mobile)
    stock.subscribe(email)

    stock.price = 155.0  # triggers notification

    assert "AAPL is now $155.0" in mobile.last_message
    assert "AAPL changed to $155.0" in email.last_message


def test_unsubscribe_stops_notifications():
    stock = Stock("TSLA", 700.0)
    mobile = MobileAppObserver("jane")

    stock.subscribe(mobile)
    stock.price = 710.0
    assert "710.0" in mobile.last_message

    stock.unsubscribe(mobile)
    stock.price = 720.0  # should NOT reach mobile
    assert "720.0" not in mobile.last_message


def test_dashboard_accumulates_history():
    stock = Stock("GOOG", 100.0)
    dashboard = DashboardObserver()
    stock.subscribe(dashboard)

    stock.price = 101.0
    stock.price = 102.0

    assert dashboard.history == ["GOOG=$101.0", "GOOG=$102.0"]


def test_duplicate_subscription_is_ignored():
    stock = Stock("MSFT", 300.0)
    dashboard = DashboardObserver()

    stock.subscribe(dashboard)
    stock.subscribe(dashboard)  # duplicate

    stock.price = 305.0
    assert len(dashboard.history) == 1  # notified only once