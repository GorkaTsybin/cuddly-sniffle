calls = 0
def count_calls():
    global calls
    calls +=1

def string_info(string):
    string = str(string)
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()

    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            reult = False
            break
        else:
            result = False
        continue
        return result

print(string_info('Richard'))
print(string_info('Vavilovec'))
print(is_contains('cycle', ['recycling', 'recycling', 'sphere']))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(calls)