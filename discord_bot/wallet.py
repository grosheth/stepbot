from mongoengine import *

class Wallet(Document):
    user = 0
    money = 0
    wallets = {
        user: money
    }

    

