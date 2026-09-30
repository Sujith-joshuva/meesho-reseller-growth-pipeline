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