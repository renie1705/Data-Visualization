# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load your dataset
df = pd.read_csv('/content/ai_job_dataset.csv')

# Step 3: Basic data check
print("Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nInfo:\n")
df.info()
print("\nMissing values:\n", df.isnull().sum())

# Step 4: Summary statistics
print("\nSummary Statistics:\n", df.describe(include='all'))

# Step 5: Categorical column visualization (e.g., job roles)
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='job_title', order=df['job_title'].value_counts().index[:10], palette="viridis")
plt.title("Top 10 AI Job Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: Distribution of Salary (if exists)
if 'salary_usd' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['salary_usd'].dropna(), kde=True, color='teal')
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Step 7: Boxplot of Salary by Job Title (if available)
if 'salary_usd' in df.columns:
    plt.figure(figsize=(12, 6))
    top_titles = df['job_title'].value_counts().index[:5]
    sns.boxplot(data=df[df['job_title'].isin(top_titles)], x='job_title', y='salary_usd', palette='Set2')
    plt.title("Salary by Top Job Titles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 8: Heatmap for numerical correlation
numeric_cols = df.select_dtypes(include=['int64', 'float64'])
if not numeric_cols.empty:
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
