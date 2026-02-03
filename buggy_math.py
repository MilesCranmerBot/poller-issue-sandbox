"""Buggy math helpers.

Intentionally contains a bug for the GitHub-mentions poller demo.
"""

from __future__ import annotations

from typing import Iterable


def mean(xs: Iterable[float]) -> float:
    """Return the mean of `xs`.

    BUG: currently returns the sum.
    """
    total = 0.0
    n = 0
    for x in xs:
        total += float(x)
        n += 1
    if n == 0:
        raise ValueError("mean() requires at least one value")
    return total / n
