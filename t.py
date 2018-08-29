#!/bin/python

def ppp():
    print 123
    def p():
        print 1234444
    p()

ppp()
    

a = [6, 7, 8, 9]
g = (x for x in a)
r = g.next()
#while True:
#    r_next = g.next()
#    print r
#    r = r_next


try:
    print 'try ....'
    raise Exception('123')

except Exception as e:
    print 'excpeton...'

else:
    print 'in else////'


