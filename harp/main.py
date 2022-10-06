from glob import glob
from operator import le


input_str = input()

input_list = list(input_str)
collector = {
    'collecting': "chars",
    'letters': "",
    'sign': "",
    'number': ""
}

global parsed_instructions
parsed_instructions = []

for c in input_list:
    if collector['collecting'] == "chars":
        if c == "+" or c == "-":
            collector['sign'] = c
            collector['collecting'] = "nums"
        else:
            collector['letters'] += c
    else:
        if not c.isdigit():
            parsed_instructions.append({
                'letters': collector['letters'],
                'sign': collector['sign'],
                'number': collector['number']
            })
            collector['letters'] = c
            collector['sign'] = ""
            collector['number'] = ""
            collector['collecting'] = "chars"
        else:
            collector['number'] += c

parsed_instructions.append({
    'letters': collector['letters'],
    'sign': collector['sign'],
    'number': collector['number']
})
collector['letters'] = c
collector['sign'] = ""
collector['number'] = ""
collector['collecting'] = "chars"


for i in parsed_instructions:
    if(i['sign'] == "-"):
        print(i['letters'], 'loosen', i['number'])
    else:
        print(i['letters'], 'tighten', i['number'])

