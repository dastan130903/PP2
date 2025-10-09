# lab4_

from datetime import datetime, date, timedelta
from math import pi, tan, radians
import json
from typing import Generator, List, Dict, Any

# ---------------------------
# Generators / Iterators
# ---------------------------

def gen_squares_upto(n: int) -> Generator[int, None, None]:
    """Generate squares 0^2 .. n^2 inclusive."""
    for x in range(n + 1):
        yield x * x

def gen_evens_upto(n: int) -> Generator[int, None, None]:
    """Generate even numbers 0,2,4,... up to n."""
    for x in range(0, n + 1, 2):
        yield x

def gen_divisible_by_3_and_4(n: int) -> Generator[int, None, None]:
    """Yield numbers in [0..n] divisible by both 3 and 4 (i.e. by 12)."""
    for x in range(0, n + 1):
        if x % 12 == 0:
            yield x

def squares_range(a: int, b: int) -> Generator[int, None, None]:
    """Yield squares of integers from a to b inclusive."""
    for x in range(a, b + 1):
        yield x * x

def countdown(n: int) -> Generator[int, None, None]:
    """Yield n down to 0."""
    for x in range(n, -1, -1):
        yield x

# ---------------------------
# Date / Time tasks
# ---------------------------

def subtract_five_days_from_today() -> date:
    return date.today() - timedelta(days=5)

def yesterday_today_tomorrow() -> (date, date, date):
    today = date.today()
    return (today - timedelta(days=1), today, today + timedelta(days=1))

def drop_microseconds(dt: datetime) -> datetime:
    return dt.replace(microsecond=0)

def date_diff_seconds(dt1: datetime, dt2: datetime) -> int:
    """Absolute difference in seconds between dt1 and dt2."""
    return int(abs((dt2 - dt1).total_seconds()))

# ---------------------------
# Math library tasks
# ---------------------------

def deg_to_rad(deg: float) -> float:
    """Convert degrees to radians."""
    return deg * pi / 180.0

def trapezoid_area(height: float, base1: float, base2: float) -> float:
    """Area of a trapezoid: (a + b) * h / 2"""
    return (base1 + base2) * height / 2.0

def regular_polygon_area(n_sides: int, side_length: float) -> float:
    """Area of a regular polygon: (n * s^2) / (4 * tan(pi/n))"""
    if n_sides < 3:
        raise ValueError("Polygon must have at least 3 sides")
    return (n_sides * side_length ** 2) / (4.0 * tan(pi / n_sides))

def parallelogram_area(base: float, height: float) -> float:
    return base * height

# ---------------------------
# JSON parsing (sample-data.json style)
# ---------------------------

# parse_interfaces.py
import json

def parse_and_print(path: str = "data.json") -> None:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':>6}  {'MTU':>6}")
    print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")

    for item in data.get("imdata", []):
        phys = item.get("l1PhysIf", {})
        attrs = phys.get("attributes", {})
        dn   = attrs.get("dn", "")
        descr= attrs.get("descr", "")
        speed= attrs.get("speed", "")
        mtu  = attrs.get("mtu", "")
        print(f"{dn:<50} {descr:<20} {str(speed):>8} {str(mtu):>7}")

if __name__ == "__main__":
    parse_and_print("data.json")
