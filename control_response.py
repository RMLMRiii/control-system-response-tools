import math
from typing import List, Tuple


def first_order_response(t: float, tau: float) -> float:
    return 1 - math.exp(-t / tau)


def second_order_response(t: float, wn: float, zeta: float) -> float:
    if zeta >= 1:
        raise ValueError("This simple model is for underdamped systems only (zeta < 1).")

    wd = wn * math.sqrt(1 - zeta**2)
    phi = math.acos(zeta)

    return 1 - (1 / math.sqrt(1 - zeta**2)) * math.exp(-zeta * wn * t) * math.sin(wd * t + phi)


def generate_first_order_data(tau: float, time_values: List[float]) -> List[Tuple[float, float]]:
    return [(t, first_order_response(t, tau)) for t in time_values]


def generate_second_order_data(wn: float, zeta: float, time_values: List[float]) -> List[Tuple[float, float]]:
    return [(t, second_order_response(t, wn, zeta)) for t in time_values]


def display_response(title: str, data: List[Tuple[float, float]]) -> None:
    print(f"\n{title}")
    print("-" * 40)
    print(f"{'Time (s)':>10} | {'Response':>12}")
    print("-" * 40)

    for t, y in data:
        print(f"{t:10.2f} | {y:12.6f}")


def main() -> None:
    time_values = [0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]

    tau = 1.5
    wn = 4.0
    zeta = 0.3

    first_data = generate_first_order_data(tau, time_values)
    second_data = generate_second_order_data(wn, zeta, time_values)

    display_response("FIRST-ORDER STEP RESPONSE", first_data)
    display_response("SECOND-ORDER STEP RESPONSE", second_data)


if __name__ == "__main__":
    main()
