def palin(text):
    if len(text)<=1:
        print("palindrome")
    
    else:
        if text[0]==text[-1]:
            palin(text[1:-1])
        else:
            print("note palindrome")

palin("madam")
palin("malayalam")
palin("abba")
palin("python")
