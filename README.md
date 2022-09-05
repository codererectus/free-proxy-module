## Python Free Proxy Module
___
### This module implements a class that parses a proxy from the Internet
___
simple example:

```
p = Proxy() 
proxies_list = p.get_selected_proxies()
```

In this example, we create a class object without any parameters and call a method that returns a proxy list.
This method takes the value from the local proxy file. If this file does not exist, it will be created.
___
another example:

```
p = Proxy(protocol='https', google=True, anon='elite', region='CA')
p.get_selected_proxies() # proxies list from cache (or update cache file)
...
p.update()  # update file with proxies
```
In this case, we create an object with our arguments and call a method that returns a proxy from a file.
We then call the method ``update()`` that parses the new proxies and update the file.
___
## How to install
___

clone the repository:

```git clone https://github.com/jsonstackhum/free-proxy-module.git```

I recommend creating a virtual environment:

```python3 -m venv env```


```pip install -Ur requirements.txt```


