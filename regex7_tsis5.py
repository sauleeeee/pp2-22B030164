import re
text = "snake_case_text"
def snake_to_camel(txt):
    tx = re.findall("[a-z]+",text)
    help = ""
    for i in tx:
        help+=i[0].upper()+i[1:len(i)]
    return help
print(snake_to_camel(text))