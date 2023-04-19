import itertools
import time
from string import ascii_letters, digits, punctuation
digits='1234567890'
users_password=input('Please input yor code')
def brute_excel_doc():
    global start, end
    print('***Hello friend***')
    try:
        password_len=input("write length of your password, for example: 2 - 5")
        password_len=[int(item) for item in password_len.split('-')]
    except:
        print("Check your input")
    
    print('If your password contains only digits write: 1\nIf your password contains only ascii_letters write: 2\nIf your password contains digits and ascii_letters write: 3\n'
          'If your password contains digits, ascii_letters and punctuation write: 4')
    
    try:
        choice=int(input(': '))
        if choice==1:
            possible_symbols=digits
        elif choice==2:
            possible_symbols=ascii_letters
        elif choice==3:
            possible_symbols=digits + ascii_letters
        elif choice==4:
            possible_symbols=digits + ascii_letters + punctuation
        else:
            possible_symbols='O.o what you want?'
        print(possible_symbols)
    except:
        print('O.o what you want?')
    
    #brute excel doc
    start = time.monotonic()
    for pass_len in range(password_len[0], password_len[1]+1):
        for password in itertools.product(possible_symbols, repeat=pass_len):
            password=''.join(password)
            print(password)
            if password==users_password:
                print("We find your code: " + password)
                break
    end = time.monotonic()


def main():
    brute_excel_doc()
    print(users_password)
    print('span : {:>9.2f}'.format(end-start))

if __name__=='__main__':
    main()

