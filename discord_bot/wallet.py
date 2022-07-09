from pymongo import MongoClient

class Wallet(Document):

    # def create_wallet(user, money)
    #     for member in ctx.guild.members:
    #         print(member.id)
    #         cashflow = Wallet.wallet(member.id, 10000)
    #         print(cashflow)

    # def wallet(user, money):

    #     connect = MongoClient(CONN_STRING)
    #     db = connect.discord
    #     collection = db.wallet
    
    #     wallets = {
    #         str(user): money
    #     }
        
    #     collection.insert_one(cashflow)

    #     return wallets
