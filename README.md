# Linode API Python Bindings
A thin python wrapper around [Linode's API](http://linode.com/api). Built with the idea of sticking to Linode's docs and being pythonic.

This is currently untested alpha software.

[![Build Status](https://secure.travis-ci.org/ghickman/linode.png?branch=master)](http://travis-ci.org/ghickman/linode)


## Installation

    pip install linode


## Usage

    from linode import Api

    api = Api('your_api_key')
    api.linode.create(datacenterid, planid, paymentterm)
    api.linode.disk.createfromdistribution(linodeid, distributionid, label, size, rootpass, rootsshkey)


## Tests
I has them.


## Caveats
Any deviations from the Linode docs.

### Variable Casing
All variables have been lower cased. The Linode API is case insensitive so this is not a true change from their docs.

### Variable Order
Required variables have been declared as positional arguments and optional variables as keyword arguments with a default of `None`. This means *all* optional arguments must come after required ones.

