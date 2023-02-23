import re

txt="hello_world_be_happy"
ans=re.findall(r"[a-z]_[a-z]",txt)
print(ans)