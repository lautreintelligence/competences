---
name: clean-code-audit
description: >
  Réalise des audits Clean Code selon les 6 principes de Robert C. Martin (nommage, fonctions,
  commentaires, formatage, gestion d'erreur, DRY). Utilise ce skill quand l'utilisateur demande
  d'auditer du code, de relire la qualité d'un code, de vérifier les violations de clean code,
  d'évaluer la dette technique, ou d'améliorer la lisibilité du code. Retourne des rapports
  structurés avec notation de sévérité (🔴 Critique / 🟠 Majeur / 🟡 Mineur), des exemples
  concrets de refactoring et des recommandations priorisées.
license: Apache-2.0
metadata:
  version: "0.1.1"
  author: "L'Autre Intelligence & Nous"
  tags: "code-review, clean-code, refactoring"
---

# Clean Code Audit

Analyze code against Uncle Bob's 6 Clean Code principles. Generate actionable audit reports with weighted scoring.

**Philosophy**: "Clean code looks like it was written by someone who cares."

## Workflow

### 1. Obtain Code

Get the code to audit via:
- File path provided by user → Read the file
- Code pasted in conversation → Use directly
- User selection → Use the highlighted code

If no code provided, ask:
> "Provide the code to audit: file path, paste it, or highlight a selection."

### 2. Analyze Against 6 Principles

For each principle, identify violations with:
- **Location**: Function name, line number
- **Severity**: 🔴 Critical | 🟠 Major | 🟡 Minor
- **Description**: What's wrong and why

| Principle | Key Question |
|-----------|--------------|
| 1. Naming | Does every name reveal intent? |
| 2. Functions | Small? Single purpose? Few params? |
| 3. Comments | Code self-documenting? Comments explain WHY? |
| 4. Formatting | Consistent? Readable? Organized? |
| 5. Errors | Explicit handling? Specific exceptions? |
| 6. DRY | No duplication? Single source of truth? |

**Reference**: See [clean-code-principles.md](references/clean-code-principles.md) for detailed criteria and examples.

### 3. Calculate Score

```
Score = 100 - (🔴 × 15) - (🟠 × 5) - (🟡 × 1)
```

| Score | Rating |
|-------|--------|
| 90-100 | 🌟 Excellent |
| 75-89 | ✅ Good |
| 50-74 | ⚠️ Needs improvement |
| 25-49 | 🔶 Problematic |
| 0-24 | 🔴 Critical |

### 4. Generate Report

Use the structured template with:
- Executive summary (score + violation counts)
- Analysis per principle
- Before/after examples for critical issues
- Prioritized recommendations
- Positive points (always mention what's done well)

**Template**: See [report-template.md](references/report-template.md) for full structure.

## Critical Rules

### Anti-Hallucination
- Base observations on VISIBLE code only
- Never invent violations not in the code
- Never presume undocumented business logic
- Distinguish: **Certain** vs **Suspicion** vs **Recommendation**

### Tone
- Pedagogical and constructive
- Never: "horrible code", "beginner mistake"
- Always explain the benefit of improvements
- Always mention positive aspects

### Quality Checklist
- [ ] All 6 principles covered
- [ ] Location specified for each violation
- [ ] Before/after for every 🔴 Critical
- [ ] Score correctly calculated
- [ ] Constructive tone throughout

## Quick Reference

**Severity thresholds**:
- 🔴 God function (100+ lines), silent `except: pass`, misleading names
- 🟠 Function doing 2-3 things, generic `except Exception`, >3 params
- 🟡 Minor formatting, redundant comments, small repetitions

**Common patterns**:
```python
# 🔴 Critical: Silent error
except: pass

# 🟠 Major: Cryptic name
def proc(d): ...

# 🟡 Minor: Redundant comment
# Increment i
i += 1
```
