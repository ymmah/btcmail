#!/usr/bin/evn python
"""
Pythong script for generating redeem links for given email address with given server end point.
"""
import re
import os
import argparse
import requests

from pycoin import ecdsa, encoding

"""
API Settings
"""
BASE_SERVER = "https://www.blockonomics.co"
SPLIT_KEY_API = BASE_SERVER + "/api/redeem_code"
SEND_MAIL_API = BASE_SERVER + "/api/send_redeem_code"
DEFAULT_REDEEM_ENDPOINT = BASE_SERVER + "/btcmail#/redeem"

"""
A custom type for argparse, to facilitate validation of email addresses.
"""
class EmailType(object):
    """
    Supports checking email agains different patterns. The current available patterns is:
    RFC5322 (http://www.ietf.org/rfc/rfc5322.txt)
    """

    patterns = {
        'RFC5322': re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"),
    }

    def __init__(self, pattern):
        if pattern not in self.patterns:
            raise KeyError('{} is not a supported email pattern, choose from:'
                           ' {}'.format(pattern, ','.join(self.patterns)))
        self._rules = pattern
        self._pattern = self.patterns[pattern]

    def __call__(self, value):
        if not self._pattern.match(value):
            raise argparse.ArgumentTypeError(
                "'{}' is not a valid email - does not match {} rules".format(value, self._rules))
        return value


def generate_redeem_code(email, redeem_url):

    """
    Generate (Public, Private) key pair
    """
    rand = os.urandom(32).encode('hex')
    secret_exponent= int("0x"+rand, 0)
    private_key = encoding.secret_exponent_to_wif(secret_exponent, compressed=True)
    public_pair = ecdsa.public_pair_for_secret_exponent(ecdsa.secp256k1.generator_secp256k1,secret_exponent)
    public_key1 = "04" + format(public_pair[0], 'x') + format(public_pair[1], 'x')

    """
    Generate split key
    email : Redeem code(other half of the private key) will be sent to this email address
    public_key1 : Pulbic key to be user to generate split key
    """
    post_request_data = { "public_key1" : public_key1, "email" : email } 
    response = requests.post(SPLIT_KEY_API, data=post_request_data)
    result = response.json()

    """ 
    Even if its gives us proper json response, we need to check for the status and error message
    """
    if "bitcoin_address" in result:

        """
        Send Redeem code from the server to registered email id
        """
        btc_address = result["bitcoin_address"]
        payload = {"bitcoin_address" : btc_address}
        response = requests.post(SEND_MAIL_API, data=payload)
        post_result = response.json()
        
        if "status" in post_result:
            print "[Send Mail] Error : " + post_result["message"]
        else:
            if redeem_url.endswith("/"):
                redeem_url = redeem_url[:-1]
            print "Redeem Link : " + redeem_url + "?key1=" + private_key + "&bitcoin_address=" + btc_address
            print "Bitcoin Address : " + btc_address
    else:
        print "[Split Key] Error : " + result["message"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", type=EmailType('RFC5322'), help="Receiver's Email Address.", required=True)
    parser.add_argument("--server", help="Server endpoint to create other half of the private key.", default=DEFAULT_REDEEM_ENDPOINT )

    args = vars(parser.parse_args())
    
    generate_redeem_code(args['email'], args['server'] )
