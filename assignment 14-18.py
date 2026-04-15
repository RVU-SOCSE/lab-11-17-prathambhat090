import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create Dataset
data = {
    'Salary': [50000, 60000, 75000, 80000, 120000, 95000, 40000, 70000]
}
df = pd.DataFrame(data)

# Histogram Plot
sns.histplot(df['Salary'], kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()


# Create Dataset
data = {
    'Salary': [50000, 60000, 75000, 80000, 120000, 95000, 40000, 70000],
    'Years_Experience': [1, 2, 3, 4, 5, 6, 1.5, 3.5]
}
df = pd.DataFrame(data)

# Pair Plot
sns.pairplot(df)
plt.show()



# Create Dataset
data = {
    'Salary': [50000, 60000, 75000, 80000, 120000, 95000, 40000, 70000],
    'Years_Experience': [1, 2, 3, 4, 5, 6, 1.5, 3.5]
}
df = pd.DataFrame(data)

# Correlation Heatmap
corr = df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()




# Create Dataset
data = {
    'Salary': [50000, 60000, 75000, 80000, 120000, 95000, 40000, 70000],
    'Years_Experience': [1, 2, 3, 4, 5, 6, 1.5, 3.5]
}
df = pd.DataFrame(data)

# Line Plot
sns.lineplot(x='Years_Experience', y='Salary', data=df, marker='o')
plt.title("Salary Trend by Experience")
plt.show()

# Scatter Plot
sns.scatterplot(x='Years_Experience', y='Salary', data=df, s=100)
plt.title("Salary vs Experience")
plt.show()


# Create Dataset
data = {
    'Salary': [50000, 60000, 75000, 80000, 120000, 95000, 40000, 70000],
    'Experience_Level': ['Junior', 'Junior', 'Mid', 'Mid', 'Senior', 'Senior', 'Junior', 'Mid']
}
df = pd.DataFrame(data)

# Bar Plot
sns.barplot(x='Experience_Level', y='Salary', data=df)
plt.title("Salary by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Salary")
plt.show()