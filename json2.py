# json is a language
# takes float > into string for easy transmission > back to float
# every data type > string
# json is a text format

import json

a = json.dumps(5)
print(a)

# dumps turns it into a string >  converts indicated value into json
print(json.dumps([1,2,3,4]))

