# Playbook Design Guide

A good front desk playbook should help an AI receptionist ask the right questions without becoming rigid or unsafe.

## Core Sections

Every playbook should define:

- purpose;
- business type;
- required fields;
- optional fields;
- follow-up questions;
- urgency rules;
- handoff summary;
- SMS or email templates;
- escalation conditions.

## Required Fields

Required fields should be the minimum needed for a staff member to act.

Common fields:

- name;
- contact method;
- location or service area;
- issue/request;
- urgency;
- preferred time;
- consent or callback permission where needed.

## Urgency Rules

Urgency rules should be practical and conservative.

Good:

- "burst pipe" -> urgent callback;
- "chest pain" -> advise emergency services and hand off;
- "hotel guest locked out" -> immediate staff alert.

Avoid:

- diagnosing;
- promising availability;
- making legal or medical decisions;
- telling the user the problem is solved before staff review.

## Handoff Summary

The handoff summary should be short and useful:

```text
Name:
Contact:
Need:
Urgency:
Location:
Preferred time:
Missing details:
Recommended staff action:
```

## Local Agent Use

For local agents, give the model structure, not a wall of text. The playbook should be easy to parse and easy to validate.

