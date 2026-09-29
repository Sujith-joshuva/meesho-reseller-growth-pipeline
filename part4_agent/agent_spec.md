# Agent Specification

## Goal

Keep Meesho category managers informed of category month-on-month revenue movements beyond the 8% threshold, with every drafted message held for human approval before it is considered sent.

## Tools

The monitoring agent uses these existing project functions:

- `validate_feed` — validates the monthly revenue feed before any further processing.
- `mom_growth` — calculates month-on-month revenue growth.
- `is_flagged` — classifies each MoM percentage as `flagged`, `not_flagged`, or `escalate_exact_boundary`.
- Part 3 prompt-pack template-fill logic — creates a stakeholder draft from verified category and MoM values.

The Part 2 functions are imported and used without modification.

## Memory / State

Between runs, the agent needs the previous month's revenue for each category so that the next run can calculate month-on-month growth.

The current month's revenue feed becomes the reference for a subsequent month's comparison.

## Planner

The agent follows these ordered subtasks:

1. Load the monthly revenue feed and run `validate_feed`.
2. If the feed is invalid, Hard Stop and report the validation errors.
3. If the feed is valid, compute `mom_growth` for every category against the previous month.
4. Run `is_flagged` on every category.
5. Sort flagged categories by `abs(mom_pct)` in descending order.
6. Draft a message using the Part 3 template for at most the top 3 flagged categories by magnitude.
7. Log any remaining flagged categories beyond the top-3 cap as `suppressed, review manually` without drafting a message.
7b. Separately log categories whose result is `escalate_exact_boundary` into `escalated_categories` without drafting a message.
8. Emit one structured JSON object for the run.

## Feedback Loop

Every drafted message is held for human approval.

The mock runner does not send email or call any messaging service. A drafted message is represented as held for approval in the structured output.

## Guardrails

### Input Guardrail

`validate_feed` must pass before any MoM calculation, flag classification, drafting, or other processing occurs.

If validation fails, the run must Hard Stop and surface the validation errors.

### Action Guardrail

No message is ever automatically sent.

Messages are only drafted and held for human approval. No Gmail, SMTP, API, or other network integration is used.

### Output Guardrail

Every number in a drafted message must trace back to a verified Part 1 or Part 2 value.

The agent must not invent figures, metrics, causes, or other numerical information.

## Success and Error Stopping Conditions

### Success

A run succeeds when:

- the feed passes validation,
- the required MoM calculations and classifications are completed,
- flagged categories are sorted by absolute MoM percentage,
- no more than the top 3 flagged categories are drafted,
- additional flagged categories are suppressed,
- exact-boundary categories are separately escalated,
- and every number in each drafted message is traceable to a Part 1 or Part 2 value.

If no category crosses the threshold, the run may correctly produce zero drafted messages.

### Error

If `validate_feed` returns `False`, the run is a **Hard Stop**.

The validation errors must be surfaced in `validation_errors`. No MoM computation or message drafting is attempted.

## Given-When-Then Agent Specifications

### 1. April to May — Ethnic Wear

**Given** the April and May validated monthly category revenue feeds,  
**When** the agent computes MoM growth for Ethnic Wear,  
**Then** the agent records `77.1%` and classifies the category as `flagged`.

### 2. May to June — Beauty & Personal Care

**Given** the May and June validated monthly category revenue feeds,  
**When** the agent computes MoM growth for Beauty & Personal Care,  
**Then** the agent records `5.67%` and classifies the category as `not_flagged`.

### 3. Exact 8% boundary

**Given** a category with previous revenue `100000` and current revenue `108000`,  
**When** the agent computes MoM growth and applies `is_flagged`,  
**Then** the agent records `8.0%` and classifies the category as `escalate_exact_boundary`.

### 4. Corrupted feed

**Given** the corrupted monthly revenue feed,  
**When** the agent runs `validate_feed`,  
**Then** the agent Hard Stops, surfaces the three validation errors, and does not attempt MoM computation or message drafting.