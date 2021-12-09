time = int(input("Please enter time (in seconds): "))
hours = time // 3600
minutes_base = time % 3600
minutes = minutes_base // 60
seconds = time % 60
print(f"{hours:}:{minutes}:{seconds}")
