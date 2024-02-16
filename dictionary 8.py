import random
import string
password_length = 30
use_lowercase = True
use_uppercase = True
use_digits = True
use_symbols = True
characters = ''
if use_lowercase:
    characters += string.ascii_lowercase
if use_uppercase:
    characters += string.ascii_uppercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))
print(f"Generated password: {password}")