def find_lines(filepath, query):
    with open(filepath, "r", encoding="utf-8") as file:
       for line in (line for line in file if query.lower() in line.lower()):
            yield line.strip()


if __name__ == "__main__":
    gen = find_lines("notes.txt", "python")
    for i in gen:
        print(i)
