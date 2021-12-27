with open("5_2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for ind, st in enumerate(lines, 1):
        n_words = len(st.split())
        print(f"In line {ind} there are {n_words} words")
