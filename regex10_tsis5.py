import re
text="camelCaseText"
def camel_to_snake(text):
        str1 = re.sub('(.)([A-Z]+)', r'\1_\2', text)
        return str1.lower()
print(camel_to_snake(text))
