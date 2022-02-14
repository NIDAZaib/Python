# %% [markdown]
# #jupyter notebook in vs code
# this is much better then other jupyter notebooks

# %%
print("python ka chilla with baba aammar")

# %% [markdown]
# 1- popup is present in vs but not in jupyter\
# 2- variable show in vs but not in jupyter\
# 3- view variables in seprate data view in vs but not in jpy which gives benefitduring plotting\
# 4- it shows line number in vs but in jpy cell number shows\
# 5- line numbers helps in finding line number of code where error is present\
# 

# %%
aammar = "python ka chilla with baba aammar"
aammar

# %%
import numpy as np
x = np.array([1,2,5,6,7,8,9,5])
x

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

phool = pd.read_csv("Iris.csv")
phool #if we dont write phool here we can also see variable inside variables section

# %%
import pandas as pd
import matplotlib.pyplot as plt
phool = pd.read_csv("Iris.csv")

plt.plot(phool.Id, phool["SepalLengthCm"], "r--")
plt.show


# %%
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)

# %%
pip install seaborn


