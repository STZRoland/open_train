from __future__ import annotations
from typing import Any
from ..structs.exercise import Exercise


class WorkoutPart:
    exercises: list[Exercise] = []

    def __init__(self, name: str, note: str = ""):
        self.name = name
        self.note = note

    @classmethod
    def from_dict(
        cls, workout_part_dict: dict, fill_values: bool = False
    ) -> WorkoutPart:
        if "WorkoutPart" in workout_part_dict:
            workout_part_dict = workout_part_dict["WorkoutPart"]

        new_workout = cls(
            workout_part_dict.get("name", None),
            workout_part_dict.get("note", None),
        )

        exerccises = workout_part_dict.get("exercises", [])
        for exercise_dict in exerccises:
            new_workout.add_exercise(Exercise.from_dict(exercise_dict, fill_values))

        return new_workout

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "note": self.note,
            "exercises": self.exercises,
        }
