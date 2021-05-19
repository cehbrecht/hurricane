# Run locaust tests

## Install

Install locust requirements:
```
pip install -r requirements.txt
```

or

```
conda env create
```

## Run

Run:
```
locust -f locustfile.py
```

And select the ESGF data node to test in the web interface:
http://0.0.0.0:8089

### Using tags

You can use tags to run specific tests:
```
locust -f locustfile.py --tags catalog
```

Or exclude tags:
```
locust -f locustfile.py --exclude-tags cmip5
```

Existing tags:
* `catalog`
* `cmip5`
* `cmip6`


See:
* https://docs.locust.io/en/stable/writing-a-locustfile.html#tag-decorator


## Links

* https://locust.io/
* https://github.com/pglass/how-do-i-locust
