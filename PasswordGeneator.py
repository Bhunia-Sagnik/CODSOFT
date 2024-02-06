import random
import string

n=int(input("Enter the length of the required password: "))
password="".join(random.choice(string.ascii_letters + string.digits) for x in range(n))
print("Generated password is: ", password)