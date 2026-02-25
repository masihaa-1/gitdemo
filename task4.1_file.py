# Task 4.1 - Read a file and display its content

try:
    with open("SAMPLE.txt", "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("File not found. Please check the filename.")

except Exception as e:
    print("Error:", e)