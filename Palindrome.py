def Palindrome():
    print("Palindrome check. Will result in 'true' if the entry is the same forward and backward")
    while True:
        palindromeCheck = str(input()).lower().replace(" ", "")
        if len(palindromeCheck) >=0:
            reverse = palindromeCheck[len((palindromeCheck))//2:len(palindromeCheck)]
            reverse = reverse[::-1]
            if palindromeCheck[0:len(palindromeCheck)//2] == reverse:
                print(True)
            elif palindromeCheck[0:len(palindromeCheck)//2] == reverse[0:-1]:
                print(True)
            else:
                print(False)
Palindrome()
