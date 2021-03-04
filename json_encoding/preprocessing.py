import re

def remove_dots(value: str):
  if (value is not None and isinstance(value, str)):
    c1=re.compile(r'^(\..)+$') #for checking if dot is at odd places in the input: .T.h.i.s
    c2=re.compile(r'^(.\.)+$') #for checking if dot is at even places in the input: T.h.i.s.
    if (bool(c1.match(value))):
      s=[d for i, d in enumerate(list(value)) if (i%2!=0)] #retain odd index .T.h.i.s -> This
      value=''.join(s)
    elif (bool(c2.match(value))):
      s=[d for i, d in enumerate(list(value)) if (i%2==0)] #retain even index T.h.i.s. -> This
      value=''.join(s)
    return value
  else:
    return value

def remove_escape_chars(value: str):
  if (value is not None and isinstance(value, str) and value!="" and value[0]=='\"' and value[-1]=='\"'):
    value=value[1:]
    value=value[:-1]
  return value

def cleaning(dict):
  for key, value in dict['properties'].items():
    value=remove_escape_chars(value)
    value=remove_dots(value)
    dict['properties'].update({key: value})
  dict['properties'].pop('out-of-service', None)
  return dict #return for test case

def start_cleaning(data):
  for keys, values in data['objects'].items():
    print('---processing values of '+keys+'---')
    for i in range(len(values)):
      cleaning(values[i])
  return data
