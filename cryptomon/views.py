from cryptomon import app
from cryptomon.ext_api.etherscan import EtherScan


@app.route('/get_last_price')
def get_last_price():
    api = EtherScan(
        app.config['ETHER_SCAN_API_ROOT'],
        app.config['ETHER_SCAN_API_KEY'],
    )

    return api.get_last_price()