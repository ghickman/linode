# Python Linode API Wrapper

A python wrapper for the Linode's API that attempts to act just like the [Linode API](http://linode.com/api/linode) Docs say it will while being pythonic.


## Installation

    pip install linode


## Usage

    from linode import Api


    linode = Api('your_api_key')
    linode.create(datacenter_id, plan_id, payment_term)
    linode.disk.createfromdistribution(linode_id, distribution_id, label, size, root_pass, root_ssh_key)

