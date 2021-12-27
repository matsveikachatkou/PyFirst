with open("5_1.txt", "w", encoding="utf-8") as file:
    while True:
        line = input("Please write new line: ")
        if line == "":
            break
        file.write(f"{line}\n")

