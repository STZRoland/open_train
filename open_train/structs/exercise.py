from __future__ import annotations
from typing import Any, Type

from open_train.functions.weights_and_reps import calc_missing_values
from ..structs.set import Set, SetWeightsAndReps
from ..state.exercises_state import exercises_state


class Exercise:
    # Potential alternative name: Movmement
    set_type = Set

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.max = self._get_max_from_state()

        self.sets: list[Set] = []

    @classmethod
    def from_dict(cls, exercise_dict: dict) -> Exercise:
        # if "Exercise" in exercise_dict:
        #     exercise_dict = exercise_dict["Exercise"]

        id = 0
        exercise_type_str = exercise_dict.get("type", "")

        new_exercise = exercise_types[exercise_type_str](
            id,
            exercise_dict.get("name", None),
        )

        sets = exercise_dict.get("sets", [])
        sets = [s["Set"] for s in sets if "Set" in s.keys()]

        for set in sets:
            new_exercise.add_set(set)

        return new_exercise

    def fill_values(self):
        for s in self.sets:
            values = calc_missing_values(s.to_dict(), self.max)
            s.update(values)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "sets": self.sets,
        }

    def add_set(self, set_object: dict):
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
        return int(exercises_state.get_exercise_max(self.name).item())

    def set_reference(self, exercise_name: str):
        self.reference = exercise_name


exercise_types: dict[str, Type[Exercise]] = {"weights_reps": ExerciseWeightsAndRep}
