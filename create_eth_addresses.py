from web3 import Web3
from eth_account import Account
import secrets



priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("SAVE BUT DO NOT SHARE THIS:", private_key)

num = 50
list_accounts = []
for i in range(num):
    acct = Account.from_key(private_key)
    list_accounts.append(acct.address)
print(list_accounts)