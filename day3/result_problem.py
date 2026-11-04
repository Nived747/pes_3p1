'''
Accept average score from the student and print the result as follows:
0  to 49  Fail
50 to 69  SC
70 to 89  FC
90 to 100 E/D
Also check for invalid score
'''
average_score = float(input('Enter your average score to print the result: '))

if average_score <= 49:
    print('Fail')
elif average_score <= 69:
    print('SC')
elif average_score <= 89:     
    print('FC')
elif average_score <= 100:
    print('E/D')
else: 
    print('Invalid score')