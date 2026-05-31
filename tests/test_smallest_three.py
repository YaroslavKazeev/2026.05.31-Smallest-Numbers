import pytest

from smallest_three import find_three_smallest_distinct_numbers, USE_CASES


def test_typical_case():
    case = USE_CASES[0]
    assert find_three_smallest_distinct_numbers(case["input"]) == case["expected"]


@pytest.mark.parametrize("idx", [1, 2])
def test_error_cases(idx):
    case = USE_CASES[idx]
    expected_message = case["expected_error"]
    with pytest.raises(Exception) as exc:
        find_three_smallest_distinct_numbers(case["input"])
    assert expected_message in str(exc.value)
