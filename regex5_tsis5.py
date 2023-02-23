import re
txt="achtotobeshechtoto"
ans=re.findall(r"a.*b",txt)
print(ans)