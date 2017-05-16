# Script to programmatically send bitcoin via email

## Install
* Make sure you have python 2.7 installed
* Install requests and pycoin python modules. Using pip you can do
```pip install pycoin requests```

## Sample Input file
```
webmaster@blockonomics.co
support@blockonomics.co
```

## Sample Run
```
python main.py -i /tmp/inp.txt 
"webmaster@blockonomics.co","1HdrmsYgPc4dKGr67PM8VhLUTFu1DKYUSp","https://www.blockonomics.co/btcmail#/redeem?key1=L26fEzVqZGDr7JcB8Aum1PAnoTaUS6pWvmA7ungch21inzSVPPZM&bitcoin_address=1HdrmsYgPc4dKGr67PM8VhLUTFu1DKYUSp"
"support@blockonomics.co","18fCzYVZ8cZqrJvdQSC5qRN7bSrDQQw8r8","https://www.blockonomics.co/btcmail#/redeem?key1=L53sqrBH5dNEbJVUiH2CLr6AviuTSmUQeuBb9VNmgEkfJQxH4Rbz&bitcoin_address=18fCzYVZ8cZqrJvdQSC5qRN7bSrDQQw8r8"
```
