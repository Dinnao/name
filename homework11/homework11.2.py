def secret_email(email):
    email_s = email.replace(email[3:6], '***')
    email_sc = email_s.replace(email[10:13], '***')
    print(email_sc)
secret_email('someemail@gmail.com')
#не знаю сделал я правельно или нет, не понял как сдлеать чтоб оно скрвыало до и после '@'