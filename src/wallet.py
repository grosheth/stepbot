# from pymongo import MongoClient

# class Wallet():

    # def create_wallet(user, money)
    #     for member in ctx.guild.members:
    #         print(member.id)
    #         cashflow = Wallet.wallet(member.id, 10000)
    #         print(cashflow)

    # def reset_wallet():
    #     connect = MongoClient(CONN_STRING)
    #     db = connect.discord
    #     collection = db.wallet
    #     for member in ctx.guild.members:
    #         print(member.id)
    #         money = 25000
    #         collection.update_one({
    #         '_id': 	member.id
    #         },{
    #         '$set': {
    #             'Nanane': money
    #         }
    #         }, upsert=True)