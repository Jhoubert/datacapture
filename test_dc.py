from datacapture import DataCapture
import random
import pytest


@pytest.fixture
def sample_data():
    capture = DataCapture()

    # Creating entries less than 100
    for _ in range(91242):
        n = random.randint(0, 99)
        capture.add(n)

    # Creating entries between 150 and 400
    for _ in range(42294):
        n = random.randint(151, 400)
        capture.add(n)

    # Creating entries greater than 421
    for _ in range(21254):
        n = random.randint(421, 1000)
        capture.add(n)

    stats = capture.build_stats()

    return stats


def test_big_ammount(sample_data):
    assert sample_data.less(100) == 91242
    assert sample_data.between(149, 401) == 42294
    assert sample_data.greater(402) == 21254


def test_basic_on_fly():
    capture = DataCapture()
    capture.build_on_fly(True)
    capture.add(21)

    statsa = capture.build_stats()

    assert statsa.between(21, 21) == 1
    assert statsa.greater(21) == 0
    assert statsa.less(21) == 0


def test_basic_on_fly_mix():
    capture = DataCapture()
    capture.build_on_fly(True)
    capture.add(21)
    capture.build_on_fly(False)
    capture.add(21)
    statsa = capture.build_stats()

    assert statsa.between(21, 21) == 2
    assert statsa.greater(21) == 0
    assert statsa.less(21) == 0
