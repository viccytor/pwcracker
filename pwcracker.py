# Imports
import itertools
import time

# Brute Force Function
def bruteForcePassword(password, characterSet):
    chars = characterSet    
    start = time.time()
    attempts = 0
    for i in range(1, 9):
        # Basic Iteration
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if letter == password:
                end = time.time()
                distance = end - start
                return (attempts, distance)

def dictionaryAttack(password):
    start = time.time()
    filepath = 'commonpw.txt'
    with open(filepath) as fp:
        count = 1
        line = fp.readline()
        while line:
            if line.strip() == password:
                end = time.time()
                distance = end - start
                return(count, distance)
            else:
                line = fp.readline()
                count+=1



# Main Function
def main():
    # Character Set
    characterSet = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"

    attackType = input("What attack type do you want to use: (Brute Force or Dictionary): ")

    password = input("Enter Password: ")

    if (attackType == ('Brute Force' or 'brute force' or 'BF' or 'bf' or 'Brute force')):
        tries, time = bruteForcePassword(password, characterSet)
    else:
        tries, time = dictionaryAttack(password)


    # Print Statistics
    print("Password cracked password %s in %s tries and %s seconds!" % (password, tries, time))


main()