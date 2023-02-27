import yaml
from training.structs.workout import Workout


# Load the test.yaml file into a dictionary
with open('test.yaml', 'r') as f:
    data = yaml.safe_load(f)

workout = Workout.from_dict(data)

print(workout.parts[0].exercises[0].sets[0].weight)
print(workout.parts[0].exercises[0].sets[0].repititions)
print(type(workout.parts[0].exercises[0].sets[0]))
