class phone:
    manufactured = 'china'

    def __init__(self, owner, brand, price):
        self.owner= owner
        self.brand= brand
        self.price= price
      


    def send_sms(self, phone, sms):
        text =f'sending to : {phone} and sms is:  {sms}'
        print(text)


my_phone = phone('Rohimi bokso', 'Samgung', 2200)        
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone= phone('Johir uddin', 'Iphone', 1500000)
print(her_phone.owner, her_phone.brand, her_phone.price)

fucker_button= phone('Shanto', 'itel', 150)
print(fucker_button.owner, fucker_button.brand, fucker_button.price)

her_phone.send_sms()
fucker_button.send_sms()
