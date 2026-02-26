print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print("Accessing Storage Vault: ancient_fragment.txt")
try:
    file = open("ancient_fragment.txt", "r")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    data = file.read()
    print(data)
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
