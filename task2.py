
user_input = input("Enter some data to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

additional_data = input("Enter more data to append: ")

with open("output.txt", "a") as file:
    file.write(additional_data + "\n")


print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
