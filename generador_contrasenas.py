import random

def uniqueValidation(newPassword, oldPasswords):
    for i in oldPasswords:
        if newPassword == oldPasswords[i]:
            return False
        return True

def shuffleText(newPassword):

    suffledPassword = ''
    for i in newPassword:
        num = random.randint(0, len(newPassword)-1)
        suffledPassword = newPassword[num] + suffledPassword
        newPassword.pop([num])
    return suffledPassword

print(shuffleText(input('\nIngrese una contraseña para mezclar: \n')))
