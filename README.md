# Meesho Reseller Growth Monitoring Pipeline

SQL, Python, and agentic workflow for reseller growth monitoring.

## Project Overview

This project implements an integrated reseller growth-monitoring pipeline using SQL, Python guardrails, reliable narrative generation, and a mock agent workflow.

The pipeline follows this order:

**Dataset → SQL Business Queries → Python Guardrails & Growth Detection → Narrative Drafting → Agentic Monitoring Workflow**

## Repository Structure

```text
data/
├── generate_dataset.py
├── resellers.csv
├── orders.csv
└── meesho_reseller.db

part1_sql/
├── queries.sql
└── output/
    ├── monthly_category_revenue.csv
    ├── region_revenue.csv
    ├── top_resellers.csv
    ├── zero_order_resellers.csv
    └── june_delivered_aov.csv

part2_engine/
├── growth_engine.py
├── test_growth_engine.py
└── fixtures/
    └── corrupted_feed.csv

part3_narrative/
├── prompt_pack.md
├── narrative_report.md
├── masking.py
├── test_masking.py
└── top_reseller_narrative.md

part4_agent/
├── agent_spec.md
├── mock_agent_runner.py
└── test_mock_agent_runner.py
```

## Requirements

- Python 3
- SQLite
- pytest

No API key is required.

## How to Run the Pipeline

Run the Parts in the following order.

### Step 1 — Regenerate the Dataset

Run:

```bash
python data/generate_dataset.py
```

This regenerates:

```text
data/resellers.csv
data/orders.csv
data/meesho_reseller.db
```

The dataset generator uses the fixed seed defined in the script.

### Step 2 — Part 1: SQL Business Query Engine

Run the SQL business queries:

```bash
sqlite3 data/meesho_reseller.db < part1_sql/queries.sql
```

The verified Part 1 output files are stored in:

```text
part1_sql/output/
```

Part 1 computes the verified business numbers that are handed off to the later stages.

### Step 3 — Part 2: Python Guardrail & Growth Detection Engine

Run the Part 2 tests:

```bash
pytest part2_engine/test_growth_engine.py
```

Part 2 validates the revenue feed, calculates Month-on-Month growth, and classifies growth movements using the required threshold and boundary handling.

### Step 4 — Part 3: Reliable AI Narrative & Prompt Pack

Run the Part 3 tests:

```bash
pytest part3_narrative/test_masking.py
```

Part 3 provides the reusable narrative prompt pack, worked stakeholder narratives, chart-choice justification, and reseller-name masking.

### Step 5 — Part 4: Agentic Workflow + Mock Agent Runner

Run the Part 4 tests:

```bash
pytest part4_agent/test_mock_agent_runner.py
```

The mock agent runner can also be executed directly:

```bash
python -m part4_agent.mock_agent_runner
```

Part 4 connects the earlier components into a guarded monitoring workflow.

### Step 6 — Run the Complete Test Suite

Run:

```bash
pytest
```

The complete test suite verifies the Python components across Parts 2, 3, and 4.

## Zero API Key Requirement

The complete pipeline runs with **zero API keys set**.

The project does not require:

- API keys
- Network calls
- Gmail integration
- SMTP integration
- External AI services

Part 4 is a mock agent runner. It creates message drafts and holds them for human approval; it does not automatically send messages.

## Workflow Pattern Mapping

### Part 1 → Part 2

Part 1 computes the real business numbers using SQL first. Part 2 validates those verified outputs and performs guarded growth calculations.

**Workflow pattern: Compute → Hand Off**

This mirrors the **"compute real numbers via SQL first, then hand off"** order of operations.

### Part 2 → Part 3

Part 2 detects verified growth movements and applies the required guardrails. Part 3 uses those verified values as controlled inputs for stakeholder narratives.

**Workflow pattern: Detect → Explain**

### Part 3 → Part 4

Part 3 provides the reusable narrative prompt and masking rules. Part 4 incorporates these into the guarded monitoring workflow.

**Workflow pattern: Draft → Validate → Human Approval**

### Part 4

Part 4 combines the earlier components into an agentic workflow:

**Intake → Validate → Compute → Classify → Prioritize → Report Draft → Suppress/Escalate → Human Approval**

The workflow includes an input validation guardrail, an action guardrail that prevents automatic sending, and an output guardrail requiring drafted numbers to trace back to verified Part 1 or Part 2 values.

## Documentation References

The implementation references the official Python standard-library documentation for:

- Python `csv` module: https://docs.python.org/3/library/csv.html
- Python `json` module: https://docs.python.org/3/library/json.html