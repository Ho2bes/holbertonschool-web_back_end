# Caching Algorithms Project

## Background Context

In this project, you will learn different caching algorithms.

## Resources

To better understand the concepts covered in this project, you can refer to the following resources:

- [Cache replacement policies - FIFO](#)
- [Cache replacement policies - LIFO](#)
- [Cache replacement policies - LRU](#)
- [Cache replacement policies - MRU](#)
- [Cache replacement policies - LFU](#)

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- The purpose of a caching system
- The limitations of a caching system

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should use the pycodestyle style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- Documentation is not just a word, it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).

## More Info

### Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
