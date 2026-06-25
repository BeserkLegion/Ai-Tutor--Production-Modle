"""
IAS AI Tutor — Password Hash Generator
---------------------------------------
Run this script to generate SHA-256 hashes to paste into the
'Password' column of the 'AI Tutor Users' Google Sheet.

Usage:
    python generate_password_hash.py

Enter the plain-text password when prompted.
Copy the output hash into the sheet — never store the plain text.
"""

import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.strip().encode()).hexdigest()

if __name__ == "__main__":
    print("\n── IAS AI Tutor · Password Hash Generator ──\n")
    while True:
        pw = input("Enter password (or 'q' to quit): ").strip()
        if pw.lower() == "q":
            break
        if not pw:
            print("  ⚠️  Password cannot be empty.\n")
            continue
        print(f"  Hash → {hash_password(pw)}\n")
