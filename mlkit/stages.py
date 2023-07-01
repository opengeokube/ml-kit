"""Module with stages utils."""
from enum import Enum


class Stage(Enum):
    """ML procedure stages."""

    TRAIN = "train"
    VALIDATION = "val"
    TEST = "test"
    PREDICT = "predict"

    def __str__(self) -> str:
        return self.value
