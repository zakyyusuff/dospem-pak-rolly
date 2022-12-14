import pytest

from tests.app import dikalikan_dua, dibagi_dua


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = dikalikan_dua(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = dibagi_dua(numbers[1])
        assert res == numbers[0]
