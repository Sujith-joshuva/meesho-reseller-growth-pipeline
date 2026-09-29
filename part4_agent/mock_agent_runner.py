import csv
import json

from part2_engine.growth_engine import validate_feed, mom_growth, is_flagged


def load_month(csv_path, month):
    data = {}

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["month"] == month:
                data[row["category"]] = float(row["revenue"])

    return data


def draft_message(category, previous_revenue, current_revenue,
                  mom_pct, month, prev_month):
    return (
        f"Context: {category} revenue changed from "
        f"{previous_revenue} in {prev_month} to "
        f"{current_revenue} in {month}.\n"
        f"Insight: Fact: {category} revenue changed by "
        f"{mom_pct}% from {prev_month} to {month}.\n"
        f"Implication: The regional manager should review "
        f"{category} performance and investigate the relevant "
        f"business drivers before deciding on corrective action."
    )


def run(month: str, previous_month_csv: str, current_month_csv: str) -> dict:
    previous_valid, previous_errors = validate_feed(previous_month_csv)
    current_valid, current_errors = validate_feed(current_month_csv)

    if not previous_valid or not current_valid:
        return {
            "run_month": month,
            "validation_status": "invalid",
            "validation_errors": previous_errors + current_errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop",
        }

    previous_month = "April" if month == "May" else "May"

    previous = load_month(previous_month_csv, previous_month)
    current = load_month(current_month_csv, month)

    flagged = []
    escalated = []

    for category in current:
        previous_revenue = previous[category]
        current_revenue = current[category]

        mom_pct = mom_growth(previous_revenue, current_revenue)
        status = is_flagged(mom_pct)

        if status == "flagged":
            flagged.append({
                "category": category,
                "mom_pct": mom_pct,
                "previous_revenue": previous_revenue,
                "current_revenue": current_revenue,
            })

        elif status == "escalate_exact_boundary":
            escalated.append(category)

    flagged.sort(key=lambda item: abs(item["mom_pct"]), reverse=True)

    drafted = []

    for item in flagged[:3]:
        item["drafted"] = True
        item["message"] = draft_message(
            item["category"],
            item["previous_revenue"],
            item["current_revenue"],
            item["mom_pct"],
            month,
            previous_month,
        )
        drafted.append(item)

    suppressed = [
        item["category"]
        for item in flagged[3:]
    ]

    return {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": drafted,
        "suppressed_categories": suppressed,
        "escalated_categories": escalated,
        "action_taken": "drafted_and_held_for_approval",
    }


if __name__ == "__main__":
    result = run(
        "May",
        "part1_sql/output/monthly_category_revenue.csv",
        "part1_sql/output/monthly_category_revenue.csv",
    )

    print(json.dumps(result, indent=2))