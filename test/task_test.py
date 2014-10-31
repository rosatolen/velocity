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
