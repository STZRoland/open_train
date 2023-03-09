from __future__ import annotations
from typing import Any, Type
from training.structs.set import Set, SetWeightsAndReps
from training.state.exercises import exercises_state


class Exercise:
    # Potential alternative name: Movmement
    sets: list[Set] = []
    set_type = Set

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.max = self._get_max_from_state()

    @staticmethod
    def from_dict(exercise_dict: dict, fill_values: bool = False) -> Exercise:
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
            new_exercise.add_set(set, fill_values)

        return new_exercise

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "sets": self.sets,
        }

    def add_set(self, set_object: dict, fill_values: bool = False):
        if fill_values:
            pass

        self.sets.append(self.set_type.from_dict(set_object))

    def check_validity(self) -> bool:
        for set in self.sets:
            if not set.check_validity():
                return False
        return True

    def _get_max_from_state(self):
        raise NotImplementedError


class ExerciseWeightsAndRep(Exercise):
    set_type = SetWeightsAndReps
    sets: list[set_type] = []
    reference: str

    def _get_max_from_state(self):
        return exercises_state.get_exercise_max(self.name)
    
    def set_reference(self, exercise_name: str):
        self.reference = exercise_name


exercise_types: dict[str, Type[Exercise]] = {"weights_reps": ExerciseWeightsAndRep}
