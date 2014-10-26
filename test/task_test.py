from nose import tools
from model.task import *


def test_snail_equality():
    snail1 = SnailTask('omanyte')
    snail2 = SnailTask('omanyte')
    tools.eq_(snail1, snail2)


def test_quail_equality():
    quail1 = QuailTask('chiquail')
    quail2 = QuailTask('chiquail')
    tools.eq_(quail1, quail2)


def test_identify_snail():
    snail = SnailTask('omanyte')
    tools.ok_(snail.is_snail())


def test_quail_is_not_snail():
    quail = QuailTask('chiquail')
    tools.ok_(not quail.is_snail())
