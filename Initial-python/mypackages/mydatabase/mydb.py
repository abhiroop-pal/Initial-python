
def pydb():
    #python with databases
    import sqlite3 
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    
    #create table
    c.execute ('''create table if not exists stocks (date text, trans text, symbol text, qty real, price real)''')

    in_put = input('Do you want to enter data? (Y|y for yes & any key for no)')
    if in_put == 'Y' or in_put == 'y':
        #insert values
        c.execute('''insert into stocks values ('2006-01-05','BUY','RHAT', 100, 35.14)''')
        
        #save/commit changes
        conn.commit()
        
        # Larger example that inserts many records at a time
        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00), ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),('2006-04-06', 'SELL', 'IBM', 500, 53.00)]
        c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
        
        conn.commit()
    else:
        pass




    print ('print what exists')
    c.execute('SELECT * FROM stocks')
    #print(c.fetchone())
    print(c.fetchall())


    x = input('Which data do you want to see:\n1: All  \n2: One Company \n\n')


    if x == '1':
        #display data
        op = c.execute('SELECT * FROM stocks')
        #print(c.fetchall())
        for row in op:
            print (row)
    elif x == '2':
        t = ('RHAT',)
        c.execute('SELECT * FROM stocks WHERE symbol=?', t)
        #print(c.fetchone())
        print(c.fetchall())
    else:
        print ('incorrect choice')


    drop_tab = input('Do you want to drop table? (Y|y for yes & any key for no)')
    if drop_tab == 'Y' or drop_tab == 'y':
        #drop table to clear entries
        c.execute('drop table stocks')
    else:
        pass

    #close connection
    conn.close()