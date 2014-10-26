from nose.tools import *
from model.task import *


def test_equality():
    snail1 = SnailTask('omanyte')
    snail2 = SnailTask('omanyte')
    eq_(snail1, snail2)


def test_identify_snail():
    snail = SnailTask('omanyte')
    ok_(snail.is_snail())


def test_quail_is_not_snail():
    quail = QuailTask('chiquail')
    ok_(not quail.is_snail())
