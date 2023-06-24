import pytest
import products

def test_create_product():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_invalid_product():
    with pytest.raises(ValueError):
        products.Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        products.Product("MacBook Air M2", price=-1450, quantity=100)  # Negative price


def test_zero_quantity():
    product = products.Product("MacBook Air M2", price=1450, quantity=0)
    assert not product.is_active()


def test_product_purchase():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert total_price == 14500
    assert product.quantity == 90


def test_invalid_quantity_purchase():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(-10)  # Invalid negative quantity
    with pytest.raises(Exception):
        product.buy(110)  # Quantity larger than available

