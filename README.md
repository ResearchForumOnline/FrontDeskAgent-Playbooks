# FrontDeskAgent Playbooks

Reusable open-source intake playbooks for AI receptionists, local agents, OpenZero workflows, and self-hosted FrontDeskAgent installs.

The goal is simple: give builders practical call-flow structure they can adapt fast, instead of starting every receptionist agent from a blank prompt.

## What Is Included

- Industry intake flows for plumbing, clinics, hotels, university admissions, estate agents, and agency discovery calls.
- Required fields, smart follow-up questions, urgency rules, SMS templates, and handoff summary formats.
- A JSON schema and validator so playbooks stay machine-readable.
- Usage notes for FrontDeskAgent, OpenZero, Ollama, llama.cpp, and other local-first agent stacks.

Main app: https://github.com/ResearchForumOnline/FrontDeskAgent

Public site: https://frontdeskagent.online/

## Featured Ecosystem Video

[![TalkToAI: Sovereignty Through ZeroThink and OpenZero Infrastructure](https://i.ytimg.com/vi/R52hsRdCmSM/hqdefault.jpg)](https://www.youtube.com/watch?v=R52hsRdCmSM)

This overview explains the wider TalkToAI, ZeroThink, and OpenZero infrastructure that these receptionist playbooks can plug into.

## Quick Use

Copy a playbook into your agent knowledge base, or point your workflow at the JSON file and ask the model to follow the `required_fields`, `urgency_rules`, and `handoff_summary` sections.

```bash
python tools/validate_playbooks.py
```

## Docs

- [Usage](docs/USAGE.md)
- [Playbook design guide](docs/PLAYBOOK_DESIGN.md)
- [OpenZero usage](docs/OPENZERO_USAGE.md)
- [Roadmap](docs/ROADMAP.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security and privacy](SECURITY.md)

## Playbooks

- `playbooks/plumbing-emergency.json`
- `playbooks/clinic-front-desk.json`
- `playbooks/hotel-guest-services.json`
- `playbooks/university-admissions.json`
- `playbooks/estate-agent-viewing.json`
- `playbooks/agency-discovery-call.json`

## License

MIT. Use these flows in commercial or private projects, but check legal, medical, telecom, privacy, and consent rules for your own region.
