# Task 1: File Reading with Error Handling

file = None
try:
    # 'r' means read mode
    file = open("sample.txt", "r")
    print("Reading file line by line:\n")

    # reading file using for loop
    for line in file:
        print(line.strip())
except FileNotFoundError:
    print("File not found. Please check if sample.txt exists.")
except Exception as e:
    print("Some error occurred:", e)
finally:
    # finally block runs whether error occurs or not
    if file is not None:
        file.close()
        print("\nFile closed.")