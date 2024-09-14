import csv

# Writing to a csv file
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Name","Age","Country"])
    # Write rows
    writer.writerow(["Dharak","22","Berlin"])
    writer.writerow(["Nevil","23","Surat"])
    writer.writerow(["Yash","21","Rajkot"])

print("CSV file written successfully.")

# Reading from a CSV file
with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)