temp_data = []
elf_calories = []

with open("AoC22-Day1-Text.txt") as data:
# with open("AoC22-Day1-Text.txt") as elf_calories:
    data = data.read().split("\n")
    for calories in data:
        if calories == "":
            # Finds sum of current list
            elf_calories.append(sum(temp_data))
            # Then clears the list and restarts it
            temp_data.clear()
        else:
            temp_data.append(int(calories))
    if len(temp_data) != 0:
        elf_calories.append(sum(temp_data))
max_calories = max(elf_calories)

elf_calories.sort(reverse=True)
print(sum(elf_calories[:3]))