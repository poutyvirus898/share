newPassword = str(input('voer hier je nieuwe wachtwoord in: '))
oldPassword = 'partybeast69'
def new_password(oldPassword, newPassword):
    if newPassword == oldPassword:
        print('je nieuwe wachtwoord mag niet hetzelfde zijn als het oude wachtwoord')
        return 0
    elif len(newPassword) < 6:
        print('je wachtwoord moet minimaal 6 tekens bevatten')
        return 0
    else:
        print('je wachtwoord is veranderd')
        return 1
new_password(oldPassword, newPassword)