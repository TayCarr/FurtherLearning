#Modular Arithmetic 

'''
I LOVE modular arithmetic I think it is so fun!! This will include an intro to what it is and all that but there will also be a module 
for use
- Modular arithmetic
- Modulo operator (%)
- Greatest Common Divisor (GCD)
- Euclid's algorithm for finding the GCD
- Choosing Valid Multiplicative Keys
- Euclid's extended algorithm for finding modular inverses

Modular Arithmetic:
    Also known as clock arithmetic, refers to math in which numbers wrap around once they reach a particular value.
    So think of a clock being 1-12 and once it reaches the 12 it wraps back around to 1 (mod13 set is {0,1,2,3,4,5,6,7,8,9,10,11,12})
    Modular arithmetic is used to handle the wrap around in the affine cipher, on our clock 12 will be 0 instead (mod12)
    if it is 10 oclock in 5 hours the time will be 15 oclock but 15 is not on the clock so 15-12=3 (which is on the clock)
    But once numbers get large this no longer works think if it is 10 right now and we want to know the time in 200 hours 
    210-12=198 which is still not on the clock so you will need to subtract multiples of 12 here is where the modulo operator comes in.
    
Modulo Operator
    Abbreviated as mod, in python the symbol used is %. It can be thought of as a division remainder operator.
    21/5=4 r1, 21%5=1
    doing the above 15%12=3 and 210%12=6
    to do this on a calculator you need to do a bit of it by hand 21/5=4.2 -> 4*5=20 -> 21-20=1 
    15/12=1.25 -> 12*1=12 -> 15-12=3
    210/12=17.5 -> 12*17=204 -> 210-204=6

    if you have a scientific graphing calculator you can just 210mod12 and get the answer faster OR use this module hehe

    Keep in mind that 12 % 12 = 0 since the set does not actually include that number it is [0,12) (square bracket is inclusive and round is exclusive)

Finding Factors to Calculate the Greatest Common Divisor
    Factors are the numbers that are applied to produce a particular number. 4 * 6 = 24 -> 4 and 6 are factors of 24
    these factors will NOT leave a remainder when used in division (remainder = 0) when dividing it is called a divisor
    24 has other factors! -> 8*3, 12*2, 21*1 -> so factors of 24 are 1,2,3,4,6,8,12,24

    note all numbers will have the factors 1*itself

    factors of 30 -> 1*30, 2*15, 3*10, 5*6

    Notice 24 and 30 have common factors 1,2,3,6 of these factors the greatest common factor (divisor) is 6 gcd(24,30)=6

Euclid's Algorithm for Finding GCD
    Take two numbers a and b -> b % a = r
    next step b % r = next r 
    this repeats until r = 0

    dont worry about the proof behind it or if you dont understand it, you can search it up if interested 

Choosing Valid Multiplicative Keys
    In the multiplicative cipher, the key and the size of the symbol set MUST be relatively prime to eachother.
    Numbers are relatively prime (or coprime) if their GCD is 1. In other words if they have no factors in common
    then those numbers are coprime. gcd(a,b) a being the key value and b being the size of the symbol set
    if they are not then the encryption decryption will result in multiple symbols having the same encryption value

Modular Inverse
    Of two numbers is represented by the expression (a * i) % m == 1, where i is the modular inverse and a & m are the 
    two numbers.
    example: the mod inverse of 5 mod 7 would be some number i where (5*i)%7 is equal to 1 
        brute force for this example can be done like this 
            1 isnt the modular inverse of 5 mod 7 because (5*1)%7=5
            2 is as (5*2)%7=3
            3 is as (5*3)%7=1
    although the encryption and decryption keys for the caesar cipher part of the affine cipher are the same, the 
    encryption and decryption keys for the multiplicative cipher are different numbers
    encryption key can be anything as long as it is relatively prime to the size of the symbol set
    example if our set size is 66 and we choose the key to be 53 with some calculations we will see that 5 is 
    the modular inverse of 53 mod 66 as (53*5)%66=1
    so you would know the affine cipher decryption key is 5 
    to decrypt the ciphertext multiply that letters number by 5 then mod 66 the result is the original plaintext number


'''



def main():
    #print(gcd(24,5))
    #print(findModInverse(5, 7))
    print(findModInverse(53, 66))

#to find the greatest common factor of a and b
# a does not need to be greater than b 
def gcd(a, b):
    while a!= 0:
        a, b = b % a, a
    return b

#to find the modular inverse
#you could brute force this but the larger the key the longer this will take 
#euclids extended algorithm to find the modular inverse of a number
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None #no mod inverse if a & m arent rel prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3 #NOTE // is the integer division
        #int div divides two numbers and rounds down to the nearest integer
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

if __name__ == '__main__':
    main()