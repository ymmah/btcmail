# Generating Redeem links with Blockonomics API
## Requirements
* python 2.7
* Python modules
  * requests
  * pycoin

## Running the script
* python redeem_bitcoin.py --email *(receivers email address)* --server *(server end point for redeem)*
  * email : mandatory field
  * server : Optional field ( default value - https://www.blockonomics.co/btcmail#/redeem )
## Sample Output
 * Redeem Link : *https://www.blockonomics.co/btcmail#/redeem?key1=KzJBFHLKJ2gbCbYYtkWJmNdoPwx8EFqhb72U9nWv97ch963CgHJt&bitcoin_address=15mPgHPZdVt1MrgZ93nADrdWxSdUNy4WoS*
 * Bitcoin Address : *15mPgHPZdVt1MrgZ93nADrdWxSdUNy4WoS*
