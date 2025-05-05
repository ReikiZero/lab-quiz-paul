import datetime

# Print personal information
full_name = "Paul Smith"       # Replace with your full name
student_id = "12345678"        # Replace with your student ID

current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Full Name:", full_name)
print("Student ID:", student_id)
print("Date & Time:", current_datetime)

# Prompt for networking issue
issue = input("Describe a networking issue you're experiencing: ")

# Save to file
with open("network_issue.txt", "w") as file:
    file.write(f"Networking Issue: {issue}\n")
