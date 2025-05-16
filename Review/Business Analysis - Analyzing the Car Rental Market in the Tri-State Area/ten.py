from _six import get_html_ny

html_ny = get_html_ny()
print(any(kw in html_ny.lower() for kw in ["$","starting from","per day"]))
