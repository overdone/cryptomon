import requests


class EtherScan:
    """ Api for access to etherscan.io """

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_last_price(self):
        """ Returns last ethereum price in usd """

        price = ''
        payload = {
            'module': 'stats',
            'action': 'ethprice',
            'apikey': self.api_key
        }

        try:
            r = requests.get(self.base_url, payload)

            if r.status_code == 200:
                data = r.json()
                price = data['result']['ethusd']

        except requests.exceptions.RequestException as ex:
            print('get_lat_price error: {err}'.format(err=str(ex)))

        return price
