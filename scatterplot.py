import pandas as pd
import matplotlib.pyplot as plt
 
 

data = pd.read_csv("tips.csv")
 

plt.scatter(data['day'], data['tip'])
 

plt.title("Scatter Plot")

plt.xlabel('Day')
plt.ylabel('Tip')
 
plt.show()
