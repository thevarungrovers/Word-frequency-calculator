# empty dictionary
mydic = {}

# function
def most_frequent(word):
     for i in word:
        b = word.count(i)
        mydic[i] = b # dictionary elements added

# input from user
text = input('Enter a string: ')


if text.isalpha():
    most_frequent(text) # function call
    # printing
    for l in mydic:
        search_key = max(mydic.values()) # maximum value
        res = list(mydic.values()).index(search_key)  # index value of maximum value

        # list out keys and values separately
        key_list = list(mydic.keys())
        val_list = list(mydic.values())

        # print key with val 
        position = val_list.index(search_key)
        print(key_list[position],'=',search_key) # printing key and value
        mydic[key_list[position]] = 0 # changing the value to 0 to move the cursor to next word

else:
    print('Please enter a valid string!!')