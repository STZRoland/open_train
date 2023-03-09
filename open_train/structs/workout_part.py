from __future__ import annotations
from typing import Any
from ..structs.exercise import Exercise


class WorkoutPart:

    def __init__(self, name: str, note: str = ""):
        self.exercises: list[Exercise] = []
        self.name = name
        self.note = note

    @classmethod
    def from_dict(cls, workout_part_dict: dict) -> WorkoutPart:
        # if "WorkoutPart" in workout_part_dict:
        #     workout_part_dict = workout_part_dict["WorkoutPart"]
        
        new_workout_part = cls(
            workout_part_dict.get("name", None),
            workout_part_dict.get("note", None) + "test",
        )

        exercises = workout_part_dict.get("exercises", [])
        exercises = [e["Exercise"] for e in exercises if "Exercise" in e.keys()]

        for exercise_dict in exercises:
            new_workout_part.add_exercise(Exercise.from_dict(exercise_dict))

        print([e.name for e in new_workout_part.exercises])
        return new_workout_part

    def fill_values(self):
        for e in self.exercises:
            e.fill_values()

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "note": self.note,
            "exercises": self.exercises,
        }
