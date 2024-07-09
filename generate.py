#!/usr/bin/env python3

with open("words.txt", "r") as file:
    words = file.read().splitlines()

years = range(2000, 2025)
generated = []
custom_word = input("Enter a custom word to include or leave empty: ").strip()

for word in words:
    variations = [word.lower(), word.upper(), word.title()]
    generated.extend(variations)

    for year in years:
        for variation in variations:
            generated.append(str(year) + variation)
            generated.append(variation + str(year))

    if custom_word:
        for variation in variations:
            generated.append(custom_word + variation)
            for year in years:
                generated.append(custom_word + str(year) + variation)
                generated.append(custom_word + variation + str(year))
                generated.append(str(year) + custom_word + variation)
                generated.append(variation + custom_word + str(year))

with open("fuzz.txt", "w") as file:
    for word in generated:
        file.write(word + "\n")

for word in generated:
    print(word)
