from typing import Dict, List


ITEMS: Dict[str, Dict[str, int]] = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, object]:
    """Жадібний підхід: максимізація співвідношення калорії / вартість."""
    ordered = sorted(
        items.items(),
        key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
        reverse=True,
    )

    chosen: List[str] = []
    total_cost = 0
    total_calories = 0

    for name, data in ordered:
        cost = data["cost"]
        calories = data["calories"]
        if total_cost + cost <= budget:
            chosen.append(name)
            total_cost += cost
            total_calories += calories

    return {
        "items": chosen,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, object]:
    """0/1 рюкзак: оптимальний набір страв за калорійністю при заданому бюджеті."""
    names = list(items.keys())
    n = len(names)

    dp = [0] * (budget + 1)
    keep = [[False] * (budget + 1) for _ in range(n)]

    for i, name in enumerate(names):
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for c in range(budget, cost - 1, -1):
            if dp[c - cost] + calories > dp[c]:
                dp[c] = dp[c - cost] + calories
                keep[i][c] = True

    chosen: List[str] = []
    c = budget
    for i in range(n - 1, -1, -1):
        if keep[i][c]:
            name = names[i]
            chosen.append(name)
            c -= items[name]["cost"]
    chosen.reverse()

    total_cost = sum(items[name]["cost"] for name in chosen)
    total_calories = sum(items[name]["calories"] for name in chosen)

    return {
        "items": chosen,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


if __name__ == "__main__":
    budget_value = 100

    greedy_result = greedy_algorithm(ITEMS, budget_value)
    dp_result = dynamic_programming(ITEMS, budget_value)

    print(f"Бюджет: {budget_value}")
    print("Жадібний алгоритм:", greedy_result)
    print("Динамічне програмування:", dp_result)