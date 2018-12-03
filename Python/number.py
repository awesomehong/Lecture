import re

data = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3})[-](\d{4})[-]\d{4}")
print(pat.sub("\g<1>-\g<2>-####", data))