## Version 0.0.2 - 2019-11-24

**Update**:

* Upgrade Python 3.6 to 3.8 for **but**
* Shorten daily build tagname


## Version 0.0.1 - 2019-11-22

**Update**:

* Migrate from [an63/butlite](https://hub.docker.com/r/an63/butlite) and [an63/but](https://hub.docker.com/r/an63/but)
* Add missing **ssh**, **unzip** and **netstat**
* Replace `ENTRYPOINT` with `CMD`

[**Source Code**](https://github.com/1set/but/releases/tag/0.0.1)

**Pull Last Build**:

```bash
# lite
docker pull 1set/butlite:0.0.1-f20a176-20191124

# full
docker pull 1set/but:0.0.1-f20a176-20191124-go1.13.4-node12.13.1-npm6.12.1-python3.6.8
```

**Last Build Content**:

* Go: 1.13.4
* Python: 3.6.8
* Node.js: 12.13.1
* npm: 6.12.1
