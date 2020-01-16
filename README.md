# MARAGI 

## Links

- [Documentation @ maragi.io](https://maragi.io)
- [Python Package Index @ pypi.org](https://pypi.org/project/maragi/)

## Install

```python
pip install maragi
# or
python -m pip install maragi
```

## Server

```python
import maragi
server = maragi.Server()
server.run()
```

## Client

```python
import maragi
client = maragi.Client()
client.send(message)  # message is a dict with service, data, and metadata keys
data = client.fetch()
```
