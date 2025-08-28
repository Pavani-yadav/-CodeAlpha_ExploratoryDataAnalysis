 # ==========================
# Task 3: Data Visualization
# ==========================

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset (directly from CSV in the same folder)
df = pd.read_csv("StudentsPerformance.csv")
print(df.head())

# 3. Visualization Settings
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# ==========================
# Univariate Visualizations
# ==========================

# Distribution of Math Scores
sns.histplot(df["math score"], bins=20, kde=True, color="blue")
plt.title("Distribution of Math Scores")
plt.show()

# Distribution of Reading Scores
sns.histplot(df["reading score"], bins=20, kde=True, color="green")
plt.title("Distribution of Reading Scores")
plt.show()

# Distribution of Writing Scores
sns.histplot(df["writing score"], bins=20, kde=True, color="red")
plt.title("Distribution of Writing Scores")
plt.show()

# ==========================
# Categorical Comparisons
# ==========================

# Gender vs Math Score
sns.barplot(x="gender", y="math score", data=df, ci=None)
plt.title("Math Scores by Gender")
plt.show()

# Gender vs Reading Score
sns.barplot(x="gender", y="reading score", data=df, ci=None)
plt.title("Reading Scores by Gender")
plt.show()

# Gender vs Writing Score
sns.barplot(x="gender", y="writing score", data=df, ci=None)
plt.title("Writing Scores by Gender")
plt.show()

# ==========================
# Bivariate Visualizations
# ==========================

# Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Scores")
plt.show()

# Scatter Plot Math vs Reading
sns.scatterplot(x="math score", y="reading score", hue="gender", data=df)
plt.title("Math vs Reading Scores by Gender")
plt.show()

# Scatter Plot Math vs Writing
sns.scatterplot(x="math score", y="writing score", hue="gender", data=df)
plt.title("Math vs Writing Scores by Gender")
plt.show()

# ==========================
# Category-wise Comparisons
# ==========================

# Writing Scores by Parental Education
sns.boxplot(x="parental level of education", y="writing score", data=df)
plt.xticks(rotation=45)
plt.title("Writing Scores by Parental Education")
plt.show()

# Reading Scores by Parental Education
sns.boxplot(x="parental level of education", y="reading score", data=df)
plt.xticks(rotation=45)
plt.title("Reading Scores by Parental Education")
plt.show()

# Math Scores by Race/Ethnicity
sns.boxplot(x="race/ethnicity", y="math score", data=df)
plt.title("Math Scores by Race/Ethnicity")
plt.show()
