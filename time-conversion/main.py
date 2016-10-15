#!/bin/python3

time = input().strip()
if time[:2] == '12':
    if time[-2:] == 'AM':
        output = ''.join(('00', time[2:-2]))
    else:
        output = time[:-2]

elif time[-2:] == 'AM':
    output = time[:-2]
else:
    hours = int(time.split(sep=':')[0]) + 12
    output = ''.join((str(hours), time[2:-2]))

print(output)
