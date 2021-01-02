try:
    import os
except:
    print(R+"\n [-]We couldn't import os. \n")
    exit()

try:
    from smtplib import SMTP
except:
    print(R+"\n [-]We couldn't import smtplib. \n")
    exit()

try:
    from email.mime.text import MIMEText
except:
    print(R+"\n [-]We couldn't import email.mime.text. \n")
    exit()

try:
    from email.mime.multipart import MIMEMultipart
except:
    print(R+"\n [-]We couldn't import email.mime.multipart. \n")
    exit()


#this colors from:(twiiter@Xcodeone1)
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray

def logo():
    os.system("clear")
    print(G+'''
                     _           
                    | |          
  ___  ___ _ __   __| | ___ _ __ 
 / __|/ _ \ '_ \ / _` |/ _ \ '__|
 \__ \  __/ | | | (_| |  __/ |   
 |___/\___|_| |_|\__,_|\___|_|   
                                 
        Twitter:@ip_274     
    ''')
    print("\n")

logo()


#send data to E-mail  
def send_to_mail(tool_mail , password , send_to , msg):
    
    # https://myaccount.google.com/u/4/lesssecureapps

    mailer = SMTP('smtp.gmail.com',587)

    mailer.starttls()

    mailer.login(tool_mail,password)
                    
    mailer.sendmail(tool_mail,send_to,msg)

    mailer.quit()


#Wait time 
def mainapp():
    logo()

    tool_email = input(G+"Enter the email that the tool will use: "+W)
    pass_email = input(G+"Enter the password for this email: "+W)
    list_email = input(G+"Enter the list of targeted email accounts [with .txt]: "+W)

    logo()
    subject = input(G+"Enter a subject of email: "+W)
    bodyfile = input(G+"Enter the name of the file that contains the message[with .txt]: "+W)

    try:
        body = open(bodyfile,"r").read()
    except:
        print(R+"\n [-]We couldn't found msg file. \n")
        exit()

    logo()

    try:
        mails = open(list_email).read().splitlines()
    except:
        print(R+"\n [-]We couldn't found mails file. \n")
        exit()
    
    count = 0
    for line in open("mails.txt"):
        count += 1 

    print("-------------------------")
    print(G+"[+]Start Send emails now!")
    print(G+"[+]We have", count , "Email")
    print("-------------------------")
    print("\n")

    for mail in mails:
        try:
            massage = MIMEMultipart()
            massage['From'] = tool_email
            massage["To"]= mail
            massage["Subject"]  = subject
                        
            massage.attach(MIMEText(body,'plain'))
            text = massage.as_string()

            send_to_mail(tool_email,pass_email,mail,text)

            print(G+"[+]We have sent a message to: "+W+mail,"\n")
        except: 
            print(R+"[+]We can't sent a message to: "+W+mail,"\n") 



mainapp()

