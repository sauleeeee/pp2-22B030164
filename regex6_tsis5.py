import re

txt="hello world,be happy."
ans=re.sub("[ .,]",";",txt)
print(ans)