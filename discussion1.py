# Rolling one die, 1000 times

import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# list to the save results
results = []

# loop
for i in range(1000):
    # random selection from 1 to 6
    roll = random.choice(range(6)) + 1    
    # add random choice to list
    results.append(roll)

# print average of all rolls
print('Average of rolls: ', sum(results) / len(results))


# summarize results
throws = pd.Series(data = results)
die = []
counts = []

for i in range(6):    
    face = i + 1
    die.append(face)
    counts.append(sum(throws == face))


df = pd.DataFrame(list(zip(die, counts)), columns = ['face', 'counts'])

# plot
sns.barplot(x = 'face', y = 'counts', data = df)
plt.show()