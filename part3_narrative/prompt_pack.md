# Reusable Prompt Pack

## Trigger

Start this prompt when a category's `is_flagged` result is `"flagged"`.

## Input list

The prompt requires these supplied placeholder variables:

- `{category}` — flagged category name
- `{previous_revenue}` — revenue in the previous month
- `{current_revenue}` — revenue in the current month
- `{mom_pct}` — verified Month-on-Month growth percentage
- `{month}` — current month
- `{prev_month}` — previous month

## Prompt

Write a concise stakeholder update for a regional manager about the flagged category.

Use this structure:

### Context
State what `{category}` measures and explicitly identify the comparison as `{month}` versus `{prev_month}`.

### Insight
State the verified `{mom_pct}` as a **fact**. Use only the supplied values `{previous_revenue}`, `{current_revenue}`, and `{mom_pct}` when mentioning numbers.

### Implication
Give a specific and actionable next step for the regional manager. If a possible cause is suggested but is not proven by the supplied data, label it explicitly as a **hypothesis** rather than a fact.

Rules:

- Do not invent facts, causes, explanations, or numbers.
- Do not state any number that is not one of the supplied placeholder values.
- Do not calculate or introduce additional metrics unless they are explicitly supplied.
- Keep the distinction between **fact** and **hypothesis** explicit.
- Write for a regional manager, not a data engineer.
- Make the recommendation specific and actionable.
- Do not expose raw reseller names. Use only approved coded aliases when a reseller is supplied.

## Checklist

Before the narrative is used, verify:

- [ ] Every number in the draft matches a supplied placeholder value exactly.
- [ ] The comparison names `{month}` and `{prev_month}` correctly.
- [ ] The verified `{mom_pct}` is stated as a **fact**.
- [ ] Any proposed cause that is not proven by the supplied data is labeled as a **hypothesis**.
- [ ] The recommendation identifies a specific and actionable next step rather than a vague suggestion.
- [ ] The narrative is written for a regional manager and is understandable without technical implementation details.
- [ ] No raw reseller name appears in the narrative; approved coded aliases are used where applicable.