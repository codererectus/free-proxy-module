## Python Free Proxy Module

### This module implements a class that parses a proxy from the Internet

Simple example:

```
from free_proxy import Proxy
...
p = Proxy() 
proxies_list = p.get_selected_proxies()
```

In this example, we create a class object without any parameters and call a method that returns a proxy list.
This method takes the value from the local proxy file. If this file does not exist, it will be created.
___
Another example:

```
p = Proxy(protocol='https', google=True, anon='elite', region='CA')
p.get_selected_proxies()
...
p.update()
```
In this case, we create an object with our arguments and call a method that returns a proxy from a file.
We then call the method ``update()`` that parses the new proxies and update the file.

### Possible arguments:

protocol - 'http', 'https', None

google - True, False, None

anon - 'elite', 'transparent', 'anonymous', None

region - 'CA', 'US', 'AU', 'RU', ... , None
## How to install:


Clone the repository:

```git clone https://github.com/jsonstackhum/free-proxy-module.git```

I recommend creating a virtual environment:

```python3 -m venv env```

Install dependencies:

```pip install -Ur requirements.txt```
___

