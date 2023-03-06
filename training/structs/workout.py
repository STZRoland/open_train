from __future__ import annotations
from typing import Any
from ..structs.workout_part import WorkoutPart


class Workout:
    def __init__(self, id: int, name: str, note: str = ""):
        self.id = id
        self.name = name
        self.note = note
        self.parts: list[WorkoutPart] = []

    @classmethod
    def from_dict(cls, workout_dict: dict, fill_values: bool = False) -> Workout:
        id = 0

        new_workout = cls(
            id,
            workout_dict.get("name", None),
            workout_dict.get("note", None),
        )

        parts = workout_dict.get("parts", [])
        for workout_part_dict in parts:
            new_workout.add_workout_part(
                WorkoutPart.from_dict(workout_part_dict, fill_values)
            )

        return new_workout

    def add_workout_part(self, workout_part: WorkoutPart):
        self.parts.append(workout_part)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "note": self.note,
            "parts": self.parts,
        }
