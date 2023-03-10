import yaml
from open_train.structs.workout import Workout


# Load the test.yaml file into a dictionary
with open("data/test.yaml", "r") as f:
    data = yaml.safe_load(f)

workout = Workout.from_dict(data)

print([p.name for p in workout.parts])
print([e.name for e in workout.parts[0].exercises])
print([e.name for e in workout.parts[1].exercises])

values = workout.parts[0].exercises[0].sets[0].to_dict()["Set"]
print(values["relative_intensity"])
print(values["weight"])
print(values["repititions"])

workout.fill_values()

values = workout.parts[0].exercises[0].sets[0].to_dict()["Set"]
print(values["relative_intensity"])
print(values["weight"])
print(values["repititions"])

new_workout_dict = workout.to_dict()


with open("data/recreated.yaml", "w") as outfile:
    yaml.dump(new_workout_dict, outfile)
