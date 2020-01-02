# maragi 

**maragi**
- Microservices 
- Architecture for 
- Robotics and 
- Artificial 
- General 
- Intelligence

# Server

## Parameters

| Parameter | Default | About |
|---|---|---|---|
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
|---|---|---|---|
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
