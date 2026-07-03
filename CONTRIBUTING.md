# Contributing

FrontDeskAgent playbooks should be practical, machine-readable, and safe for real businesses to adapt.

Good contributions include:

- new industry playbooks;
- better required fields;
- clearer urgency rules;
- safer handoff summaries;
- better SMS/email templates;
- schema improvements;
- examples for OpenZero, FrontDeskAgent, Ollama, llama.cpp, n8n, Zapier, or Make.

## Rules

- Do not include real customer data.
- Do not include real phone numbers, private emails, or API keys.
- Do not promise legal, medical, or emergency outcomes.
- Keep playbooks adaptable across regions.
- Validate before submitting:

```bash
python tools/validate_playbooks.py
```

## Pull Requests

Include:

- what industry/workflow the playbook supports;
- why the fields matter;
- how urgency is handled;
- how it was validated.

