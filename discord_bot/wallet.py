from mongoengine import *

class Wallet(Document):
    
    
    def wallet(user, money):
        wallets = {
            user: money
        }
        return wallets
