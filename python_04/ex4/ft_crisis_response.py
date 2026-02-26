print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open("lost_archive.txt", "r") as file:
        print("success")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
print("STATUS: Crisis handled, system stable\n")
print("CRISIS ALERT: Attempting access to 'classified_data.txt'...")
try:
    with open("classified_data.txt", "w") as file:
        print("success")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
print("STATUS: Crisis handled, security maintained\n")
print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
try:
    with open("standard_archive.txt", "r") as file:
        data = file.read()
        print(f"SUCCESS: Archive recovered - ``{data}''")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
print("STATUS: Normal operations resumed\n")
print("All crisis scenarios handled successfully. Archives secure.")
