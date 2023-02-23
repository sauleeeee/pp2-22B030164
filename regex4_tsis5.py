import re

txt="HelloWorldBeHappy"
ans=re.findall(r"[A-Z][a-z]+",txt)
print(ans)