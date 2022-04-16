now = datetime.now() # current date and time

class colors:

    darkblue = fg('#1915ed')
    blue = fg('#00ffff')
    aqua = fg('#11d9f0')
    gray = fg('#aab2b3')
    purple = fg('#d400ff')
    ehpurple = fg('#3420e6')
    reset = fg('#FFFFFF')

os.system('cls;clear & title Email Spammer')
print (f"""

                                                    {colors.blue}╔═╗{colors.darkblue}╔╦╗{colors.blue}╔═╗{colors.darkblue}╦{colors.blue}╦  
                                                    {colors.blue}║╣ {colors.darkblue}║║║{colors.blue}╠═╣{colors.darkblue}║{colors.blue}║  
                                                    {colors.blue}╚═╝{colors.darkblue}╩ ╩{colors.blue}╩ ╩{colors.darkblue}╩{colors.blue}╩═╝
                                                {colors.blue}╔═╗{colors.darkblue}╔═╗{colors.blue}╔═╗{colors.darkblue}╔╦╗{colors.blue}╔╦╗{colors.darkblue}╔═╗{colors.blue}╦═╗
                                                {colors.blue}╚═╗{colors.darkblue}╠═╝{colors.blue}╠═╣{colors.darkblue}║║║{colors.blue}║║║{colors.darkblue}║╣ {colors.blue}╠╦╝
                                                {colors.blue}╚═╝{colors.darkblue}╩  {colors.blue}╩ ╩{colors.darkblue}╩ ╩{colors.blue}╩ ╩{colors.darkblue}╚═╝{colors.blue}╩╚═
{colors.reset}
""")

files = open('email.txt', 'r')
bomb_emails = files.readlines()

email = input(now.strftime(f"{colors.gray}[{colors.purple}%H:%M:%S{colors.gray}]" f" Your Email? "))
password = (maskpass.askpass((now.strftime(f"{colors.gray}[{colors.purple}%H:%M:%S{colors.gray}]" " Your Password? "))))
message = input(now.strftime(f"{colors.gray}[{colors.purple}%H:%M:%S{colors.gray}]" f" Message? "))
message_relode = int(input(now.strftime(f"{colors.gray}[{colors.purple}%H:%M:%S{colors.gray}]" f" How many message you want to send? ")))


for bomb_email in bomb_emails:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        print("message sent to {}".format(bomb_email))
    time.sleep(1)

input()
mail.close()
files.close()

print("Ez")
input()
