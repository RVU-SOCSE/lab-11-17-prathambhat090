
#Lab 12: Outlier Detection: 
#A) Visualize outliers using box plot from Matplotlib and Seaborn 
#B) Identify outliers in datasets using Pandas DataFrame and Interquartile Range (IQR)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset\")
df = pd.read_csv("exp1.csv")
print("Dataset:")
print(df)


# Matplotlib Boxplot - Screen

print("\nBoxplot for Screen Size")

plt.boxplot(df["Screen"], notch=True, vert=False, showmeans=True)
plt.xlabel("Screen")
plt.title("Boxplot - Screen Size")
plt.show()


# Matplotlib Boxplot - Weight
# -------------------------------
print("\nBoxplot for Weight")

plt.boxplot(df["Weight"])
plt.ylabel("Weight")
plt.title("Boxplot - Weight")
plt.show()


# Seaborn Boxplot
# -------------------------------
print("\nSeaborn Boxplot for Weight")

sns.boxplot(x=df["Weight"])
plt.title("Seaborn Boxplot - Weight")
plt.show()

print("\nSeaborn Boxplot - Weight vs RAM")

sns.boxplot(x=df["Weight"], y=df["RAM"])
plt.title("Weight vs RAM")
plt.show()


# IQR Method
# -------------------------------
print("\nIQR Method Calculation")

Q1 = df["Weight"].quantile(0.25)
Q3 = df["Weight"].quantile(0.75)

print("Q1:", Q1)
print("Q3:", Q3)

IQR = Q3 - Q1
print("IQR:", IQR)

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Lower Bound:", lower)
print("Upper Bound:", upper)

# Outliers
outliers = df[(df["Weight"] < lower) | (df["Weight"] > upper)]

print("\nOutliers in Weight:")
print(outliers)