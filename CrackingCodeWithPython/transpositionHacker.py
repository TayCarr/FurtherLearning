#Transposition Cipher Hacker
#www.nostarch.com/crackingcodes/ (some changes i made)

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    '''test = "  aaHell o World"
    print(test)
    test= test.strip('aa')
    print(test)''' #strip doesnt remove cars in the middle of a string only at start and end!! so aa wont be removed cause of the whitespace
    message = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hackedMessage = hackTransposition(message)

    if hackedMessage == None:
        print("Failed to hack encrypted message.")
    else:
        print("Copying hacked message to clipboard: ")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print("Hacking ...")

    #can quit with ctr c or ctr d
    print("Force quit at anytime if needed.")

    #brute force by looping through every possible key 
    for key in range(1, len(message)):
        print("Trying key #%s..." % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            #ask user if this is correct
            print("\nPossible encryption hack: ")
            print("Key %s: %s" % (key, decryptedText[:100]))
            print("\nEnter D if done, anything else to continue to hack...")
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return decryptedText
    return None

if __name__ == '__main__':
    main()