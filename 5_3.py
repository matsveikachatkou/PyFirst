with open("5_3.txt", "r", encoding="utf-8") as file:
    worker_dict = {line.split()[0]: float(line.split()[1]) for line in file}
    for key, value in worker_dict.items():
        if value <= 20000:
            print(f"{key} has low salary")
    average = sum(worker_dict.values()) / len(worker_dict)
    print(f"Average salary is: {average}")
