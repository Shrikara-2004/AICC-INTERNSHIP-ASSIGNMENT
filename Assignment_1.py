import hashlib
import secrets
import getpass
# Function to hash password
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Registration
def register():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    salt = secrets.token_hex(8)   # Generate random salt
    hashed = hash_password(password, salt)
    
    with open("users.txt", "a") as f:
        f.write(f"{username},{salt},{hashed}\n")
    
    print("Registration successful!\n")

# Login
def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    try:
        with open("users.txt", "r") as f:
            for line in f:
                stored_user, salt, stored_hash = line.strip().split(",")
                
                if username == stored_user:
                    hashed = hash_password(password, salt)
                    
                    if hashed == stored_hash:
                        print("Login successful!")
                    else:
                        print("Incorrect password!")
                    return
        
        print("User not found!")
    
    except FileNotFoundError:
        print("No users registered yet.")

# Main
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")