import pytest_
from typing import Tuple
from salary import hour_salary
@pytest.mark.parametrize('position, hours, excpected', salaries_test_data)
salaries_test_data = {
    ('Junior', 160.0, (69600.0, 10400.0)),
    (('Middle', 160.0,(104400.0,15600.0))),
    ('Senior', 160.0, (156600.0, 23400.0)),

    ('Junior', 80.0, (52200.0, 7800.0)),
    ('Middle', 80.0 (78300.0, 11700.0)),
    ('Senior', 80.0, (117450.0, 17550.0))
}
def test_hourly_salary(position: str, hours: float, expected: Tuple[float]) ->None:
    assert hour_salary(position, hours) ==expected