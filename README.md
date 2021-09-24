# Ashyq

[![Financial Contributors](https://t.me/ashyqpy)](https://t.me/ashyqpy)
[![PyVersions](https://img.shields.io/pypi/pyversions/ashyq.svg?style=flat-square)](https://pypi.python.org/pypi/ashyq)
[![PyPi Package Version](https://img.shields.io/pypi/v/ashyq.svg?style=flat-square)](https://pypi.python.org/pypi/ashyq)
[![Downloads](https://img.shields.io/pypi/dm/ashyq.svg?style=flat-square)](https://pypi.python.org/pypi/ashyq)
[![Github issues](https://img.shields.io/github/issues/arynyklas/ashyq.svg?style=flat-square)](https://github.com/arynyklas/ashyq/issues)
[![MIT License](https://img.shields.io/pypi/l/ashyq.svg?style=flat-square)](https://opensource.org/licenses/MIT)

**ashyq** is a simple and (a-)synchronous framework for Private Ashyq API written in Python 3.7 with [requests](https://github.com/psf/requests) and [aiohttp](https://github.com/aio-libs/aiohttp). It helps you to get your status in Ashyq faster and simpler.


## Examples
<details>
  <summary>📚 Click to see some basic examples</summary>


### Simple `get user` request

```python
from ashyq import Ashyq


phone_number = ""
ashyq = Ashyq(phone_number)

ashyq.new_install()

code = ""
print(ashyq.connect(code))

print(ashyq.user)
```

### Moar!

You can find more examples in [`examples/`](https://github.com/arynyklas/ashyq/blob/master/examples) directory

</details>


## Official ashyq resources:
 - News and community: [@ashyqpy](https://t.me/ashyqpy)
 - Russian community: [@ashyqpy](https://t.me/ashyqpy)
 - PyPI: [ashyq](https://pypi.python.org/pypi/ashyq)
 - Source: [Github repo](https://github.com/arynyklas/ashyq)
 - Issues/Bug tracker: [Github issues tracker](https://github.com/arynyklas/ashyq/issues)
