'''
test the secrets module

the docs are here:
    https://docs.python.org/3/library/secrets.html#module-secrets


'''


# built-in modules (secrets)
import secrets
import pprint

def main():
    ''' main entry point for the code '''
    
    print('dice rolls:')
    r = test_secrets_01()
    print(r)

    print('random number:')
    r = test_secrets_02()
    print(r)

    print('random bits:')
    r = test_secrets_03()
    print(r)

    print('random byte string:')
    r = test_secrets_04()
    pprint.pp(r, indent=4)

    print('random text string (as hex):')
    r = test_secrets_05()
    pprint.pp(r, indent=4)

    print('URL-safe text string:')
    r = test_secrets_06()
    pprint.pp(r, indent=4)



def test_secrets_01():
    ''' simulate a dice roll '''
    seq = [1, 2, 3, 4, 5, 6]
    result = []
    for i in range(10):
        result.append(secrets.choice(seq))
    return result    


def test_secrets_02():
    ''' gen a random number '''
    result = []
    for i in range(10):
        result.append(secrets.randbelow(7))
    return result    

def test_secrets_03():
    ''' gen random bits '''
    result = []
    for i in range(10):
        # 0, 2, 4, 8
        result.append(secrets.randbits(3))
    return result    


def test_secrets_04():
    ''' gen random byte string '''
    result = []
    for i in range(5):
        result.append(secrets.token_bytes(16))
    return result    


def test_secrets_05():
    ''' gen random text string '''
    result = []
    for i in range(5):
        result.append(secrets.token_hex(16))
    return result    


def test_secrets_06():
    ''' gen URL-safe text string '''
    result = []
    for i in range(5):
        result.append(secrets.token_urlsafe(16))
    return result    

# main guard idiom
if __name__=='__main__':
    main()

