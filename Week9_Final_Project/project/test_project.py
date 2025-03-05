import pytest
from datetime import datetime, timedelta
from project import ValetParking

@pytest.fixture
def valet_parking():
    return ValetParking()

def test_calculate_payment(valet_parking):
    entry_time = datetime.now() - timedelta(hours=2)
    exit_time = datetime.now()
    payment_due, duration = valet_parking.calculate_payment(entry_time, exit_time)

    assert duration.total_seconds() == pytest.approx(7200, rel=1e-6)  # Usando una tolerancia relativa
    assert payment_due == pytest.approx(20, rel=1e-6)  # Igualmente para el pago

def test_validate_payment_exact(valet_parking):
    status, difference = valet_parking.validate_payment(10, 10)
    assert status == "Exacto"
    assert difference == 0

def test_validate_payment_falta(valet_parking):
    status, difference = valet_parking.validate_payment(5, 10)
    assert status == "Falta"
    assert difference == 5

def test_validate_payment_sobra(valet_parking):
    status, difference = valet_parking.validate_payment(20, 10)
    assert status == "Sobra"
    assert difference == 10
