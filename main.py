import yaml
from training.structs.exercise import Exercise, ExerciseWeightsAndRep
from training.structs.set import SetWeightsAndReps
from training.structs.workout import Workout
from training.structs.workout_part import WorkoutPart


# Load the test.yaml file into a dictionary
with open('test.yaml', 'r') as f:
    data = yaml.safe_load(f)

workout = Workout.from_dict(data)

test = workout.parts[0].exercises[0]
print(workout.parts[0].exercises[0].sets[0].weight)
print(workout.parts[0].exercises[0].sets[0].repititions)
print(type(workout.parts[0].exercises[0].sets[0]))