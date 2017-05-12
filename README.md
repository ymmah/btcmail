# Script to programmatically send bitcoin via email

## Install
* Make sure you have python 2.7 installed
* Install requests and pycoin python modules. Using pip you can do
```pip install pycoin requests```

## Running the script
* python main.py --email *(receivers email address)* 

## Sample Output
```
python main.py -e webmaster@blockonomics.co
{'bitcoin_address': u'16bAaVkzX6BQVdfYxSfGfHMamTcWAX3ekj', 'redeem_url':
'https://www.blockonomics.co/btcmail#/redeem?key1=Kyk8AYKuxhMRtXMtnJ51AbHoGrJRv4Lpc1fziux6kNLuYFqwryhU&bitcoin_address=16bAaVkzX6BQVdfYxSfGfHMamTcWAX3ekj'}
You can now send BTC to 16bAaVkzX6BQVdfYxSfGfHMamTcWAX3ekj and send webmaster@blockonomics.co the above redeemlink
```
