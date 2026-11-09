from pathlib import Path


# path.parents[0] это то же самое, что и path.parent
print(f"Первый родитель: {Path.parents[0]}") # /home/user/project
print(f"Второй родитель: {Path.parents[1]}")  # /home/user
