import pywhatkit

no =input("enter the no &\n add country code in staring :- ")
text = input("enter the sms :- ")
h=int(input("enter the hour between 1 to 24 :- "))
m=int(input("enter the miniut between 1 to 60 :- "))

def whatsapp(no, text, h, m):
    texts = text+'\n whatsapp_bot by amg '
    pywhatkit.sendwhatmsg(no, texts, h, m)

whatsapp(no, text, h, m)