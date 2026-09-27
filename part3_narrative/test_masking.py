from masking import alias_for, assert_no_raw_names_leak


def test_alias():
    assert alias_for("RS019") == "ALIAS-19"
    assert alias_for("RS006") == "ALIAS-06"


def test_no_raw_names_leak():
    names = [
        "Mumbai Reseller 1",
        "Mumbai Reseller 4",
        "Hyderabad Reseller 6",
        "Lucknow Reseller 6",
        "Jaipur Reseller 5",
    ]

    text = "West region, ALIAS-19, revenue increased."

    assert assert_no_raw_names_leak(text, names) is True


def test_raw_name_leak():
    names = ["Mumbai Reseller 1"]

    text = "Mumbai Reseller 1 had high revenue."

    assert assert_no_raw_names_leak(text, names) is False
    