# 09-01. REGEX [Lab]
# 03. Match Dates

import re
pattern = r'(?P<day>\d{2})(?P<sep>[\./-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})'
string = input()

dates = re.finditer(pattern, string)

for d in dates:
    date = d.groupdict()
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")
