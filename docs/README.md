# MARAGI Documentation

| M | Microservices |
| A | Architecture for |
| R | Robotics and |
| A | Artificial |
| G | General | 
| I | Intelligence |

- **M**icroservices 
- **A**rchitecture for 
- **R**obotics and 
- **A**rtificial 
- **G**eneral 
- **I**ntelligence

MARAGI is a system designed to make robotics and AGI accessible to everyone and to facilitate collaboration in the design, development, and research of AGI and robotics. 

## Installation

## MARAGI in 30 Seconds

# Concepts

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

## Disadvantages of Microservices

Individual microservices are very easy to understand, but a *microservices architecture* requires thinking about your application a bit differently. Then again, human brains and cognitive architectures are intrinsically complicated.

- The overall application can be more complicated
- Linking services together can be unintuitive at first
- Organizing your cognitive architecture with metadata is a novel concept

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
