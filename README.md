# MARAGI Stream of Consciousness 

MARAGI 
- Microservices 
- Architecture for 
- Robotics and 
- Artificial 
- General 
- Intelligence

This server is the core MARAGI service. The Stream of Consciousness (SOC) is a REST API microservice. This service allows an arbitrary number of microservices to post messages to the SOC and to fetch messages from the SOC.

# Usage

There are two basic functions when interacting with the SOC: 

- Adding messages
- Fetching messages

You can use the MARAGI client to perform either action. This service records the SOC in a JSON file. 

## Instantiate the SOC

The MARAGI client talks to the core MARAGI service, the Stream of Consciousness using REST API

```python
import maragi_soc
server = maragi_soc.Server()
# optional, specify port and SOC file
server = maragi_soc.Server(port=##, soc_file=##)
server.run()
```

## Communicate via the MARAGI Client

- [MARAGI Client on GitHub](https://github.com/daveshap/maragi_client)
- [MARAGI Client on PyPI](https://pypi.org/project/maragi-client/)

The MARAGI Client is a simple REST client. You can use this client to communicate witht he SOC. See the above links for examples and usage of the client. 

## Contribute and Collaborate 

This is a nascent project. Please contribute your expertise to make it better! 

- [Find more MARAGI projects on GitHub](https://github.com/topics/maragi)

# Installation

```python
pip install maragi-soc
```