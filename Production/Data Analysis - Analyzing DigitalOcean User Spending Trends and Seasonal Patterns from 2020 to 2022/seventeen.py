from fifteen import get_yearly_avg_table

def get_yearly_avg_markdown():
    yearly_avg_table = get_yearly_avg_table()
    return yearly_avg_table.to_markdown(index=False)

if __name__ == "__main__":
    yearly_avg_markdown = get_yearly_avg_markdown()
    print(yearly_avg_markdown[:500])
