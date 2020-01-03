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

- Easy to design and understand
- Clearly defined boundaries and purpose
- Highly specialized, focused on specific domain
- Flexible and portable, easy to deploy and modify
- Language agnostic, use any programming language

Microservices Architectures are ideally suited to large, complex systems. As robotics and artificial intelligence systems become more complex, MARAGI aims to democratize access to these technologies. 

## Types of Microservices

Microservices can do anything, but each one should focus on achieving one goal. This specialization allows each microservice to be very useful and very robus. Here are some examples of microservices:

- **Camera Service**
  - This service would take input data from camera(s) and package the information up to be added to the maragi server, so that other microservices can consume real-time camera data.
- **Microphone Service**
  - This service would serve an identical purpose, of taking information in from the outside world and adding it into the maragi system for other services.
- **Object Detection**
  - This would be an ML microservice that consumes images from the maragi system, interprets the images, and adds labels/inferences to the maragi system.
- **Automated Speech Recognition**
  - This service would consume audio data and publish inferences about speech.
- **Conversation Modeling**
  - This microservice would consume speech and chat information and propose verbal output responses.
- **Motor Actuation Services**
  - This service would be in control of motor outputs. 

As you can see, there are many domains of expertise that must work together in order to create a cohesive, intelligent machine. No single human could possibly have all the required knowledge and expertise. 
These six microservices could, in theory, create a walking and talking robot. 

# Server

The maragi server is the central nexus through which all other microservices can commmunicate. The server enables two primary types of interaction:

- Adding new messages
- Fetching messages 

All maragi microservices contribute to the whole via *messages*. Messages are analogous to *thoughts*, in that they contain information, ideas, memories, sensory information, facts, and so on. 
Messages can contain different types of data. Some messages may contain images or audio data, where others contain sentences or paragraphs, and yet more may contain spatial information such as maps or world models. 
The core function of the maragi server is to facilitate communication between all other microservices. The maragi server makes it easy for anyone to spin up a complex AGI or robotics system!

## Server Quick Start

Starting the maragi server takes only a couple lines of code. See! I told you it was easy! 

```python
import maragi
server = maragi.Server(fields=['image', 'label'])
server.run()
```

## Single Server

It is possible to create an entire maragi system with a single maragi server. This would mean that all messages and microservices communicate with a single instance of the maragi server. There are several advantages and disadvantages to this design:

- Simple design and planning
- Single point of contact
- Potentially more noise to filter

## Multiple Servers

Many microservices may not need to communicate with each other. Furthermore, some functions may benefit from highly specialized designs, such as vision or motor planning. Because of this, you may want to setup several individual maragi servers.

- Increasingly complex to design
- More points of contact to keep track of
- More specialized, purpose-built
- Less noise to sift through

# Client

The maragi client is a compact piece of code that allows you to quickly and easily interact with a maragi server. The client handles all the underlying communication so that you don't have to worry about it. 
The client can be used in any other microservice to standardize the interaction with the maragi server. 

## Client Quick Start

```python
import maragi
client = maragi.Client()  # instantiate the client
message = {'service': 'demo_service'}  # compose a test message
client.send(message)  # send the message to the server
messages = client.fetch_all()  # retrieve all messages from the server
```
