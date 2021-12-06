#!/usr/bin/env python3

print("AoC 2021 Day 6")

with open("testinput", "rt") as f:
    lanternfish_ages = [int(age) for age in f.read().split(",")]

# Part 1
days = 80

for day in range(days + 1):
    print(f"day {day}")
    new_fish = lanternfish_ages.count(-1)
    # for _ in range(new_fish):
    #     lanternfish_ages.remove(-1)
    # lanternfish_ages[lanternfish_ages.index(-1)] = 6
    lanternfish_ages = [f for f in lanternfish_ages if f != -1]
    print("done removing old fish")
    lanternfish_ages += [6] * new_fish
    lanternfish_ages += [8] * new_fish
    print("done spawning new fish")
    lanternfish_ages = [age - 1 for age in lanternfish_ages]
    print("done creating new fish list")

print(f"Part 1: {len(lanternfish_ages)}")
