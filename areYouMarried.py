

def yourMaritalStatus(married:str, assetsBefore:float):
    ''' function to return assets based on marital status '''
    
    if not isinstance(married, str):
        raise TypeError('married must be a string')

    if not isinstance(assetsBefore, (int, float)):
        raise TypeError('assetsBefore must be a number')

    # check if married
    if married == 'y':
        assetsAfter = assetsBefore / 2
    elif married == 'n':
        assetsAfter = assetsBefore
    else:
        raise ValueError('married must be y or n')

    return assetsAfter


marriedBool = input('are you married? input y (for yes) or n (for no) >>>   ')
assetPool = int(input('how much money do you have ?   '))

z = yourMaritalStatus(marriedBool, assetPool)
print(f'{z:,}')



