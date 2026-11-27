import csv
from pathlib import Path

import pytest

from qa_automation.pages.inventory import InventoryPage
from qa_automation.pages.login import LoginPage

DATA_FILE = Path(__file__).parents[2] / "data" / "login_cases.csv"
with DATA_FILE.open(encoding="utf-8", newline="") as file:
    LOGIN_CASES = list(csv.DictReader(file))


@pytest.mark.ui
@pytest.mark.parametrize(
    "case",
    LOGIN_CASES,
    ids=[f"{case['username'] or 'empty'}-{case['result']}" for case in LOGIN_CASES],
)
def test_login_scenarios(browser, case):
    login = LoginPage(browser).open()
    login.sign_in(case["username"], case["password"])

    if case["result"] == "ok":
        assert InventoryPage(browser).is_open()
    else:
        assert case["expected_error"] in login.error_message()
