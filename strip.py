def mystrip(text):
    end_index = len(text)
    for i in range(len(text) - 1, -1, -1):
        if text[i] != ' ':
            end_index = i + 1
            break
    
    return text[:end_index]

user_input = input("inter string : ")
stripped_result = mystrip(user_input)
print(f"'{stripped_result}'")