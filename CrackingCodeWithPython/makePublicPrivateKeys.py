#public key generator
#www.nostarch.com/crackingcodes

import random, sys, os, primeNum, cryptoMath

def main():
    #create a public/private keypair with 1024 bit keys
    print('Making key files...')
    makeKeyFiles('t_c', 1024)
    print('Key files made')


def generateKey(keySize):
    #creates pub/priv keys keysize bits in size
    p = 0 
    q = 0

    #step 1 create two prime numbers, p and q
    #calculate n = p * q
    print('generating p prime...')
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p * q

    #step 2 create a number e that is relat prime to (p-1)*(q-1)
    print('generating e that is is relat prime to (p-1)*(q-1)...')
    while True:
        #keep trying random numbers for e until one is valid
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    
    #step 3 calculate d, the mod inverse of e
    print('calculating d that is the mod inverse of e...')
    d = cryptoMath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public Key: ', publicKey)
    print('Private Key: ', privateKey)

    return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    #create two files 'x_pubkey.txt' and 'x_privkey.txt' 

    #check not overwriting files
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print()
    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    print()
    print('The private key is a %s and a %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()

if __name__ == '__main__':
    main()