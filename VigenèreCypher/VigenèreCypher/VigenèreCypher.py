
# Vigenere Cipher 
  
# This function generates the  
# key in a cyclic manner until  
# it's length is equal to  
# the length of original text 
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
# This function returns the  
# encrypted text generated  
# with the help of the key 
def cipherText(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 
      
# This function decrypts the  
# encrypted text and returns  
# the original text 
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 
      

# Driver code  main1
if __name__ == "__main__": 
    choice = int(input("Enter 1 for Encrypting or 2 for Decrypting: ")) # This makes 
    if choice ==1:
        string = input("Enter some text to encrypt: ").upper();
        keyword = input("Enter any letters to be able to make a key: ").upper();
        key = generateKey(string, keyword) 
        cipher_text = cipherText(string,key) 
        print("Ciphertext :", cipher_text) 
    elif choice ==2:
        string = input( "Enter The encrypted word:").upper();
        keyword = input( "Enter any letters to be able to make a key:").upper();
        key = generateKey(string, keyword) 
        cipher_text = string 
        print("Original/Decrypted Text: ",  
               originalText(cipher_text, key)) 
    else:
        print("Wrong choice entered, Exiting now..");
        exit();
  
# This code is contributed  
# by Pratik Somwanshi 
# Vigenère Cipher. (2019, May 29). Retrieved from https://www.geeksforgeeks.org/vigenere-cipher/
