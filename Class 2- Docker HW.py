import os
import getpass

user = os.environ.get("USERNAME") or os.environ.get("USER") or getpass.getuser()

print(user)