# Task 2: File Writing and Appending

try:
    text = input("Enter anything to add into file: ")

    # 'a' means append mode 
    # 'w' means write mode 
    with open("sample.txt", "a") as file:
        file.write(text + "\n")

    print("Data added successfully.")

except Exception as e:
    print("Error occurred:", e)