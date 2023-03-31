def max_contiguous_c(A: str, B: int, C: str) -> int:
    n = len(A)
    max_c = 0
    freq = {}
    left = right = 0
    while right < n:
        freq[A[right]] = freq.get(A[right], 0) + 1
        max_freq = freq.get(C, 0)
        if right - left + 1 - max_freq > B:
            freq[A[left]] -= 1
            left += 1
        max_c = max(max_c, right - left + 1)
        right += 1
    return max_c