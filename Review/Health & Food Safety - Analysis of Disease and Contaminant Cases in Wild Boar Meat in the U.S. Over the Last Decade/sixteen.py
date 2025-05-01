from fifteen import get_summary_by_disease

summary_by_disease = get_summary_by_disease()
print(summary_by_disease.to_markdown(index=False))
