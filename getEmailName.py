# -*- coding: utf-8 -*-
import re
def name_of_email(addr):
    pattern = r'^(<\w+\s\w+>)\s[a-z]+@\w+\.(com|org)|(\w+)@\w+\.(com|org)$'
    ismatch = re.match(pattern,addr)
    if ismatch:
        name = ismatch.group(1)
        if name:
           return name[1:-1]
        else:
           return ismatch.group(3)
    else:
        return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
