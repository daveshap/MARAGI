# MARAGI Documentation

- **M**icroservices 
- **A**rchitecture for 
- **R**obotics and 
- **A**rtificial 
- **G**eneral 
- **I**ntelligence

MARAGI is a system designed to make robotics and AGI accessible to everyone and to facilitate collaboration in the design, development, and research of AGI and robotics. 

## Installation

[MARAGI on PyPI](https://pypi.org/project/maragi/)

```python
pip install maragi
# or
python -m pip install maragi
```

## MARAGI in 30 Seconds

Instantiate a server in Python

```python
import maragi
server = maragi.Server()
server.run()
# go to http://127.0.0.1:9999
```

Create a client in a second instance of Python

```python
import maragi
client = maragi.Client()

# compose a message
message = {}
message['service'] = 'test service'
message['data'] = 'this is a test message'
message['metadata'] = {'type': 'text/string'}

client.send(message)
```

# Concepts

## Microservices Architecture

### Software Architectures

There are three primary software application design patterns, or architectures:

- Monolithic Architecture
- Service-Oriented Architecture (often abbreviated SOA)
- Microservices Architecture

### Advantages

With microservices, each component of the larger whole is a small, "fine-grained" application. There are many advantages to this design paradigm:

- Easy to design and understand
- Clearly defined boundaries and purpose
- Highly specialized, focused on specific domain
- Flexible and portable, easy to deploy and modify
- Language agnostic, use any programming language

Microservices Architectures are ideally suited to large, complex systems. As robotics and artificial intelligence systems become more complex, MARAGI aims to democratize access to these technologies. 

### Disadvantages

Individual microservices are very easy to understand, but a *microservices architecture* requires thinking about your application a bit differently. Then again, human brains and cognitive architectures are intrinsically complicated.

- The overall application can be more complicated
- Linking services together can be unintuitive at first
- Organizing your cognitive architecture with metadata is a novel concept

### Examples

| Service | Description |
|---|---|
| **Camera** | Takes images from a physical camera device and publishes them to the MARAGI server |
| **Object Detection** | Consumes images from MARAGI server and performance inference, publishes what it "sees" back to the server |
| **Autobiography** | Records and stores events so that they can be recalled later |
