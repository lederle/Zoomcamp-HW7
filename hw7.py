import os

print(f"1) bentoml version: {os.popen('bentoml --version').read().rstrip()}")
print("2) size is 197kb, so best answer is 114kb")

print("3) class UserProfile(BaseModel):\n\tname: str\n\tage: int\n\tcountry: str\n\trating: float\n")
