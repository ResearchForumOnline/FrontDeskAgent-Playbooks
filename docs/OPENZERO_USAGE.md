# OpenZero Usage

These playbooks can be used with OpenZero as local agent context.

## Simple Prompt Pattern

```text
Use the attached playbook as the intake policy.
Ask only for missing required fields.
Apply urgency rules conservatively.
Do not invent prices or availability.
End with a staff handoff summary.
```

## OpenZero + FrontDeskAgent

Best path:

1. Run OpenZero locally.
2. Run FrontDeskAgent.
3. Configure FrontDeskAgent `LLM_BACKEND=auto`.
4. Set `OPENZERO_LLM_URL` to the OpenZero local `/v1/chat/completions` endpoint.
5. Add the selected playbook to business knowledge.
6. Test in the playground before exposing public intake.

## CPU-Friendly Use

Small local models work better when the playbook is structured.

Tips:

- use concise field names;
- avoid huge policy blocks;
- put emergency rules in a clear list;
- keep templates short;
- ask one or two follow-up questions at a time.

## Operator Safety

The playbook is a workflow guide, not a legal or medical authority. The business operator remains responsible for compliance and customer handling.

