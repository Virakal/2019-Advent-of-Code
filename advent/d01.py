#!/usr/bin/env python3

from advent.common import data_path


def calculate_fuel_cost(module_mass: int):
    return int(module_mass / 3) - 2


if __name__ == "__main__":
    with open(data_path / "d01.txt", "r") as f:
        lines = f.readlines()

    masses = [int(line.strip()) for line in lines]
    fuel_counts = [calculate_fuel_cost(mass) for mass in masses]
    print("Part 1:", sum(fuel_counts))
