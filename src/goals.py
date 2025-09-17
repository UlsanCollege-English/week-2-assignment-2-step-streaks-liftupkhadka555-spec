from typing import List, Tuple

def max_window_sum(values: List[int], k: int) -> Tuple[int, int] | None:
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(values):
        return None

    max_sum = current_sum = sum(values[:k])
    start_index = 0

    for i in range(1, len(values) - k + 1):
        current_sum = current_sum - values[i - 1] + values[i + k - 1]
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i

    return (start_index, max_sum)


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(values):
        return 0

    count = 0
    current_sum = sum(values[:k])

    if current_sum / k >= target_avg:
        count += 1

    for i in range(1, len(values) - k + 1):
        current_sum = current_sum - values[i - 1] + values[i + k - 1]
        if current_sum / k >= target_avg:
            count += 1

    return count


def longest_rising_streak(values: List[int]) -> int:
    if not values:
        return 0

    max_streak = streak = 1

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1

    return max_streak
