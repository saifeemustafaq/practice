if __name__ == '__main__':
    s = 'qA2'
    a = list(s)
    for x in a:
        j = x.isalnum()
        if(j==True):
            print('True')
            break
        else:
            print('False')
            break

    for x in a:
        j = x.isalpha()
        if(j==True):
            print('True')
            break
        else:
            print('False')
            break

    for x in a:
        j = x.isdigit()
        if(j==True):
            print('True')
            break
        else:
            print('False')
            break

    for x in a:
        j = x.islower()
        if(j==True):
            print('True')
            break
        else:
            print('False')
            break

    for x in a:
        j = x.isupper()
        if(j==True):
            print('True')
            break
        else:
            print('False')
            break
        



    '''
    alnum = s.isalnum()
    alpha = s.isalpha()
    digit = s.isdigit()
    lower = s.islower()
    upper = s.isupper()
    print(alnum,alpha,digit,lower,upper,sep="\n")
    
    
    if(s.isalnum() == True):
        print("True")
    else:
        print("False")
    '''
