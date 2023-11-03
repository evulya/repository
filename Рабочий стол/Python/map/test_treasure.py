test_data = (
    (
        {['x', 0],
         [0, 't'],},
         [0]

    )
)

import pytest
test_data = ()
@pytest.mark.parametrize()
def test_get_path(map: list, expected: dict) -> None:
    path = get_path(map)
    valid_path = True
    for key, value in expected.items():
        if way.count(key) != value:
            valid_path = False
            break
