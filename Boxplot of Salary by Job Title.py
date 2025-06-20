if 'salary_usd' in df.columns:
    plt.figure(figsize=(12, 6))
    top_titles = df['job_title'].value_counts().index[:5]
    sns.boxplot(data=df[df['job_title'].isin(top_titles)], x='job_title', y='salary_usd', palette='Set2')
    plt.title("Salary by Top Job Titles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
