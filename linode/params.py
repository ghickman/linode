import requests


def get_required_params(api_url):
    """
    Build a dictionary of actions with required parameters

    Consume the api.spec data and create a dictionary with actions as keys and
    their required parameters in a list.

    For example:

        {
            'linode.create': ['foo', 'bar']
        }
    """
    url = '{0}/?api_action=api.spec'.format(api_url)
    r = requests.get(url)
    if not r.ok:
        raise

    required = {}
    for method, options in r.json()['DATA']['METHODS'].items():
        parameters = options['PARAMETERS'].items()

        required_only = filter(lambda x: x[1]['REQUIRED'], parameters)
        required[method.lower()] = [name.lower() for name, _ in required_only]

    return required
