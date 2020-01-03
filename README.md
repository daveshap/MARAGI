# MARAGI 

- `M`icroservices 
- `A`rchitecture for 
- `R`obotics and 
- `A`rtificial 
- `G`eneral 
- `I`ntelligence

## Microservices Architecture

There are three primary software application design patterns, or architectures:

- Monolithic Architecture
- Service-Oriented Architecture (often abbreviated SOA)
- Microservices Architecture

With microservices, each component of the larger whole is a small, "fine-grained" application. There are many advantages to this design paradigm:

- Microservices are easy to design and understand, meaning that each microservice is easy to develop and maintain
- Microservices have clearly defined boundaries and purposes, allowing for easy documentation and communication
- Microservices can focus on specific domains of knowledge or expertise, allowing developers to specialize without having to understand the entire system
- Microservices are highly portable, and can be packaged into virtual containers, rapidly deployed, and easily moved around

# Server

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
