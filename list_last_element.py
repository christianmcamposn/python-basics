

def run():
    test_list = [ ['Team 01: Player 01', 'Team 01: Player 02', 'Team 01: Player 03', 'Team 01: Player 04', 'Team 01: Player 05', 'Team 01: Player 06'], 
                  ['Team 02: Player 01', 'Team 02: Player 02', 'Team 02: Player 03', 'Team 02: Player 04', 'Team 02: Player 05', 'Team 02: Player 06'],
                  ['Team 03: Player 01', 'Team 03: Player 02', 'Team 03: Player 03', 'Team 03: Player 04', 'Team 03: Player 05', 'Team 03: Player 06'],
                  ['Team 04: Player 01', 'Team 04: Player 02', 'Team 04: Player 03', 'Team 04: Player 04', 'Team 04: Player 05', 'Team 04: Player 06'] 
                ]

     
    #print(len(test_list))
    #print(test_list[-1][1])
    #print(test_list)
    #print(test_list[3][0])
    print([1, 2, 3][1:])
    print(len([1, 2, 3][1:]))

def run2():
    #n = 0
    #variable =  "Team " + str(n+3) + ": Player " + str(n+3)
    test_list2 = [["Team " + str("0").zfill(2) + ": Player " + str(n).zfill(2) for n in range(10) ] ,
                  ["Team " + str("1").zfill(2) + ": Player " + str(n).zfill(2) for n in range(10) ] , 
                  ["Team " + str("2").zfill(2) + ": Player " + str(n).zfill(2) for n in range(10) ]
                 ]
    print(test_list2) 

if __name__ == '__main__':
    #run()
    run2()