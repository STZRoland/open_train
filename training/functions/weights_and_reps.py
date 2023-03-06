"""Calculations for Epley formula"""


# 3 Core functions

def one_rep_max(weight: float, repititions: int) -> float:
    return weight * (1 + repititions / 30)


def max_weight_from_reps(one_rep_max_value: float, repititions: int) -> float:
    return one_rep_max_value / (1 + repititions / 30)


def max_reps_from_weight(one_rep_max_value: float, weight: float) -> int:
    return round(30 * (one_rep_max_value / weight - 1))


# Derived functions

def n_rep_max(weight: float, repititions: int, n: int) -> float:
    max = one_rep_max(weight, repititions)
    if n == 1:
        return max
    else:
        return max_weight_from_reps(max, n)


def abs_int_from_rel_int(relative_intensity: float, repititions: int) -> float:
    return max_weight_from_reps(1, repititions) * relative_intensity


def weight_from_rel_int(one_rep_max_value: float, relative_intensity: float, repititions: int) -> float:
    return abs_int_from_rel_int(relative_intensity, repititions) * one_rep_max_value


def weight_from_abs_int(one_rep_max_value: float, absolute_intensity: float) -> float:
    return one_rep_max_value * absolute_intensity


def abs_int_from_weight(one_rep_max_value: float, weight: float) -> float:
    return weight / one_rep_max_value


def rel_int_from_weight_repititions(one_rep_max_value: float, weight: float, repititions: int) -> float:
    return one_rep_max(weight, repititions) / one_rep_max_value


def repititions_from_rel_int_weight(one_rep_max_value: float, weight: float, relative_intensity: float) -> int:
    return max_reps_from_weight(one_rep_max_value * relative_intensity, weight)
