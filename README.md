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

## Examples of Microservices

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
- **Autobiographical Service**
  - This service records interactions and experiences to be recalled later. Can be used to compile training data or remember conversations with people from the past. 
- **Encyclopedia Service**
  - This service adds knowledge and facts based on current context, allowing the maragi system access to useful information. 

As you can see, there are many domains of expertise that must work together in order to create a cohesive, intelligent machine. No single human could possibly have all the required knowledge and expertise. 
These six microservices could, in theory, create a walking and talking robot. Furthermore, as more microservices become available, maragi can be quickly and easily extended. 

# Server

The maragi server is the central nexus through which all other microservices can commmunicate. The server enables two primary types of interaction:

- Adding new messages
- Fetching messages 

## Server Quick Start

Starting the maragi server takes only a couple lines of code. See! I told you it was easy! 

```python
import maragi
server = maragi.Server()
server.run()
```

That's it! It's that fast!

## Single Server

It is possible to create an entire maragi system with a single maragi server. This would mean that all messages and microservices communicate with a single instance of the maragi server. There are several advantages and disadvantages to this design:

- Simpler to design and deploy
- More resource intensive
- Generalized

## Multiple Servers

Many microservices may not need to communicate with each other. Furthermore, some functions may benefit from highly specialized designs, such as vision or motor planning. Because of this, you may want to setup several individual maragi servers.

- More complex to design and deploy
- Less resource intensive
- Specialized

# Client

The maragi client is a compact piece of code that allows you to quickly and easily interact with a maragi server. The client handles all the underlying communication so that you don't have to worry about it. 
The client can be used in any other microservice to standardize the interaction with the maragi server. 

## Client Quick Start

```python
import maragi
client = maragi.Client()
service = 'test_service'  # this is a string
data = ['this', 'is', 'data']  # any JSON serializable data
metadata = 'list.strings.tokens.sentence'  # this is a string
client.send(service=service, data=data, metadata=metadata)  # send the message to the server
messages = client.get_all()  # retrieve all messages from the server
```

## Client Fields

### Service

The `service` field is required. This records the originating service of a message, and is primarily for human-readability and diagnostic purposes. Consider that some MARAGI systems will be running dozens, hundreds, or even thousands of services. 

### Data

The `data` field must be JSON serializable. Beyond that, anything flies. You can pre-package it yourself if you like, into a string or leave it as a `list` or `dict` or whatever. If you're dealing with numpy arrays, you'll need to prepackage it.

### Metadata

The `metadata` field must be a string. This is a taxonomical description of the data. Remember, *metadata == data about the data*. The simplest and most obvious type of metadata is to describe the data type. Is the data a string? A list? An image? Audio?
Furthermore, you can describe the origin, provenance, or predicate of a piece of data. Let's say you've made an inference about an image and you want to include a reference back to the image. 
Now imagine that you have a speech recognition service that produces text strings but also includes information such as gender of the speaker, confidence, and other information. This is what the metadata field is for. 
Here are some examples:

- `string.sentence`
- `image.numpy`
- `image.labels.inference`