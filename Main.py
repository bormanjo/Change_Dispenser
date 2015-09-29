
def giveChange(amount, coins):
    '''given an amount and a list of coins, returns [numberOfCoins, listOfCoins]'''

    if amount == 0:
        return [0, []]
    elif coins == []:
        return [float("inf"), []]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    
    else:                                               #coins[0] <= amount
        useit = giveChange(amount-coins[0], coins)
        loseit = giveChange(amount, coins[1:])
        
        use = [ useit[0] + 1, useit[1] + [coins[0]] ]
        lose = [ loseit[0], loseit[1] ]

        if use[0] < lose[0]:                            #numberOfCoins in use list < lose list
            return use                          
        
        else:                                           #numberOfCoins in lose list <= use list
            return lose

            
        
        
