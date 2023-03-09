import numpy as np
import matplotlib.pyplot as plt

from training.functions.weights_and_reps import (
    max_reps_from_weight,
    max_weight_from_reps,
    one_rep_max,
    rel_int_from_abs_int_repititions,
    abs_int_from_rel_int_repititions,
    repititions_from_rel_int_abs_int,
)


if __name__ == "__main__":
    """Test abs_int_from_rel_int_repititions"""
    rel_int = np.linspace(0.5, 1.0, 6)
    repititions = np.arange(1, 15)

    for rel in rel_int:
        abs_int_calc = [abs_int_from_rel_int_repititions(rel, r) for r in repititions]

        plt.plot(repititions, abs_int_calc, label=round(rel, 2))
        plt.gca().set(ylabel="Absolute intensity", xlabel="Repititions")
        plt.gca().legend(title="Relative intensity")

    plt.show()


    """Test rel_int_from_abs_int_repititions"""
    abs_int = np.linspace(0.5, 1.0, 6)
    repititions = np.arange(1, 15)

    for abs in abs_int:
        rel_int_calc = [rel_int_from_abs_int_repititions(abs, r) for r in repititions]

        plt.plot(repititions, rel_int_calc, label=round(abs, 2))
        plt.gca().set(ylabel="Relative intensity", xlabel="Repititions")
        plt.gca().legend(title="Absolute intensity")

    plt.show()


    """Test repititions_from_rel_int_abs_int"""
    abs_int = np.linspace(0.5, 1.0, 6)
    rel_int = np.linspace(0.5, 1.0, 6)

    for abs in abs_int:
        reps_calc = [repititions_from_rel_int_abs_int(rel, abs) for rel in rel_int]

        plt.plot(rel_int, reps_calc, label=round(abs, 2))
        plt.gca().set(ylabel="Repititions", xlabel="Relative intensity")
        plt.gca().legend(title="Absolute intensity")

    plt.show()


    """Test one_rep_max"""
    weight = np.linspace(50, 100, 11)
    reps = np.arange(1, 16)

    for w in weight:
        orm = [one_rep_max(w, r) for r in reps]

        plt.plot(reps, orm, label=round(w))
        plt.gca().set(ylabel="One Rep Max", xlabel="Repititions")
        plt.gca().legend(title="Weight")
    
    plt.show()


    """Test max_weight_from_reps"""
    orm = np.linspace(100, 150, 11)
    reps = np.arange(1, 16)

    for w in orm:
        weight = [max_weight_from_reps(w, r) for r in reps]

        plt.plot(reps, weight, label=round(w))
        plt.gca().set(ylabel="Max weight", xlabel="Repititions")
        plt.gca().legend(title="1RM")
    
    plt.show()


    """Test max_reps_from_weight"""
    orm = np.linspace(100, 150, 11)
    weight = np.linspace(50, 100, 11)

    for o in orm:
        reps = [max_reps_from_weight(o, w) for w in weight]

        plt.plot(weight, reps, label=round(o))
        plt.gca().set(ylabel="Max Repititions", xlabel="Weight")
        plt.gca().legend(title="1RM")
    
    plt.show()