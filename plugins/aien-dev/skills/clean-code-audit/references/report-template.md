# Audit Report Template

Use this template structure for all Clean Code audit reports.

---

```markdown
# 🔍 Clean Code Audit

## 📊 Executive Summary

| Metric | Value |
|--------|-------|
| **Global Score** | XX/100 [emoji] |
| 🔴 Critical Violations | X |
| 🟠 Major Violations | X |
| 🟡 Minor Violations | X |
| **Language** | [detected] |

**Verdict**: [One constructive sentence summarizing code quality]

---

## 📋 Analysis by Principle

### 1️⃣ Meaningful Names

**Status**: [✅ Good | ⚠️ Issues found | 🔴 Critical issues]

[List violations with location and severity emoji]

### 2️⃣ Functions

**Status**: [✅ Good | ⚠️ Issues found | 🔴 Critical issues]

[List violations with location and severity emoji]

### 3️⃣ Comments

**Status**: [✅ Good | ⚠️ Issues found | 🔴 Critical issues]

[List violations with location and severity emoji]

### 4️⃣ Formatting

**Status**: [✅ Good | ⚠️ Issues found | 🔴 Critical issues]

[List violations with location and severity emoji]

### 5️⃣ Error Handling

**Status**: [✅ Good | ⚠️ Issues found | 🔴 Critical issues]

[List violations with location and severity emoji]

### 6️⃣ DRY

**Status**: [✅ Good | ⚠️ Issues found | 🔴 Critical issues]

[List violations with location and severity emoji]

---

## 🛠️ Refactoring Examples

[For EACH critical violation, provide before/after]

### [Problem Title]

**Before** ❌
```[lang]
[original code]
```

**After** ✅
```[lang]
[refactored code]
```

**Why**: [Explain the benefit]

---

## 🎯 Priority Recommendations

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | [Most important fix] | High | [Low/Med/High] |
| 2 | [Second priority] | Medium | [Low/Med/High] |
| 3 | [Third priority] | Medium | [Low/Med/High] |

---

## ✨ Positive Points

[Always mention what's done well - at least 1-2 points]

---

## 💬 Conclusion

[Constructive message with clear next steps]
```
