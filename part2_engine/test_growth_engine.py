from part2_engine.growth_engine import (
    mom_growth,
    is_flagged,
    validate_feed,
)


def test_april_to_may_ethnic_wear():
    # GIVEN April -> May Ethnic Wear revenue
    previous = 104520.77
    current = 185107.61

    # WHEN MoM growth and flagging are calculated
    mom_pct = mom_growth(previous, current)
    result = is_flagged(mom_pct)

    # THEN
    assert mom_pct == 77.1
    assert result == "flagged"


def test_may_to_june_beauty_personal_care():
    # GIVEN May -> June Beauty & Personal Care revenue
    previous = 35542.11
    current = 37559.07

    # WHEN MoM growth and flagging are calculated
    mom_pct = mom_growth(previous, current)
    result = is_flagged(mom_pct)

    # THEN
    assert mom_pct == 5.67
    assert result == "not_flagged"


def test_exact_threshold_boundary():
    # GIVEN a synthetic 8% growth case
    previous = 100000
    current = 108000

    # WHEN MoM growth and flagging are calculated
    mom_pct = mom_growth(previous, current)
    result = is_flagged(mom_pct)

    # THEN
    assert mom_pct == 8.0
    assert result == "escalate_exact_boundary"


def test_corrupted_feed():
    # GIVEN the required corrupted feed fixture
    fixture = "part2_engine/fixtures/corrupted_feed.csv"

    # WHEN validation runs
    is_valid, errors = validate_feed(fixture)

    # THEN
    expected_errors = [
        "line 3: negative revenue (-4200.0) for category=Western Wear",
        "line 4: missing category (month=July)",
        "line 6: missing revenue (category=Home & Kitchen)",
    ]

    assert is_valid is False
    assert len(errors) == 3
    assert errors == expected_errors