#text always started with a Capital letter and ended with a period.

def correct_sentence(text: str):
    text = text[0].upper() + text[1:]
    if not text[-1] == '.':
        text += '.'
    return text


print(correct_sentence("greetings, friends") ) #== "Greetings, friends.", 'Test1'
print(correct_sentence("hello"))# == "Hello.", 'Test2'
print(correct_sentence("Greetings. Friends"))# == "Greetings. Friends.", 'Test3'
print(correct_sentence("Greetings, friends.") )#== "Greetings, friends.", 'Test4'
print( correct_sentence("greetings, friends."))# == "Greetings, friends.", 'Test5'
