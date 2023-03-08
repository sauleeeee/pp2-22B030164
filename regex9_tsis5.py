import re
text="HelloworldBeHappy"
tx = re.sub(r"(\w)(\s)+([A-Z])", r"\1 \3",text)
print(tx)