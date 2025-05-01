from fourteen import get_specific_freq

specific_freq = get_specific_freq()
summary_by_disease = specific_freq.reset_index()
print(summary_by_disease)
