import re
txt ="jfkdshabbabbblkjfsdabb"
ans=re.findall(r"ab{2,3}",txt)
print(ans)