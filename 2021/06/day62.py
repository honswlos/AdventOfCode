#!/usr/bin/env python3
from numba import njit, jit
import numpy

print("AoC 2021 Day 6")

with open("input", "rt") as f:
    lanternfish_ages = numpy.array([int(age) for age in f.read().split(",")])

# Part 1
days = 256


@njit(parallel=True)
def day6(lf):
    return numpy.array([age - 1 for age in lf])


@njit(parallel=True)
def day62(lf2):
    return lf2[lf2 != -1]


@njit(parallel=True)
def day63(lf3, sixeights):
    return numpy.append(lf3, sixeights)


for day in range(days + 1):
    print(f"day {day}")
    new_fish = numpy.count_nonzero(lanternfish_ages == -1)
    # lanternfish_ages = numpy.delete(
    #     lanternfish_ages, numpy.where(lanternfish_ages == -1)
    # )
    print("removing -1s")
    lanternfish_ages = day62(lanternfish_ages)
    print("adding 6s and 8s")
    sixeights = numpy.tile((6, 8), new_fish)
    lanternfish_ages = day63(lanternfish_ages, sixeights)
    # lanternfish_ages = numpy.append(lanternfish_ages, numpy.tile(8, new_fish))
    print("subtracting")
    lanternfish_ages = day6(lanternfish_ages)

print(f"Part 1: {len(lanternfish_ages)}")
