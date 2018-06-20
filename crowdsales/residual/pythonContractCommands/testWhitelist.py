from ico.utils import check_succesful_tx
from ico.utils import get_contract_by_name
import populus
from populus.utils.cli import request_account_unlock
from populus.utils.accounts import is_account_locked

p = populus.Project()
account = "0x3e3c4504a59d1f35dedc9b079dbbd51275ee1a6b"  # Our controller account on Kovan

with p.get_chain("kovan") as chain:
    web3 = chain.web3
    Contract = get_contract_by_name(chain, "Crowdsale")
    contract = Contract(address="0x3bfb37fde9bf11923de51d50e58c67a6675040c2")

    if is_account_locked(web3, account):
        request_account_unlock(chain, account, None)

    txid = contract.transact({"from": account}).setEarlyParicipantWhitelist("0x2BB6a9aC8ff0bF09aAC94F08bACe57f41E9bC312", True)
    print("TXID is", txid)
    check_succesful_tx(web3, txid)
    print("OK")