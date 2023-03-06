import yaml
from training.structs.workout import Workout


# Load the test.yaml file into a dictionary
with open("data/test.yaml", "r") as f:
    data = yaml.safe_load(f)

workout = Workout.from_dict(data)

values = workout.parts[0].exercises[0].sets[0].to_dict()
# print(values["relative_intensity"])
# print(values["weight"])
# print(values["repititions"])

new_workout = workout.to_dict()
# print(new_workout.keys())
# print(new_workout["parts"])


with open("data/recreated.yaml", "w") as outfile:
    yaml.dump(data, outfile)
