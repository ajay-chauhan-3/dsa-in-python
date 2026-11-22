# Binary Search on Answer — Cheat Sheet

### 1. How to Identify
Look at the goal in the question: **"Minimize the Maximum"** OR **"Maximize the Minimum"**.
* Whatever is **inside** (the second word), `mid` represents **that** value.

---

### 2. Case A: "MINIMIZE the MAXIMUM" *(e.g., Split Array Largest Sum)*
* **What is `mid`?** $\rightarrow$ The **MAXIMUM** allowed limit for any single group.
* **Check rule:** Can we make `<= k` groups where **every** group is `<= mid`?
* **If `True` (valid):** Save `ans = mid`, and try **smaller** (`high = mid - 1`).
* **If `False`:** Limit is too tight, try **bigger** (`low = mid + 1`).

---

### 3. Case B: "MAXIMIZE the MINIMUM" *(e.g., Aggressive Cows)*
* **What is `mid`?** $\rightarrow$ The **MINIMUM** required value/gap for every group.
* **Check rule:** Can we place `k` items where **every** gap is `>= mid`?
* **If `True` (valid):** Save `ans = mid`, and try **bigger** (`low = mid + 1`).
* **If `False`:** Gap is too wide, try **smaller** (`high = mid - 1`).

---

### 4. Safe Loop Template *(Zero Infinite Loop Risk)*
Always use `while low <= high:` when saving `ans = mid` and moving by `mid ± 1`.

```python
low, high = min_possible_ans, max_possible_ans
ans = high  # (or 'low' for Case B)

while low <= high:
    mid = (low + high) // 2
    if is_valid(mid):
        ans = mid
        high = mid - 1   # Use 'low = mid + 1' for Case B
    else:
        low = mid + 1    # Use 'high = mid - 1' for Case B

return ans