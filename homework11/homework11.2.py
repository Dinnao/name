delimiter = '***@***'
def secret_email(s_email):
    email = s_email.index('@')
    print(s_email[:email -5] + delimiter + s_email[email + 5:])
secret_email(input('Please enter email: '))