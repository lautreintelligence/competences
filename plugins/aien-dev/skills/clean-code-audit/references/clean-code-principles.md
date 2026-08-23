# Clean Code Principles Reference

Based on "Clean Code" by Robert C. Martin (Uncle Bob).

---

## Table of Contents

1. [Meaningful Names](#1-meaningful-names)
2. [Functions](#2-functions)
3. [Comments](#3-comments)
4. [Formatting](#4-formatting)
5. [Error Handling](#5-error-handling)
6. [DRY](#6-dry)
7. [Severity Criteria](#severity-criteria)
8. [Scoring Formula](#scoring-formula)

---

## 1. Meaningful Names

**Rule**: Every name must reveal intent.

### Violations

| Pattern | Severity | Example |
|---------|----------|---------|
| Single-letter vars (except iterators) | 🟠 Major | `x`, `d`, `temp` |
| Cryptic names | 🟠 Major | `processData`, `doIt` |
| Type encoding | 🟡 Minor | `strName`, `intCount` |
| Misleading names | 🔴 Critical | Name doesn't match behavior |

### Good Patterns

```python
# Variables: descriptive noun
user_count, file_path, is_valid

# Functions: verb_action (snake_case)
get_user(), save_file(), calculate_total()

# Classes: NounPhrase (PascalCase)
UserManager, FileProcessor, DataValidator

# Constants: UPPER_SNAKE
MAX_SIZE, DEFAULT_TIMEOUT, API_KEY

# Booleans: is_/has_/can_ prefix
is_active, has_permission, can_edit
```

---

## 2. Functions

**Rule**: Small, single purpose, one level of abstraction.

### Violations

| Pattern | Severity | Threshold |
|---------|----------|-----------|
| God function | 🔴 Critical | >100 lines |
| Multiple responsibilities | 🟠 Major | Does 2-3 things |
| Too many parameters | 🟠 Major | >3 params |
| Mixed abstraction levels | 🟠 Major | High+low level mixed |
| Long but coherent | 🟡 Minor | 30-50 lines |

### Good Pattern

```python
# ❌ Bad: Does everything
def process_user(data):
    # validate, clean, save, notify... 50+ lines

# ✅ Good: Orchestrates single-purpose functions
def create_user(data):
    validate_email(data['email'])
    user = normalize_user_data(data)
    save_user(user)
    return user
```

---

## 3. Comments

**Rule**: Code should be self-documenting. Comments explain WHY, not WHAT.

### Violations

| Pattern | Severity |
|---------|----------|
| Misleading/dangerous comments | 🔴 Critical |
| Commented-out code | 🟠 Major |
| Obsolete comments | 🟠 Major |
| Redundant comments | 🟡 Minor |

### Good vs Bad

```python
# ❌ Bad: Says what code does
# Increment i by 1
i += 1

# ✅ Good: Explains why
# 86400 seconds because time.sleep() doesn't accept "1 day"
CACHE_DURATION = 86400

# ✅ Good: Documents public API
def upload_file(path: str, max_size_kb: int = 100) -> bool:
    """Upload file to storage with size validation.

    Args:
        path: Local file path
        max_size_kb: Maximum file size in KB

    Returns:
        True if upload succeeded
    """
```

---

## 4. Formatting

**Rule**: Consistent, readable, organized.

### Violations

| Pattern | Severity |
|---------|----------|
| Unreadable formatting | 🔴 Critical |
| Inconsistent style | 🟠 Major |
| Lines >120 chars | 🟡 Minor |
| Minor spacing issues | 🟡 Minor |

### File Organization (Python)

```python
"""Module docstring."""

# 1. Standard library imports
import os
import json

# 2. Third-party imports
import requests

# 3. Local imports
from .utils import helper

# 4. Constants
MAX_RETRIES = 3

# 5. Classes/Functions (high to low level)
class MainClass:
    pass

def public_function():
    pass

def _private_helper():
    pass

# 6. Entry point
if __name__ == "__main__":
    pass
```

---

## 5. Error Handling

**Rule**: Explicit, specific, fail fast.

### Violations

| Pattern | Severity | Example |
|---------|----------|---------|
| Silent errors | 🔴 Critical | `except: pass` |
| Catching Ctrl+C | 🔴 Critical | Bare `except:` |
| Generic exception | 🟠 Major | `except Exception` |
| Uninformative message | 🟡 Minor | `raise Error("failed")` |

### Good Pattern

```python
# ❌ Bad: Swallows everything
try:
    result = operation()
except:
    pass

# ✅ Good: Specific, informative
def read_config(path="config.json"):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return {"debug": False}  # Sensible default
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid config in {path}: {e}")
```

---

## 6. DRY

**Rule**: Don't Repeat Yourself. Single source of truth.

### Violations

| Pattern | Severity |
|---------|----------|
| 10+ line block duplicated | 🔴 Critical |
| Similar logic not factored | 🟠 Major |
| Repeated constants | 🟡 Minor |
| Small pattern duplication | 🟡 Minor |

### Good Pattern

```python
# ❌ Bad: Logic duplicated
def greet_admin():
    hour = datetime.now().hour
    period = "morning" if hour < 12 else "afternoon" if hour < 18 else "evening"
    return f"Good {period}, Admin!"

def greet_user(name):
    hour = datetime.now().hour
    period = "morning" if hour < 12 else "afternoon" if hour < 18 else "evening"
    return f"Good {period}, {name}!"

# ✅ Good: Extracted
def get_time_period():
    hour = datetime.now().hour
    if hour < 12: return "morning"
    if hour < 18: return "afternoon"
    return "evening"

def greet(name):
    return f"Good {get_time_period()}, {name}!"
```

---

## Severity Criteria

### 🔴 Critical (-15 points)
- Makes code hard to maintain or debug
- Creates bug risks or unexpected behavior
- Fundamentally violates readability

### 🟠 Major (-5 points)
- Significantly reduces code quality
- Complicates understanding or evolution
- Clearly suboptimal pattern

### 🟡 Minor (-1 point)
- Desirable but not urgent improvement
- Style or convention detail
- Possible optimization

---

## Scoring Formula

```
Score = 100 - (critical × 15) - (major × 5) - (minor × 1)
```

**Bounds**: min 0, max 100

| Score | Rating | Emoji |
|-------|--------|-------|
| 90-100 | Excellent | 🌟 |
| 75-89 | Good | ✅ |
| 50-74 | Needs improvement | ⚠️ |
| 25-49 | Problematic | 🔶 |
| 0-24 | Critical | 🔴 |
