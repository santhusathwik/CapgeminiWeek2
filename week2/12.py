class Payment:
    def process_payment(self):
        print("The payment is processed")

class CreditCardPayment(Payment):
    def process_payment(self):
        print("The payment is processed through CreditCard")

class PayPalPayment(Payment):
    def process_payment(self):
        print("The payment is processed thorugh PayPal")

class BitCoinPayment(Payment):
    def process_payment(self):
        print("The payment is processed Bitcoin")

cc=CreditCardPayment()
pp=PayPalPayment()
bc=BitCoinPayment()
cc.process_payment()
pp.process_payment()
bc.process_payment()
p=Payment()
p.process_payment()

