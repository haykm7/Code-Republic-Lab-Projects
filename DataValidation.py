def email_validator(email):
    check1 = False
    check2 = False
    first_check = email[0].isalnum() == False

    if email[0] == '_' or email[0] == '@' or first_check:
        return False

    for i in range(len(email)):
        if email[i] == '@' and email[i+1] != '.':
            check1 = True
        if email[i] == '.' and email[len(email)-1] != '.':
            check2 = True
    if check1 == True and check2 == True:
        return True
    return False

def url_validator(url):
    if url[:4] != 'www.':
        return False
    for i in range(4,len(url)):
        if url[i] == '.' and url[len(url)-1] != '.':
            return True
    return False

def date_validator(date):
    if int(date[:2]) > 32:
        return False
    check1 = False
    check2 = False
    for i in range(2,len(date)):
        if date[i] == '/' and date[i+1] != '2':
            check1 = True
        if date[i] == '/' and date[i+1] == '2':
            check2 = True
    if check1 == True and check2 == True:
        return True
    else:
        return False

def number_validator(number):
    if number.isalpha():
        return False
    else:
        return True

def card_validator(card):
    digits_n = len(card)
    if digits_n >= 13 and digits_n <= 16:
        return True
    return False

def mobilenumber_validator(number):
    if number.isalpha():
        return False
    else:
        return True



