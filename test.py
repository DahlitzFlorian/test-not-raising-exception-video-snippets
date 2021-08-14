from contextlib import nullcontext as does_not_raise

import math_ops
import pytest


@pytest.mark.parametrize(
    "divident, divisor, expectation",
    [
        (1, 3, does_not_raise()),
        (2, 1, does_not_raise()),
        (6, 2, does_not_raise()),
        (5, 0, pytest.raises(ZeroDivisionError)),
    ],
)
def test_division(divident, divisor, expectation):
    with expectation:
        assert (math_ops.division(divident, divisor)) is not None
