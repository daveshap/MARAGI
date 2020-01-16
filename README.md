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

That's it! It's that fast! You can now go to a web browser, the default is http://127.0.0.1:9999 (this will redirect you to the web server)

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

The default client settings match the default server settings

```python
import maragi
client = maragi.Client()
message = {'service':'service_name', 'metadata':{'info':'about the data'}, 'data':'the actual data'}
client.send(message)
messages = client.fetch({})
```

## Metadata

The purpose of metadata is to allow other services to find messages and data from other services. Metadata allows you to experiment with different organizations and cognitive architectures easily. 
Human brains rely upon physical connections and physical connections to organize its architecture. Computers have no such restrictions, but organization is still critical. This is achieved through metadata. 
Below are some suggested fields. 

| Field | Examples | Explanation |
|---|---|---|
| Datatype | `string`, `ndarray`, `vector` | Simple label telling downstream services what kind of data is contained in the message. |
| Infotype | `image`, `fact`, `semantic vector` | More practical label providing context about the data. |
| Cortex | `visual`, `auditory`, `executive` | Highest order of organization in cognitive architecture. This can be used to organize certain types of services together. | 
| Domain | `sensory`, `motor`, `system` | Highest order of organization for the entire system. Can be used to organize services with functions outside of cognition. |
| Layer | `inference`, `evaluation` | Some cognitive architectures or models of cognition include layers, or subgroupings of functions that have similar functions. For example, you may have multiple visual inference services looking at the same images |
| Predicate | `<uuid>` | Most services consume messages from other services, all of which have UUIDs. It can be very useful to track a thread of messages, inferences, and results. |
| Thread/Origin | `<uuid>` | As with predicate, it can be helpful to be able to easily retrieve an entire "train of thought", so to speak. |

## Custom Fetch

The MARAGI server's fetch function will return all messages in the *stream of consciousness* by default. This gets very noisy very quickly, therefore you can filter the results based on `time`, `service`, `uuid`, and `metadata`.

```python
query = {'start':'<start time>', 'end':'<end time>', 'metadata':{'field':'to match'}}
messages = client.fetch(query)
```