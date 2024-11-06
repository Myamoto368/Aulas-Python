import pytest
from calculo_imposto import calculo_imposto

def test_calculo_imposto():

    assert calculo_imposto(1000, 0.1) == 100
    assert calculo_imposto(2000, 0.15) == 300
    assert calculo_imposto(500, 0.05) == 25
    assert calculo_imposto(2500, 0.2) == 500
    assert calculo_imposto(0, 0.1) == 0
    assert calculo_imposto(10000, 0.3) == 3000
    assert calculo_imposto(1500, 0.1) == 150
    assert calculo_imposto(750, 0.2) == 150
    assert calculo_imposto(1800, 0.15) == 270
    assert calculo_imposto(3000, 0.25) == 750

def test_salario_negativo():
    with pytest.raises(ValueError):
        calculo_imposto(-1000, 0,1)

def test_aliquota_invalida():
    with pytest.raises(ValueError):
        calculo_imposto(1000, -0,1)
    with pytest.raises(ValueError):
        calculo_imposto(1000, 1.5)

def test_aliquota_zero():
    assert calculo_imposto(1000, 0) == 0