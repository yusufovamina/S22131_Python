'''
try:
    print("start code")
    print(error)
    print("no errors")
except:
    print("we have an error")

print("code after capsule")


try:
    print("start")
    print("murad")
    print(10/2)
    print("end")
except NameError: #'SyntaxError'
    print("Name error")
except ZeroDivisionError:
    print("Zero Division Error")
else:
    print("YOUR CODE IS VERY GOOD DUDE!!!")


class OnlyDigitsAllowed(Exception):
    pass

def get_number():
    user_input = input("Input your phone number: ")
    if not user_input.isdigit():
        raise OnlyDigitsAllowed("Nepravsan. AE ONLY NUMBERS ALLOWED")
    return user_input

try:
    number = get_number()
    print(f"Вы ввели {number}")
except OnlyDigitsAllowed:
    print("ONLY NUMBERS ALLOWED")
'''



import requests

try:
    response = requests.get("https://fake-json-api.mock.beeceptor.com/users")
    response.raise_for_status()
    data = response.json()

    for user in data:
        print(user)
except requests.exceptions.RequestException:
    print("Ошибка при запросе данных")