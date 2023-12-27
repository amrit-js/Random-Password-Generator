import random
import string
x = int(input("Enter the length of Password: "))
def generate_password(length=x):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

random_password = generate_password()
print("Random Password:", random_password)
