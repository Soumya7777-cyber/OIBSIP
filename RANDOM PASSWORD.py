import random
import string
# def gen_pass(all_characters,lenth):
#     for _ in range(lenth):
#         password=random.choice(all_characters)
#         print(password,end="")
#     # return password

def generate_password(lenth):
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = uppercase + lowercase + digits + special_characters
    # password=gen_pass(all_characters,lenth)
    password=''.join(random.choice(all_characters) for _ in range(lenth))
    return password
lenth=int(input("Enter the lenth of password:"))
password=generate_password(lenth)
print(password)