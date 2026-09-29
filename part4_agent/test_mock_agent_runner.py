import json

from part4_agent.mock_agent_runner import run


DATA = "part1_sql/output/monthly_category_revenue.csv"
CORRUPTED = "part2_engine/fixtures/corrupted_feed.csv"


def test_may_scenario():
    result = run("May", DATA, DATA)

    assert result["validation_status"] == "valid"

    flagged = result["flagged_categories"]

    assert [item["category"] for item in flagged] == [
        "Ethnic Wear",
        "Western Wear",
        "Kids Wear",
    ]

    assert [item["mom_pct"] for item in flagged] == [
        77.1,
        -23.6,
        -23.48,
    ]

    assert all(item["drafted"] is True for item in flagged)

    assert set(result["suppressed_categories"]) == {
        "Beauty & Personal Care",
        "Home & Kitchen",
    }

    assert result["escalated_categories"] == []


def test_june_scenario():
    result = run("June", DATA, DATA)

    assert result["validation_status"] == "valid"

    flagged = result["flagged_categories"]

    assert [item["category"] for item in flagged] == [
        "Ethnic Wear",
        "Home & Kitchen",
        "Kids Wear",
    ]

    assert [item["mom_pct"] for item in flagged] == [
        -58.74,
        42.59,
        23.9,
    ]

    assert all(item["drafted"] is True for item in flagged)

    assert result["suppressed_categories"] == ["Western Wear"]

    assert result["escalated_categories"] == []

    assert "Beauty & Personal Care" not in [
        item["category"] for item in flagged
    ]

    assert "Beauty & Personal Care" not in result["suppressed_categories"]


def test_corrupted_feed_hard_stop():
    result = run("July", DATA, CORRUPTED)

    assert result["validation_status"] == "invalid"
    assert result["action_taken"] == "hard_stop"

    assert result["validation_errors"] == [
        "line 3: negative revenue (-4200.0) for category=Western Wear",
        "line 4: missing category (month=July)",
        "line 6: missing revenue (category=Home & Kitchen)",
    ]

    assert result["flagged_categories"] == []
    assert result["suppressed_categories"] == []
    assert result["escalated_categories"] == []


def test_drafted_messages_contain_exact_values():
    result = run("May", DATA, DATA)

    for item in result["flagged_categories"]:
        message = item["message"]

        assert item["category"] in message
        assert str(item["mom_pct"]) + "%" in message