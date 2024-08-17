def send_email(message: str, recipient: str, *, sender: str= "university.help@gmail.com"):
    r_domain = recipient[-4:]
    s_domain = sender[-4:]
    r_valid = "@" in recipient and (".com" in r_domain or ".ru" in r_domain or ".net" in r_domain)
    s_valid = "@" in sender and (".com" in s_domain or ".ru" in s_domain or ".net" in s_domain)
    if r_valid and s_valid:
        if recipient == sender:
            print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


send_email("Example.", "amogus@red.sus")
send_email("Regarding grand embezzlement allegations.", "rsa@usa.gov", sender="humble_billionaire@protonmail.net")
send_email("I love taxes.", "rsa@google.com", sender="nonprofit_startup@protonmail.net")
send_email("Ереванские овшоры за три минуты!", "orders@aliexpress.com")
