def anagram(input_string:str):
    if len(input_string)==1:
        return input_string[0]
    collection = []
    first_char = input_string[0]
    substring_anagram = anagram(input_string[1:len(input_string)])

    for item in substring_anagram:
        for i in range(0,len(item)+1):
            print(f"i={i} len:{len(item)}  len+1:{len(item)+1}")
            new_substring = item[:i]+ first_char + item[i:]
            collection.append(new_substring)
    return collection

print(anagram("abc"))
    