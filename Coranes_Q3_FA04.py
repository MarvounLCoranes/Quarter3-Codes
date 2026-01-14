import numpy as np

names = ["Marvoun", "Aston", "Jane"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

total_steps = steps.sum(axis=1)
print("Total steps per person:")
for i in range(len(names)):
    print(names[i], ":", total_steps[i])
max_index = np.argmax(total_steps)
print("Person with the highest total steps:")
print(names[max_index], ": ", total_steps[max_index], "steps")
difference = total_steps.max() - total_steps.min()
print("Difference between highest and lowest total steps:", difference)