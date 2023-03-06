import polars as pl
from pathlib import Path


def _read_csv_state() -> pl.DataFrame:
    if not exercise_csv_path.is_file():
        exercises_df = pd.DataFrame({"exercise": [], "max": []}).to_csv(
            exercise_csv_path
        )
    exercises_df = pd.DataFrame(pd.read_csv(exercise_csv_path))

    return exercises_df


class ExercisesState(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ExercisesState, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.exercise_df = _read_csv_state()
        assert "exercise" in self.exercise_df.columns
        assert "max" in self.exercise_df.columns

    def get_exercise_max(self, exercise_name: str):
        # df_row = self.exercise_df[self.exercise_df["exercise"].str.match(exercise_name)]
        df_row = self.exercise_df.filter(pl.col("exercise") == exercise_name)

        if df_row is not None:
            return df_row["max"]
        else:
            return None


exercise_csv_path = Path("exercises.csv")
exercises_state = ExercisesState()
