from typing import Any


class Set:
    def __init__(self) -> None:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, set_dict: dict):
        raise NotImplementedError

    def update(self, set_dict: dict):
        raise NotImplementedError

    def check_validity(self) -> bool:
        raise NotImplementedError

    def to_dict(self) -> dict[str, Any]:
        raise NotImplementedError


class SetWeightsAndReps(Set):
    def __init__(
        self,
        absolute_intensity: float,
        relative_intensity: float,
        repititions: int,
        weight: float,
    ) -> None:
        self._absolute_intensity = absolute_intensity
        self._relative_intensity = relative_intensity
        self._repititions = repititions
        self._weight = weight

    @classmethod
    def from_dict(cls, set_dict: dict) -> "SetWeightsAndReps":
        if "Set" in set_dict:
            set_dict = set_dict["Set"]
        else:
            raise ValueError("Key 'Set' is not in input.")

        return cls(
            set_dict.get("absolute_intensity", None),
            set_dict.get("relative_intensity", None),
            set_dict.get("repititions", None),
            set_dict.get("weight", None),
        )

    def update(self, set_dict: dict):
        self._absolute_intensity = set_dict.get("absolute_intensity", None)
        self._relative_intensity = set_dict.get("relative_intensity", None)
        self._repititions = set_dict.get("repititions", None)
        self._weight = set_dict.get("weight", None)

    def to_dict(self) -> dict[str, Any]:
        return {"Set": {
            "absolute_intensity": self._absolute_intensity,
            "relative_intensity": self._relative_intensity,
            "repititions": self._repititions,
            "weight": self._weight,
        }}

    def check_validity(self) -> bool:
        if self._repititions is None:
            return False
        if (
            self._absolute_intensity is None
            and self._relative_intensity is None
            and self._weight is None
        ):
            return False
        return True


# There have to be multiple states possible
# 1. Exercise only with Weights and Reps (e.g. accessory stuff)
# 2. Exercise with relative intensity and repititions set (e.g. squats)

# TODO: AMRAP should be an option!
