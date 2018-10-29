# This is a script written by Dustin H. 
# Educational purposes only.

# Note: won't work without the appropriate dictionary.txt file present
# Any competent SysAdmin will have logging on whatever machine you run this on.
# I am not responsible for whatever you do with this.

import crypt    # import crypt module
from pathlib import Path

def testPass(cryptPass):    # define function to take one argument, the encrypted password
        salt = cryptPass[0:2]  # `salt` is the first two characters of the hashed password
        dictFile = open('dictionary.txt', 'r') # open the dictionary, read from it and assign
        for word in dictFile.readlines(): # for every word in our dictionary file,
            word = word.strip('\n') # word is defined by every end of a line
            cryptWord = crypt.crypt(word,salt) # associate the word with the salt
            if (cryptWord == cryptPass): # if the word and salt match the hash
                    print("[+] Found Password: " , word , "\n") # print the cracked password
                    return # and return it
        print("[-] Password not found.\n") # if you never go into the loop, print this
        return

def main(): # main function that writes to our file
    dictFile = Path("./dictionary.txt")  # change this to whatever dir your dict is in.
    if not dictFile.is_file(): # check for dictionary file
        print("[!] No dictionary file found.")

    passFile = open('passwords.txt') # passFile is the opened form of passwords.txt
    for line in passFile.readlines(): # every line, we will
        if ":" in line:   # check for users 
            user = line.split(':')[0]  # break them up from the semicolons, giving us a username
            cryptPass = line.split(':')[1].strip(' ') # format them 
            print("[*] Cracking Password for: ", user) 
            testPass(cryptPass)

main()
#if __name__ == "__main__":
#   main()
