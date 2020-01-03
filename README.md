# MARAGI 

- **M**icroservices 
- **A**rchitecture for 
- **R**obotics and 
- **A**rtificial 
- **G**eneral 
- **I**ntelligence

MARAGI is a system designed to make robotics and AGI accessible to everyone and to facilitate collaboration in the design, development, and research of AGI and robotics. 

## Software Architectures

There are three primary software application design patterns, or architectures:

- Monolithic Architecture
- Service-Oriented Architecture (often abbreviated SOA)
- Microservices Architecture

## Advantages of Microservices

With microservices, each component of the larger whole is a small, "fine-grained" application. There are many advantages to this design paradigm:

- Microservices are easy to design and understand, meaning that each microservice is easy to develop and maintain
- Microservices have clearly defined boundaries and purposes, allowing for easy documentation and communication
- Microservices can focus on specific domains of knowledge or expertise, allowing developers to specialize without having to understand the entire system
- Microservices are highly portable, and can be packaged into virtual containers, rapidly deployed, and easily moved around

Microservices Architectures are ideally suited to large, complex systems. As robotics and artificial intelligence systems become more complex, MARAGI aims to democratize access to these technologies. 

## Types of Microservices

Microservices can do anything, but each one should focus on achieving one goal. This specialization allows each microservice to be very useful and very robus. Here are some examples of microservices:

- **Camera microservice**. This service would take input data from camera(s) and package the information up to be added to the maragi server, so that other microservices can consume real-time camera data.
- **Microphone microservice**. This service would serve an identical purpose, of taking information in from the outside world and adding it into the maragi system for other services.
- **Object Detection**. This would be an ML microservice that consumes images from the maragi system, interprets the images, and adds labels/inferences to the maragi system.
- **Automated Speech Recognition**. This service would consume audio data and publish inferences about speech.
- **Conversation Modeling**. This microservice would consume speech and chat information and propose verbal output responses.
- **Motor Actuation Services**. This service would be in control of motor outputs. 

As you can see, there are many domains of expertise that must work together in order to create a cohesive, intelligent machine. No single human could possibly have all the required knowledge and expertise. 

## Stream of Consciousness

Currently, our only model for strong intelligence is the human brain. Maragi is designed to approximate some of the most critical features of human intelligence, and by extension, human cognition. Intelligence 

# Server

The maragi server is the central nexus through which all other microservices can commmunicate. The server enables two primary types of interaction:

- Adding new messages to the *stream of consciousness*
- Fetching messages from the *stream of consciousness*

## Parameters

| Parameter | Default | About |
|---|---|---|
| port | 9999 | Network port for maragi to accept messages on |
| fields | ['time', 'uuid', 'service'] | Additional fields to instantiate SOC |
| soc_file | `soc.json` | File name or full file path to SOC log |

## Methods

| Method | Usage |
|---|---|
| load_soc() | Attempt to load SOC log from file |
| run() | Start maragi SOC server | 

## Usage 

```python
import maragi
server = maragi.Server(fields=['image', 'label'])
server.run()
```

# Client

## Parameters

| Parameter | Default | About |
|---|---|---|
| ip | `127.0.0.1` | Network IP address of maragi server |
| port | 9999 | Network port of maragi server |

## Methods

| Method | Description |
|---|---|
| send(message=`message`) | Send a message to the maragi server |
| fetch(field=`field`,keyword=`keyword`) | Fetch messages from the maragi server | 

## Usage 

```python
import maragi
client = maragi.Client()
client.get_fields()
```
