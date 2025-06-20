if 'salary_usd' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['salary_usd'].dropna(), kde=True, color='teal')
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
