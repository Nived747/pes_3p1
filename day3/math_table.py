# Accept a number from the user and print its math table for multiple upto 20

import sys 

input_number = int(sys.argv[1])

for i in range(1, 21):
    #print(input_number, '*', i, '=', input_number * i)
    #print(f'{input_number} * {i} = {input_number * i}')
    print('%2d * %2d = %3d' % (input_number, i, (input_number * i)))