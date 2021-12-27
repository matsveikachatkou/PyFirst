with open("5_2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for ind, text in enumerate(lines, 1):
        n_words = len(text.split())
        print(f"In line {ind} there are {n_words} words")
