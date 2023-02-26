
from typing import Optional, Union


class Set:
    def __init__(self) -> None:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, set_dict: dict):
        raise NotImplementedError

    def check_validity(self) -> bool:
        raise NotImplementedError


class SetWeightsAndReps(Set):
    def __init__(self, absolute_intensity: float, relative_intensity: float, repititions: int, 
            weight: int) -> None:
        self.absolute_intensity = absolute_intensity
        self.relative_intensity = relative_intensity
        self.repititions = repititions
        self.weight = weight

    @classmethod
    def from_dict(cls, set_dict: dict) -> 'SetWeightsAndReps':
        return cls(
            set_dict.get("absolute_intensity", None),
            set_dict.get("relative_intensity", None),
            set_dict.get("repititions", None),
            set_dict.get("weight", None)
        )
        
    def check_validity(self) -> bool:
        if self.repititions is None:
            return False
        if self.absolute_intensity is None and self.relative_intensity is None and self.weight is None:
            return False
        return True

    
# There have to be multiple states possible
# 1. Exercise only with Weights and Reps (e.g. accessory stuff)
# 2. Exercise with relative intensity and repititions set (e.g. squats)

# TODO: AMRAP should be an option!
