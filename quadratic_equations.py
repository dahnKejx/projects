from datetime import datetime
stime = datetime.now()
print(f'---programm started at {stime}')

def formula(a, b, c):
    d = b**2 - 4 * a * c

    if d > 0:
        x1_1 = - b + (d ** 0.5)
        x1_2 = x1_1 / (2 * a)

        x2_1 = - b - (d ** 0.5)
        x2_2 = x2_1 / (2 * a)

        print(f'discriminant - > {d} = two solutions.')
        print(f'x1 -> {x1_2}')
        print(f'x2 -> {x2_2}')
    elif d == 0: 
        x1_1 = - b + (d ** 0.5)
        x1_2 = x1_1 / (2 * a)
        
        print(f'discriminant - > {d} = one solution.')
        print(f'x1 -> {x1_2}')
    elif d < 0:
        print(f'{d} < 0, no solutions.')
    else:
        print('invalid.')
        
def main():
    ans = 1
    while ans == 1:
        a = int(input('enter variable A -> '))
        b = int(input('enter variable B -> '))
        c = int(input('enter variable C -> '))
        
        formula(a, b, c)
        
        ans = int(input('again? 1 - yes, 0 - stop: '))
        
    endt = datetime.now()
    print(f'--- programm finished at {endt}.')
    
main()
    