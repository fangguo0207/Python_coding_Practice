import re
t='arrive,YOW'
m = re.match(r'(\w+)\,([A-Z]{3})',t)
print(m.groups())

