# Python Linode API Wrapper

A python wrapper for the Linode's API that attempts to act just like the [Linode API](http://linode.com/api/linode) Docs say it will while being pythonic.


## Installation

    pip install linode


## Usage

This is currently alpha software but this example is what I'm aiming for.

    from linode import Api


    api = Api('your_api_key')
    api.linode.create(datacenterid, planid, paymentterm)
    api.linode.disk.createfromdistribution(linodeid, distributionid, label, size, rootpass, rootsshkey)


## Caveats

Any changes to the Linode docs.

### Variable Casing
All variables have been lower cased. The Linode API is case insensitive so this is not a true change from their docs at least.

### Variable Order
Required variables have been declared as positional arguments and optional variables as keyword arguments with a default of `None`. This means *all* optional arguments must come after required ones.

