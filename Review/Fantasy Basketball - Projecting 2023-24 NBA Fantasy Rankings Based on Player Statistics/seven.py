from _six import get_top100_reset

top100_reset = get_top100_reset()

print(top100_reset.head(100).to_markdown())
