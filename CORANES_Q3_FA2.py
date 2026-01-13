import numpy as np

names = ["Marvoun", "Aston", "Jane"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4100, 6200, 4300, 5400, 5500],  # Marvoun's
    [4000, 4100, 3200, 4300, 4600],  # Aston's
    [6000, 5800, 5200, 6100, 6700]   # Jane's
])

print("Daily steps (Monday to Friday):")
for i in range(len(names)):
    print(names[i], ":", steps[i])

