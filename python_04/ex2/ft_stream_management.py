import sys


print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
archivist_ID = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")
print("\n{[}STANDARD{]} Archive status from" +
      f" {archivist_ID}: {status_report}", file=sys.stdout)
print("{[}ALERT{]} System diagnostic:" +
      " Communication channels verified", file=sys.stderr)
print("{[}STANDARD{]} Data transmission complete\n")
print("Three-channel communication test successful.")
