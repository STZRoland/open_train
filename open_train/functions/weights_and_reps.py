from typing import Any, Optional


"""Calculations for Epley formula"""
def one_rep_max(weight: float, repititions: float) -> float:
    return weight * (1 + repititions / 30)


def max_weight_from_reps(one_rep_max_value: float, repititions: float) -> float:
    return one_rep_max_value / (1 + repititions / 30)


def max_reps_from_weight(one_rep_max_value: float, weight: float) -> float:
    return 30 * (one_rep_max_value / weight - 1)


"""Calculations for Brzycki formula"""
# def one_rep_max(weight: float, repititions: float) -> float:
#     return weight * 36 / (37 - repititions)


# def max_weight_from_reps(one_rep_max_value: float, repititions: float) -> float:
#     return one_rep_max_value * (37 - repititions) / 36


# def max_reps_from_weight(one_rep_max_value: float, weight: float) -> float:
#     return 37 - 36 * weight / one_rep_max_value


# Derived functions

def n_rep_max(weight: float, repititions: float, n: int) -> float:
    max = one_rep_max(weight, repititions)
    if n == 1:
        return max
    else:
        return max_weight_from_reps(max, n)


def weight_from_abs_int(one_rep_max_value: float, absolute_intensity: float) -> float:
    return one_rep_max_value * absolute_intensity


def abs_int_from_weight(one_rep_max_value: float, weight: float) -> float:
    return weight / one_rep_max_value


# Trifactor
def rel_int_from_abs_int_repititions(
    absolute_intensity: float, repititions: float
) -> float:
    return absolute_intensity / max_weight_from_reps(1, repititions)


def repititions_from_rel_int_abs_int(
    relative_intensity: float, absolute_intensity: float
) -> float:
    # return max_reps_from_weight(1, absolute_intensity / relative_intensity)
    return relative_intensity * max_reps_from_weight(1, absolute_intensity)


def abs_int_from_rel_int_repititions(
    relative_intensity: float, repititions: float
) -> float:
    return relative_intensity * max_weight_from_reps(1, repititions)


def calc_missing_values(
    values_dict: dict[str, Any], one_rep_max_value: Optional[float] = None
):
    abs_int = values_dict.get("absolute_intensity")
    rel_int = values_dict.get("relative_intensity")
    reps = values_dict.get("repititions")
    weight = values_dict.get("weight")

    if one_rep_max_value is not None:
        if abs_int is None and weight is not None:
            abs_int = abs_int_from_weight(one_rep_max_value, weight)
        if weight is None and abs_int is not None:
            weight = weight_from_abs_int(one_rep_max_value, abs_int)

    if abs_int is not None and rel_int is not None and reps is None:
        reps = repititions_from_rel_int_abs_int(rel_int, abs_int)
    if abs_int is not None and reps is not None and rel_int is None:
        rel_int = rel_int_from_abs_int_repititions(abs_int, reps)
    if rel_int is not None and reps is not None and abs_int is None:
        abs_int = abs_int_from_rel_int_repititions(rel_int, reps)

    if one_rep_max_value is not None and abs_int is not None and weight is None:
        weight = weight_from_abs_int(one_rep_max_value, abs_int)

    # TODO: Check if calculated values disagree with existing (except for repititions)
    
    return {"absolute_intensity": abs_int, "relative_intensity": rel_int, "repititions": reps, "weight": weight}
