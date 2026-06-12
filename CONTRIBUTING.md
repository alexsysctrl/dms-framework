# Contributing to DMS Framework

## Overview

The Derived Modular Spectrum (DMS) Framework is an ongoing research program organized into sequential agent sessions. Each agent explores a specific domain, producing equations, theorems, and patterns that build on prior work.

## Agent Pipeline

Agents execute sequentially, each responsible for a specific research area:

1. **Read context** — Review global-research-log.md, mission.md, and agent-handoff.md from the previous agent
2. **Check numbering** — Verify highest equation number (currently E1935) and pattern number (currently P770)
3. **Write output** — Produce equations (E###), theorems (X.Y), and patterns (P###)
4. **Write handoff** — Complete agent-handoff.md with priorities for the next agent
5. **Update global log** — Add entry to global-research-log.md

### Phase Organization

| Phase | Agents | Focus |
|-------|--------|-------|
| Phase 1 | 1–12 | Mathematical Foundations |
| Phase 2 | 17–30 | Physical Systems |
| Phase 3 | 32–57 | Deep Mathematics |
| Phase 4 | 58–71 | Foundations & Expansion |

## File Naming Conventions

### Agent Directories

Each agent has a dedicated directory under `explorations/`:

```
explorations/XX-description/
```

- `XX` is a zero-padded agent number (01, 02, ..., 71)
- `description` is a lowercase, hyphenated description of the agent's focus area
- Examples: `01-math-foundations/`, `33-neural-networks-and-deep-learning/`

### Agent Files

| File | Purpose |
|------|---------|
| `agent-handoff.md` | Notes for the next agent (renamed from notes-for-next-agent.md) |
| `session-log.md` | Session record (renamed from exploration-log.md) |
| `*.md` | Main research files |
| `mission.md` | Mission statement for the agent |

### Equation and Theorem Numbering

- **Equations**: Sequential across all agents (E1–E1935). Check the highest number before writing.
- **Theorems**: Agent-specific prefix (e.g., 70.1–70.30 for Agent 70).
- **Patterns**: Sequential across all agents (P1–P770). Check the highest number before writing.

## How to Continue Research

### Starting a New Agent

1. Create a new directory: `explorations/XX-{description}/`
2. Write `mission.md` defining scope
3. Read `global-research-log.md` for overall state
4. Read `agent-handoff.md` from the previous agent for priorities
5. Read `session-log.md` from the previous agent for session record
6. Check highest equation and pattern numbers
7. Write your research output in chunks of 25-30 lines per write_file call
8. Complete `agent-handoff.md` with priorities for the next agent
9. Update `global-research-log.md` with your completion entry

### Writing Guidelines

- Write in chunks of 25-30 lines per file operation
- Mark all theorems as PROVEN with explicit proof text
- Include diagrams as ASCII art where applicable
- Connect to specific equations from previous agents
- Avoid repetition by reading agent-handoff.md before writing
- Use sequential equation numbering to prevent duplicates

### Adding Figures

PNG figures go in `figures/diagrams/` or `figures/plots/`. GIF animations go in `figures/animations/`.

### Adding Papers

Publication papers go in the `papers/` directory.

## Best Practices

1. Read global-research-log.md first for overall state
2. Read mission.md for scope
3. Read agent-handoff.md from previous agent
4. Check highest equation number before writing
5. Check highest pattern number before writing
6. Write in chunks of 25-30 lines per write_file call
7. Connect to specific equations from previous agents
8. Mark all theorems as PROVEN with explicit proof text
9. Include diagrams as ASCII art
10. Write agent-handoff.md with specific priorities for next agent

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Citation

If you use this framework in your research, please cite:

```bibtex
@misc{dms2026,
  author = {DMS Research Team},
  title = {Derived Modular Spectrum ({DMS}) Framework},
  year = {2026},
  version = {Phase 7},
  url = {https://github.com/alexsysctrl/dms-framework}
}
```
