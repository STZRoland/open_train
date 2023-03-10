from __future__ import annotations
from typing import Any, Optional, Type

from open_train.functions.weights_and_reps import calc_missing_values
from ..structs.set import Set, SetWeightsAndReps
from ..state.exercises_state import exercises_state


class Exercise:
    # Potential alternative name: Movmement
    set_type = Set

    def __init__(self, id: int, name: str, exercise_type: Optional[str] = None, **kwargs):
        self.id = id
        self.name = name
        # self.max = self._get_max_from_state()
        self.exercise_type = exercise_type

        self.sets: list[Set] = []
        self._post_init()

    def _post_init(self):
        # Can be changed by subclass to perform operations in the __init__() method
        pass

    @classmethod
    def from_dict(cls, exercise_dict: dict) -> Exercise:
        if "Exercise" in exercise_dict:
            exercise_dict = exercise_dict["Exercise"]
        else:
            raise ValueError("Key 'Exercise' is not in input.")

        id = 0
        exercise_type_str = exercise_dict.get("type", "")
        name = exercise_dict.get("name", None)
        if name == None:
            raise ValueError("You must provide a name for the exercise!")

        exercise_dict.pop("name")
        exercise_dict.pop("type")

        new_exercise = exercise_types[exercise_type_str](
            id, name, exercise_type_str, **exercise_dict
        )

        sets = exercise_dict.get("sets", [])
        # sets = [s["Set"] for s in sets if "Set" in s.keys()]

        for set in sets:
            try:
                new_exercise.add_set(set)
            except ValueError as e:
                print(e)

        return new_exercise


    def to_dict(self) -> dict[str, Any]:
        return {
            "Exercise": {
                "id": self.id,
                "name": self.name,
                "type": self.exercise_type,
                "sets": [s.to_dict() for s in self.sets],
            }
        }

    def add_set(self, set_object: dict):
        self.sets.append(self.set_type.from_dict(set_object))

    def check_validity(self) -> bool:
        for set in self.sets:
            if not set.check_validity():
                return False
        return True
    
    def fill_values(self):
        raise NotImplementedError

    def _get_max_from_state(self):
        raise NotImplementedError


class ExerciseWeightsAndRep(Exercise):
    set_type = SetWeightsAndReps

    def __init__(self, id: int, name: str, exercise_type: Optional[str] = None, **kwargs):
        super().__init__(id, name, exercise_type)
        test = kwargs.get("reference", None)
        self.reference_exercise_name = kwargs.get("reference", None)

    def set_reference(self, exercise_name: str):
        self.reference = exercise_name

    def fill_values(self):
        if self.reference_exercise_name is None:
            max_value = exercises_state.get_exercise_max(self.name)
        else:
            max_value = exercises_state.get_exercise_max(self.reference_exercise_name)
    
        print(f"Max: {max_value}")
        print(self.reference_exercise_name)

        for s in self.sets:
            test = s.to_dict()
            values = calc_missing_values(s.to_dict()["Set"], max_value)
            s.update(values)

        
exercise_types: dict[str, Type[Exercise]] = {
    "weights_reps": ExerciseWeightsAndRep,
    "": Exercise,
}
