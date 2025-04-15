from first import get_text

def get_text_lines():
    text = get_text()
    return text.strip().split('\n')

if __name__ == "__main__":
    text_lines = get_text_lines()
    print(len(text_lines), text_lines[:10])
