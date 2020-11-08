import pytest
import time
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook' : {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# the pupose of this test is to test the input funtion of the invoice
def testInput():
        unit_price = Invoice().inputNumber("Please enter unit price : ")
        while (unit_price is None):
            time.sleep(.5)
        assert type(unit_price) is float

#The purpose of this test is to test the add items function
def testAddProduct():
        invoice = Invoice()
        invoice.addProducts(2, 2, 2)
        assert invoice.items["qnt"] == 2
