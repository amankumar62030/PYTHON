# WAP to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 - year old.

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"

    # Use a raw string for the file path or double the backslashes
    with open(f"D:\\PYTHON\\practiceSet\\tables\\table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)

print("Multiplication tables generated successfully!")
