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

MARAGI is a system designed to make robotics and AGI accessible to everyone and to facilitate collaboration in the design, development, and research of AGI and robotics. MARAGI is a type of cognitive arcitecture.

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

# Microservices

Microservices in a nutshell:

- Tiny software programs
- Completely self-contained
- Talk to other programs with an API

## Examples

| Service | Description |
|---|---|
| **Camera** | Takes images from physical camera(s) device and publishes them to the MARAGI server |
| **Object Detection** | Consumes images from MARAGI server and performance inference, publishes what it "sees" back to the server |
| **Autobiography** | Records and stores events so that they can be recalled later |
| **Microphone** | Handles the audio data from a hardware microphone(s) |
| **Speech Recognition** | Consumes audio data and spits out speech inferences |
| **Conversation** | Consumes speech, chat, and conversation data and spits out responses | 

## Contribute

- [More MARAGI services on GitHub](https://github.com/topics/maragi)
- [More MARAGI packages on PyPI](https://pypi.org/search/?q=maragi)

Please consider writing your own microservices and publishing them on GitHub and/or PyPI! Please check out the [Microservices](https://maragi.io/pages/microservices.html)
