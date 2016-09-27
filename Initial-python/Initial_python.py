

def module1():
    print('this is module 1')
    print ('__name__ is ' +__name__)

def db_mod():
    '''Database module used in packages
    '''
    #calling a package
    print ('\nThis is database modules')
    import mypackages.mydatabase.mydb as p
    #import all the way till the module name and then reference the function in that module
    p.pydb()


def main():
    print ('this is a sample program')
    print ('this is main module')
    print ('__name__ is ' +__name__)

    #calling another module in same program
    module1()
    
    #calling another module in same directory
    import extra_module as m
    m.module2()

    db_mod()
    '''
    import time
    print ('sleeping for 3\n')
    time.sleep(3)
    '''

    




if __name__ == '__main__':
    main()
