import re
text = "snake_case_text"
def snake_to_camel(txt):
    tx = re.findall("[a-z]+",text)
    help =""
    for i in range(0,len(tx)):
        if i==0:
            help+=tx[i]
        else:
            help+=tx[i][0].upper()+tx[i][1:len(tx[i])]
    return help
print(snake_to_camel(text))
