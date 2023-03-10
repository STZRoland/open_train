from __future__ import annotations
from typing import Any, Optional
from ..structs.workout_part import WorkoutPart


class Workout:
    def __init__(
        self,
        id: int,
        name: str,
        note: str = "",
        week: Optional[int] = None,
        day: Optional[int] = None,
        recorded: Optional[bool] = False,
    ):
        self.id = id
        self.name = name
        self.note = note
        self.week = week
        self.day = day
        self.recorded = recorded

        self.parts: list[WorkoutPart] = []

    @classmethod
    def from_dict(cls, workout_dict: dict) -> Workout:
        id = 0

        new_workout = cls(
            id,
            workout_dict.get("name", None),
            workout_dict.get("note", None),
            workout_dict.get("week", None),
            workout_dict.get("day", None),
            workout_dict.get("recorded", False)
        )

        parts = workout_dict.get("parts", [])
        # parts = [p["WorkoutPart"] for p in parts if "WorkoutPart" in p.keys()]

        for workout_part_dict in parts:
            try:
                new_workout.add_workout_part(WorkoutPart.from_dict(workout_part_dict))
            except ValueError as e:
                print(e)

        return new_workout

    def fill_values(self):
        for p in self.parts:
            p.fill_values()

    def add_workout_part(self, workout_part: WorkoutPart):
        self.parts.append(workout_part)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "note": self.note,
            "week": self.week,
            "day": self.day,
            "recorded": self.recorded,
            "parts": [p.to_dict() for p in self.parts],
        }
