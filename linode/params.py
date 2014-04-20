import requests


def get_required_params(api_url):
    url = '{0}/?api_action=api.spec'.format(api_url)
    r = requests.get(url)
    if not r.ok:
        raise

    required = {}
    for method, params in r.json()['DATA']['METHODS'].items():
        req = [x[0].lower() for x in filter(lambda x: x[1]['REQUIRED'], params['PARAMETERS'].items())]
        required[method.lower()] = req

    return required
