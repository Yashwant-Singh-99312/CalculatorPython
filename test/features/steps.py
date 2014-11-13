# -*- coding: utf-8 -*-
from lettuce import step, world
import sys
sys.path.append("../app")
from Calculator import Calculator


@step(u'Dado los números "([^"]*)" y "([^"]*)"')
def dado_los_numeros_group1_y_group1(step, num1, num2):
    world.cal = Calculator()
    world.num1 = num1
    world.num2 = num2


@step(u'Cuando los sumamos')
def cuando_los_sumamos(step):
    world.result = world.cal.suma(int(world.num1), int(world.num2))


@step(u'Cuando los restamos')
def cuando_los_restamos(step):
    world.result = world.cal.resta(int(world.num1), int(world.num2))


@step(u'Cuando los multiplicamos')
def cuando_los_multiplicamos(step):
    world.result = world.cal.multiplicar(int(world.num1), int(world.num2))


@step(u'Cuando los dividimos')
def cuando_los_dividimos(step):
    world.result = world.cal.dividir(int(world.num1), int(world.num2))


@step(u'Entonces el resultado es "([^"]*)"')
def entonces_el_resultado_es_group1(step, resEsperado):
    assert world.result == int(
        resEsperado), 'El resultado es %s y el esperado es %s' % (world.result, resEsperado)
