# Module: Files and Exception Handling
# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to output.txt
text_to_write = input("Enter text to write to the file: ")

# Open the file in write mode
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")

print("Data successfully written to output.txt.")

# Step 2: Take additional input and append it to the same file
text_to_append = input("Enter additional text to append: ")

# Open the file in append mode
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")

print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())