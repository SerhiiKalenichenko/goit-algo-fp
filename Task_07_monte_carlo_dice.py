import random
from typing import Dict, Tuple

import matplotlib.pyplot as plt


def simulate_dice(num_rolls: int = 100_000) -> Tuple[Dict[int, int], Dict[int, float]]:
    counts = {s: 0 for s in range(2, 13)}
    for _ in range(num_rolls):
        total = random.randint(1, 6) + random.randint(1, 6)
        counts[total] += 1

    probabilities = {s: counts[s] / num_rolls for s in counts}
    return counts, probabilities


def analytic_probs() -> Dict[int, float]:
    combinations = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1,
    }
    total_outcomes = 36
    return {s: combinations[s] / total_outcomes for s in combinations}


def plot_results(mc_probs: Dict[int, float], analytic: Dict[int, float]):
    sums = sorted(mc_probs.keys())
    mc_values = [mc_probs[s] for s in sums]
    analytic_values = [analytic[s] for s in sums]

    x = range(len(sums))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar([i - width / 2 for i in x], mc_values, width, label="Monte Carlo")
    ax.bar([i + width / 2 for i in x], analytic_values, width, label="Аналітично")

    ax.set_xticks(list(x))
    ax.set_xticklabels(sums)
    ax.set_xlabel("Сума на двох кубиках")
    ax.set_ylabel("Ймовірність")
    ax.set_title("Порівняння розподілів (Monte Carlo vs аналітика)")
    ax.legend()
    fig.tight_layout()
    plt.show()


def compare_distributions(mc_probs: Dict[int, float], analytic: Dict[int, float]):
    diffs = {
        s: abs(mc_probs[s] - analytic[s])
        for s in mc_probs
    }
    max_diff = max(diffs.values())
    return diffs, max_diff


if __name__ == "__main__":
    rolls = 100_000

    counts, mc = simulate_dice(rolls)
    analytic = analytic_probs()
    diffs, max_diff = compare_distributions(mc, analytic)

    print(f"Кількість кидків: {rolls}")
    print("Ймовірності (Monte Carlo):")
    for s in range(2, 13):
        print(f"Сума {s}: {mc[s]:.4f}")

    print("\nЙмовірності (аналітично):")
    for s in range(2, 13):
        print(f"Сума {s}: {analytic[s]:.4f}")

    print("\nАбсолютні відхилення:")
    for s in range(2, 13):
        print(f"Сума {s}: {diffs[s]:.4f}")

    print(f"\nМаксимальна похибка: {max_diff:.4f}")
    plot_results(mc, analytic)