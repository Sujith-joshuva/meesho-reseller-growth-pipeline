# Narrative Report

## Worked Narrative 1 — Ethnic Wear: May vs April

### Context

Ethnic Wear revenue increased from April to May. The comparison is May versus April.

### Insight

**Fact:** Ethnic Wear revenue increased by **77.1%** from April to May.

### Implication

The regional manager should compare Ethnic Wear performance by region and review reseller-level activity to identify where the May increase occurred before deciding whether to sustain the change.

**Hypothesis:** The increase may be associated with changes in regional demand or reseller activity, but the supplied data does not establish a specific cause.

### Self-score

- **Specificity — PASS:** The narrative identifies the exact category, comparison period, and verified growth percentage.
- **Audience fit — PASS:** The explanation is written for a regional manager rather than a technical audience.
- **Completeness — PASS:** It includes context, a fact-based insight, and an implication with a clearly labeled hypothesis.
- **Actionability — PASS:** It directs the manager to compare regional performance and review reseller-level activity as concrete next steps.

---

## Worked Narrative 2 — Ethnic Wear: June vs May

### Context

Ethnic Wear revenue decreased from May to June. The comparison is June versus May.

### Insight

**Fact:** Ethnic Wear revenue decreased by **58.74%** from May to June.

### Implication

The regional manager should compare Ethnic Wear performance by region and review reseller-level activity for May versus June to identify where the decline occurred before deciding on corrective action.

**Hypothesis:** The decline may be associated with changes in regional demand or reseller activity, but the supplied data does not establish a specific cause.

### Self-score

- **Specificity — PASS:** The narrative identifies the exact category, comparison period, and verified growth percentage.
- **Audience fit — PASS:** The explanation is written for a regional manager rather than a technical audience.
- **Completeness — PASS:** It includes context, a fact-based insight, and an implication with a clearly labeled hypothesis.
- **Actionability — PASS:** It directs the manager to compare regional performance and review reseller-level activity as concrete next steps.

---

# Chart-Choice Justification

## 1. Monthly total revenue

### Verified values

- April: 419417.43
- May: 444594.25
- June: 398055.24

### Chart choice

**Column chart**

This is a univariate comparison of total revenue across three months. A column chart makes the comparison of monthly totals easy to understand within 10 seconds.

The y-axis should start at zero to avoid exaggerating differences. A 3D chart should not be used because it can distort visual comparison. No legend is required because there is only one series.

---

## 2. Ethnic Wear share of April total revenue

### Verified calculation

Ethnic Wear April revenue = 104520.77

April total revenue = 419417.43

Ethnic Wear share of April total revenue:

`104520.77 / 419417.43 × 100 = 24.92%`

### Chart choice

**Donut chart**

This is a univariate part-to-whole view of April revenue, where Ethnic Wear is compared with the remainder of April revenue.

The chart should clearly show the 24.92% share. A simple design should be used so the part-to-whole relationship is understandable within 10 seconds. A 3D chart should not be used.

---

## 3. Revenue by region

### Verified values

- North: 337125.46
- West: 333106.33
- South: 316736.68
- East: 275098.45

### Chart choice

**Bar chart**

This is a univariate comparison of revenue across regions. A horizontal bar chart allows the four regional values to be compared directly and clearly.

The x-axis should start at zero to avoid exaggerating differences. A 3D chart should not be used. No legend is required because there is only one series.

---

## Top-Reseller Masked Narrative

The Part 1 `HAVING` query identified five resellers with total spend above INR 50,000.

- **West — ALIAS-19:** INR 75,295.09 in total spend.
- **West — ALIAS-22:** INR 73,882.33 in total spend.
- **South — ALIAS-12:** INR 69,936.46 in total spend.
- **North — ALIAS-06:** INR 64,238.97 in total spend.
- **North — ALIAS-05:** INR 61,825.02 in total spend.

These references use the reseller's region and coded alias only. Raw reseller names are intentionally excluded from the external-facing narrative.
