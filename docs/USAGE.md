# Usage Guide

These playbooks are designed to be readable by both humans and agents.

## FrontDeskAgent

1. Open the self-hosted FrontDeskAgent dashboard.
2. Go to the knowledge page.
3. Add the relevant playbook sections as business rules.
4. Test the flow in the playground before connecting calls or forms.

For local AI, keep the playbook short enough for the model context. Use the required fields and urgency rules first, then add SMS templates and industry notes.

## OpenZero

Use a playbook as routing context for a local OpenZero workflow:

- Read the JSON playbook.
- Map `required_fields` to the fields your agent must collect.
- Map `urgency_rules` to escalation or human handoff.
- Map `handoff_summary` to the final staff note.

## Local Models

Small CPU models work better when the task is structured. Put the playbook rules before the customer message and ask for one action at a time:

```text
Follow this intake playbook. Ask only the next missing question. If an urgency rule matches, collect safe details and hand off.
```

## Safety Notes

These playbooks do not replace professional judgement. Medical, legal, financial, emergency, or safety-critical calls should be routed to an appropriate human or official service according to the organisation's own policy.
