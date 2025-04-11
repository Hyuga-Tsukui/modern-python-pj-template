from __future__ import annotations

import math
from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class Point:
    """
    A class representing a point in 2D space.
    """

    x: float
    y: float

    def move(self, dx: float, dy: float) -> Point:
        """
        Move the point by dx and dy.
        """
        return Point(self.x + dx, self.y + dy)


def calculate_distance(p1: Point, p2: Point) -> float:
    """
    Calculate the distance between two points.
    """
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def sum(x: int, y: int) -> int:
    """
    A simple function that adds two integers.
    """
    return x + y


def fetch_webpage(url: str) -> str:
    """
    Fetch a webpage from the given URL.

    Raises:
        ValueError: If the page is not found or an error occurs.
    """
    with requests.get(url) as response:
        match response.status_code:
            case 200:
                return response.text
            case 404:
                raise ValueError("Page not found")
            case _:
                raise ValueError(f"Error fetching page: {response.status_code}")


@dataclass
class Stack[T]:
    """
    A simple stack implementation.

    Generic type Class GA python 3.12.
    """

    items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


def main() -> None:
    p1 = Point(x=1, y=3)
    print(p1)
    p2 = Point(x=2, y=2)
    print(p2)
    distance = calculate_distance(p1, p2)
    print(distance)


if __name__ == "__main__":
    main()
