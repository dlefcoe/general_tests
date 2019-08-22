


def yourMaritalStatus(married, assetsBefore):
    ''' function to return assets based on marital status '''


    # check if married
    if married == True or married == 'y':
        assetsAfter = assetsBefore / 2
    else:
        assetsAfter = assetsBefore

    return assetsAfter


marriedBool = input('are you married? input y (for yes) or n (for no) >>>   ')
assetPool = int(input('how much money do you have ?   '))

z = yourMaritalStatus(marriedBool, assetPool)
print(f'{z:,}')



