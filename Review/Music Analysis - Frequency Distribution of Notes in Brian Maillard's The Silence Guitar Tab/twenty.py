def parse_fret_numbers(num_str):
    i=0
    numbers=[]
    while i < len(num_str):
        c=num_str[i]
        if i < len(num_str)-1 and c in '12':  # start of 2-digit
            candidate=int(num_str[i:i+2])
            if candidate <= 24:  # typical max fret
                numbers.append(candidate)
                i += 2
                continue
        # otherwise 1 digit
        numbers.append(int(c))
        i += 1
    return numbers

all_frets=[]
numbers =  ['70',
  '6',
  '4',
  '3',
  '4',
  '78',
  '5',
  '4',
  '1215172015',
  '15',
  '15',
  '1118',
  '17151715',
  '8',
  '781908712',
  '1344',
  '7',
  '2',
  '5',
  '5']
for ns in numbers:
    frets=parse_fret_numbers(ns)
    all_frets.extend(frets)
print(len(all_frets), all_frets[:20])
