import random
from typing import List

def random_no_consecutive(n: int, a: int, b: int, rng: random.Random | None = None) -> List[int]:
    """
    Generate a length-n list of integers in [a, b] with no equal consecutive elements.
    Runs in O(n) time with O(1) extra space and never retries.

    Args:
        n: length of the list (n >= 0)
        a, b: inclusive range bounds (a <= b)
        rng: optional random.Random instance (for seeding/reproducibility)

    Returns:
        List[int]: numbers in [a, b] with no consecutive duplicates.

    Raises:
        ValueError: if impossible (e.g., n > 1 while a == b).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if a > b:
        raise ValueError("Require a <= b")
    if n == 0:
        return []

    m = b - a + 1
    if m == 1:
        if n == 1:
            return [a]
        raise ValueError("Impossible: only one value available but n > 1 (would force duplicates).")

    rnd = rng or random

    # First element: uniform in [a, b]
    first = rnd.randint(a, b)
    out = [first]

    # For each next element, choose uniformly from [a, b] \ {prev}
    # Trick: pick k in [0, m-2]; map to value in [a, b] skipping prev.
    for _ in range(1, n):
        k = rnd.randrange(m - 1)      # 0 .. m-2
        candidate = a + k
        prev = out[-1]
        if candidate >= prev:
            candidate += 1            # skip the previous value
        out.append(candidate)

    return out

# --- Example usage ---
if __name__ == "__main__":
    # Reproducible run (optional)
    rng = random.Random(42)
    seq = random_no_consecutive(n=13, a=1, b=16, rng=rng)
    print(seq)
