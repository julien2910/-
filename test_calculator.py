import pytest
from calculator import calculate_commission

class TestCalculateCommission:
    @pytest.mark.parametrize("amount, expected", [
        (100, 50.0),
        (1000, 50.0),
        (1001, 150.0),
        (20000, 150.0),
        (20001, 400.01),
        (50000, 700.0),
    ])
    def test_commission_calculation(self, amount, expected):
        assert calculate_commission(amount) == expected

    @pytest.mark.parametrize("invalid_amount", [99, 50001, -1])
    def test_commission_invalid_amount_raises_error(self, invalid_amount):
        with pytest.raises(ValueError):
            calculate_commission(invalid_amount)

    def test_non_numeric_raises_type_error(self):
        with pytest.raises(TypeError):
            calculate_commission("abc")
