
que=['1.which language frequently used in japan?', 'japanese','punjabi','hindi','english']
i=0
money=0
for i in range(0,1):
    print(que[i])
    print('\t\t\t\tpress any key to continue...')
    b=input()
    print('a.',que[1],'\t\t\t','b.',que[2],'\t\t\t','\n','c.',que[3],'\t\t\t','d.',que[4])
    choose=int(input('enter your choice(1-4)\n'))
    if (choose==1):
        print("you are right")
        money=1000
        print('your winning price is :',money)
    else:
        print("better luck next time")
        money=0
        print('your Balance is :',money)

print('\t\t\t-x-x-x-x-x-x-x-x-x')

print("\t\t\t\tMoving to the next question....")



que1=['2.which language frequently used in india?', 'japanese','punjabi','hindi','english ']
i=0
money1=0
for i in range(0,1):
    print(que1[i])
    print('\t\t\t\tpress any key to continue...')
    b=input()
    print('a.',que1[1],'\t\t\t','b.',que1[2],'\t\t\t','\n','c.',que1[3],'\t\t\t','d.',que1[4])
    choose=int(input('enter your choice(1-4)\n'))
    if (choose==3):
        print("you are right")
        money1=1000+money
        print('your winning price is :',money1)
    else:
        print("better luck next time")
        money1=0+money
        print('your Balance is :',money1)
