PLACEHOLDER = "[Name]"

with open("Invitations.txt") as invite:
    names = invite.readlines()
    print(names)

with open("letter_sample.txt") as letters:
    letter = letters.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)

        with open(f"Letter for {stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
