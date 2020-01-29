---
title: MARAGI
---

# Overview

- **M**icroservices 
- **A**rchitecture for 
- **R**obotics and 
- **A**rtificial 
- **G**eneral 
- **I**ntelligence

MARAGI is a system designed to make robotics and AGI accessible to everyone and to facilitate collaboration in the design, development, and research of AGI and robotics. MARAGI is a type of cognitive arcitecture, a framework that allows you to easily lay the plumbing and wiring to experiment with cognitive microservices. MARAGI creates a *pluggable architecture* where microservices can be rapidly developed and dropped into the MARAGI ecosystem. 

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
# go to http://127.0.0.1:9999 in a browser
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

# send the message
client.send(message)
# refresh your browser to see the message

# fetch messages
messages = client.fetch({})
```

MARAGI server defaults to http://127.0.0.1:9999

## Contribute

- [More MARAGI services on GitHub](https://github.com/topics/maragi)
- [More MARAGI packages on PyPI](https://pypi.org/search/?q=maragi)

Please consider writing your own microservices and publishing them on GitHub and/or PyPI! Please check out the [Microservices](https://maragi.io/pages/microservices.html)

# Mission

The mission of MARAGI is simple: Democratize access to AGI. This goal is ambitious, and we have several strategies by which we hope to achieve this goal.

## Lower Barriers

Machine Learning, Deep Learning, and Cognitive Architectures are all big, complex topics. The foremost objective of MARAGI is to lower the barrier of entry to these topics by creating a highly accessible ecosystem of microservices and a highly collaborative community. Lowering the barriers means producing great documentation, Agile methodology, user engagement, and providing education. Accessibility is the name of the game! 

## Facilitate Experimentation

General intelligence, cognition, spontaneous learning, and executive reasoning are all still unknown quantities. We can study neuroscience to glean some insights about how strong intelligence works, but we still do not have a strong theory of intelligence. MARAGI is designed to be flexible, allowing tinkerers and researchers to experiment with cognitive architectures, rapidly changing the plumbing and wiring of microservices so that we can work together to develop a solid theory of intelligence. 

## Massive Collaboration

MARAGI is merely the skeleton. The muscles and organs need to be added and these come in the form of microservices. Everyone with rudimentary programming skills should be able to get started with MARAGI. This will provide a springboard for thousands upon thousands of hobbiests, researchers, and tinkerers to all work together to create a vast, robust ecosystem of microservices. Think of it like creating a giant App Store for AGI microservices. 
