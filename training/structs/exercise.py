from __future__ import annotations
from typing import Optional, Type, Union
from training.structs.set import Set, SetWeightsAndReps


class Exercise:
    sets: list[Set] = []
    set_type = Set

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(exercise_dict: dict) -> Exercise:
        if "Exercise" in exercise_dict:
            exercise_dict = exercise_dict["Exercise"]

        id = 0 
        exercise_type_str = exercise_dict.get("type", "")

        new_exercise = exercise_types[exercise_type_str](
            id,
            exercise_dict.get("name", None),
        )

        sets = exercise_dict.get("sets", [])
        for set in sets:
            new_exercise.add_set(set)
        
        print(new_exercise.id)
        
        return new_exercise

    def add_set(self, set_object: dict):
        self.sets.append(self.set_type.from_dict(set_object))

    def check_validity(self) -> bool:
        for set in self.sets:
            if not set.check_validity():
                return False
        return True

    def get_total_volume(self) -> float:
        raise NotImplementedError

    def get_max_intensity(self) -> float:
        raise NotImplementedError


class ExerciseWeightsAndRep(Exercise):
    set_type = SetWeightsAndReps
    sets: list[set_type] = []


exercise_types: dict[str, Type[Exercise]] = {
    "weights_reps": ExerciseWeightsAndRep
}