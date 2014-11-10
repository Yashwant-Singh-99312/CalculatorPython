# -*- coding: utf-8 -*-
from lettuce import step, world
import sys
sys.path.append("../app")
from Calculator import Calculator


@step(u'Dado los números "([^"]*)" y "([^"]*)"')
def dado_los_numeros_group1_y_group1(step, num1, num2):
    cal = Calculator()
    world.result = cal.suma(int(num1), int(num2))


@step(u'Cuando los sumamos')
def cuando_los_sumamos(step):
    pass


@step(u'Entonces el resultado es "([^"]*)"')
def entonces_el_resultado_es_group1(step, resEsperado):
    assert world.result == int(
        resEsperado), 'El resultado es %s y el esperado es %s' % (world.result, resEsperado)
