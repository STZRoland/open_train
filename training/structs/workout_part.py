from __future__ import annotations
from training.structs.exercise import Exercise
from training.structs.set import Set
from typing import Type


class WorkoutPart:
    exercises: list[Exercise] = []

    def __init__(self, name: str, note: str = ""):
        self.name = name
        self.note = note

    @classmethod
    def from_dict(cls, workout_part_dict: dict) -> WorkoutPart:

        if "WorkoutPart" in workout_part_dict:
            workout_part_dict = workout_part_dict["WorkoutPart"]

        new_workout = cls(
            workout_part_dict.get("name", None),
            workout_part_dict.get("note", None),
        )

        exerccises = workout_part_dict.get("exercises", [])
        for exercise_dict in exerccises:
            new_workout.add_exercise(Exercise.from_dict(exercise_dict))

        return new_workout


    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)
    