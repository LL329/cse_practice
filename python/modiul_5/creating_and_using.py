def call():
    print('calling some one i don\'t know')
    return 'call done'

class phone:
    price = 12000
    color ='blue'
    brand='samsung'
    features=['camera','speaker','hammer']

    def call(self):
        print('calling one person')
    
    def send_sms(self,phone,sms):
        text=f'sending sms to: {phone} and message: {sms}'
        return text

my_phone = phone()
print(my_phone.features)
print(my_phone.brand)
calling=my_phone.call()
print(calling)
result=my_phone.send_sms(4153,'I forgot to miss you')
print(result)


