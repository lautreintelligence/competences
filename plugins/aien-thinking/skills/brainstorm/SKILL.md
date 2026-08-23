---
name: brainstorm
description: "Orchestrate structured brainstorming sessions with 7 distinct expert roles (Facilitator, Optimist, Observer, Counterpoint, Innovator, Solution Seeker, Reflective Thinker). Use when the user wants to: (1) brainstorm ideas on any topic, (2) explore a subject from multiple perspectives, (3) generate creative solutions with built-in critical analysis, (4) run a simulated roundtable discussion, or (5) get a structured ideation session with ranked actionable solutions. Triggered by '/brainstorm [topic]' or any request to brainstorm, ideate, or explore ideas systematically."
license: Apache-2.0
metadata:
  version: "0.1.0"
  author: "AIEN"
  tags: ["ideation", "facilitation", "creativite"]
---

# Brainstorm — Multi-Role Session Orchestrator

Simulate a structured brainstorming roundtable with 7 cognitive perspectives. Each role has a distinct voice and function. The session follows a strict protocol and produces ranked actionable solutions.

## Input Parsing

Extract from the user's input:
- **topic** (required): The main brainstorming subject
- **subtopics** (optional): 2-4 sub-topics to explore

| Situation | Action |
|-----------|--------|
| No subtopics provided | Infer 3 relevant, non-redundant sub-topics |
| Topic too vague | Ask user to clarify with a specific suggestion |
| Topic very narrow | Adapt to 2 focused sub-topics |
| Subtopics > 4 | Ask user to prioritize or keep first 4 |

**Language**: Conduct the entire session in the same language as the user's input.

## The 7 Roles

| # | Role | Speaks | Personality | Core Function |
|---|------|--------|-------------|---------------|
| 1 | **Facilitator** | Opens + closes | Calm, neutral, diplomatic | Open-ended questions, transitions, takeaways |
| 2 | **Optimist** | 1st after Facilitator | Energetic, visionary | Bold positive ideas, "yes and..." |
| 3 | **Observer** | 2nd + round summaries | Precise, factual, neutral | Details, clarifications, factual summaries |
| 4 | **Counterpoint** | 3rd + challenges | Skeptical, analytical, direct | Risks, assumptions, devil's advocate |
| 5 | **Innovator** | 4th | Creative, provocative, curious | Unconventional ideas, cross-domain analogies |
| 6 | **Solution Seeker** | 5th + final solutions | Pragmatic, results-oriented | Specific actionable steps, feasibility |
| 7 | **Reflective Thinker** | Last (always) | Measured, wise, strategic | Long-term implications, systemic view |

For detailed behavioral specs per role, see [references/roles-protocol.md](references/roles-protocol.md).

## Session Protocol

```
FOR EACH SUB-TOPIC (Round N):
  Step 1: Facilitator → open-ended question (NEVER yes/no)
  Step 2: Optimist → Observer → Counterpoint → Innovator → Solution Seeker → Reflective Thinker
  Step 3: Observer → factual summary of the round (zero opinion)
  Step 4: Counterpoint → challenges at least one point from summary

AFTER ALL SUB-TOPICS:
  Step 5: Observer → global summary of entire discussion
  Step 6: Reflective Thinker → strategic long-term analysis
  Step 7: Solution Seeker → ranked solutions table (max 5-7)
  Step 8: Facilitator → 3-5 key takeaways + closing
```

## Output Template

```markdown
# Session Brainstorming : {topic}

> **Sous-themes explores**: {list}
> **Note**: Session simulant 7 perspectives cognitives generees par IA.
> Les idees produites sont des pistes de reflexion, pas des recommandations validees.

## Round 1 : {subtopic_1}

**[Facilitateur]:** {open-ended question}

**[Optimiste]:** {2-4 sentences}

**[Observateur]:** {1-3 sentences, may ask clarification}

**[Contrepoint]:** {2-3 sentences challenging}

**[Innovateur]:** {2-3 sentences unconventional}

**[Solution Seeker]:** {2-3 sentences actionable}

**[Penseur Reflexif]:** {1-3 sentences strategic}

**[Observateur — Synthese Round]:** {factual summary}

**[Contrepoint — Challenge]:** {challenge at least one point}

---

## Round N : {subtopic_N}
[Same structure repeats]

---

## Synthese et Solutions

**[Observateur — Resume global]:**
{comprehensive summary across all rounds}

**[Penseur Reflexif — Analyse strategique]:**
{long-term implications}

**[Solution Seeker — Solutions classees]:**

| # | Solution | Applicabilite | Effort | Impact |
|---|----------|---------------|--------|--------|
| 1 | {best solution} | Haute | {F/M/E} | {F/M/E} |
| 2 | ... | ... | ... | ... |

**[Facilitateur — Cloture]:**
{3-5 key takeaways}
```

## Hard Rules

| Type | Rule |
|------|------|
| **MUST** | All 7 roles speak at least once per round |
| **MUST** | Facilitator opens with open-ended question (never yes/no) |
| **MUST** | Observer summaries are purely factual (zero opinion) |
| **MUST** | Counterpoint challenges at least one idea per round |
| **MUST** | Solution Seeker proposes concrete, specific actions |
| **MUST** | Final synthesis contains ONLY ideas actually discussed |
| **MUST** | Each role maintains distinct voice throughout |
| **NEVER** | Blend perspectives between roles |
| **NEVER** | Invent statistics, studies, or fake citations |
| **NEVER** | Drift from the main topic |
| **NEVER** | Claim the roles are real people |
