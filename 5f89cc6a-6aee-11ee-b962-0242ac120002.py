O0000OOOOOOOO00000000OOOO00000OOOO0000OO =int (input ())
if O0000OOOOOOOO00000000OOOO00000OOOO0000OO > 5: exit(0)
O0000OOOO00000OOOO0000OO =[3 ,5 ]
for _ in range (2 ,O0000OOOOOOOO00000000OOOO00000OOOO0000OO +1 ):
    O0000OOOO00000OOOO0000OO .append (O0000OOOO00000OOOO0000OO [-1 ]*2 -1 )
OOO0O0O00O00O0O00O000O00O0OOO =[[' 'for _O00OO000OOOOO0000 in range (O0000OOOO00000OOOO0000OO [O0000OOOOOOOO00000000OOOO00000OOOO0000OO ]+1 )]for __ in range (O0000OOOO00000OOOO0000OO [O0000OOOOOOOO00000000OOOO00000OOOO0000OO ]+1 )]
def O0000OOOOOO0000000OOOOO00000000OOOO00000OOOO0000OOOOO0O0O00O00O0O00O000O00O0OOO (O0000OOOOOO0000OO0OOOO00000OOOO0000OO ,O0000OOOOO00000000OOOO00OOOO0000OO ,O0000OOOO000OOOO00000000OOOO00OOOO0000OO ):
    if O0000OOOOOO0000OO0OOOO00000OOOO0000OO ==0 : return
    O0O00OO0O0OOOO0OO =O0000OOOO00000OOOO0000OO [O0000OOOOOO0000OO0OOOO00000OOOO0000OO ]
    O0O0OOO00000OOOO0 =O0000OOOO00000OOOO0000OO [O0000OOOOOO0000OO0OOOO00000OOOO0000OO -1 ]
    for _OO00OO00O00O0O0OO in range (O0O00OO0O0OOOO0OO ):
        OOO0O0O00O00O0O00O000O00O0OOO [O0000OOOO000OOOO00000000OOOO00OOOO0000OO ][O0000OOOOO00000000OOOO00OOOO0000OO +_OO00OO00O00O0O0OO ]="*"
    for _OO00OO00O00O0O0OO in range (O0O0OOO00000OOOO0 ):
        OOO0O0O00O00O0O00O000O00O0OOO [O0000OOOO000OOOO00000000OOOO00OOOO0000OO -_OO00OO00O00O0O0OO ][O0000OOOOO00000000OOOO00OOOO0000OO +_OO00OO00O00O0O0OO ]="*"
        OOO0O0O00O00O0O00O000O00O0OOO [O0000OOOO000OOOO00000000OOOO00OOOO0000OO -_OO00OO00O00O0O0OO ][O0000OOOOO00000000OOOO00OOOO0000OO +(O0O00OO0O0OOOO0OO -1 )-_OO00OO00O00O0O0OO ]="*"
    O0000OOOOOO0000OO0OOOO00000OOOO0000OO -=1
    O0O00O0OOOOO00O00 =(O0000OOOO00000OOOO0000OO [O0000OOOOOO0000OO0OOOO00000OOOO0000OO ]+1 )//2
    O0000OOOOOO0000000OOOOO00000000OOOO00000OOOO0000OOOOO0O0O00O00O0O00O000O00O0OOO (O0000OOOOOO0000OO0OOOO00000OOOO0000OO ,O0000OOOOO00000000OOOO00OOOO0000OO ,O0000OOOO000OOOO00000000OOOO00OOOO0000OO )
    O0000OOOOOO0000000OOOOO00000000OOOO00000OOOO0000OOOOO0O0O00O00O0O00O000O00O0OOO (O0000OOOOOO0000OO0OOOO00000OOOO0000OO ,O0000OOOOO00000000OOOO00OOOO0000OO +(O0000OOOO00000OOOO0000OO [O0000OOOOOO0000OO0OOOO00000OOOO0000OO ]-1 ),O0000OOOO000OOOO00000000OOOO00OOOO0000OO )
    O0000OOOOOO0000000OOOOO00000000OOOO00000OOOO0000OOOOO0O0O00O00O0O00O000O00O0OOO (O0000OOOOOO0000OO0OOOO00000OOOO0000OO ,O0000OOOOO00000000OOOO00OOOO0000OO +(O0O00O0OOOOO00O00 -1 ),O0000OOOO000OOOO00000000OOOO00OOOO0000OO -(O0O00O0OOOOO00O00 -1 ))
O0000OOOOOO0000000OOOOO00000000OOOO00000OOOO0000OOOOO0O0O00O00O0O00O000O00O0OOO (O0000OOOOOOOO00000000OOOO00000OOOO0000OO ,0 ,O0000OOOO00000OOOO0000OO [O0000OOOOOOOO00000000OOOO00000OOOO0000OO ]-1 )
for _____ in range (len (OOO0O0O00O00O0O00O000O00O0OOO [0 ])//2 -1 ,len (OOO0O0O00O00O0O00O000O00O0OOO [0 ])-1 ):
    for __________ in range (len (OOO0O0O00O00O0O00O000O00O0OOO [0 ])):
        print (OOO0O0O00O00O0O00O000O00O0OOO [_____ ][__________ ],end ="")
    print ()
