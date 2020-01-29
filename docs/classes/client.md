---
title: Client
---

# Client

## Quick Start
```python
from maragi import Client
client = Client()
client.send({})
client.fetch({})
```

## Custom Fetch

The MARAGI server's fetch function will return all messages in the *stream of consciousness* by default. This gets very noisy very quickly, therefore you can filter the results based on `time`, `service`, `uuid`, and `metadata`.

```python
query = {'start':'<start time>', 'end':'<end time>', 'metadata':{'field':'to match'}}
messages = client.fetch(query)
```

# Methods

| Method | Arguments | Description |
|---|---|---|
| `send` | `payload` (dictionary) | Sends a message to the MARAGI server |
| `fetch` | `query` (dictionary) | Fetches messages from MARAGI server that match your query |

## Send

Send a message to the configured MARAGI server. This sends a `payload` which is a dictionary and has some required keys. All values must be JSON friendly. 

| Key | Datatype | Explanation |
|---|---|---|
| Service | `string` | Name of the service sending the message |
| Data | `any` | The core message, which could be a string, a vector, a matrix, etc, it just has to be JSON friendly |
| Metadata | `dictionary` | This information is used by other services to find the messages each service is providing. See below for more information about metadata and its importance |
| Time | `decimal` | Automatically added by MARAGI server, Unix Epoch time |
| UUID | `uuid v4` | Automatically added by MARAGI server |

## Fetch

Fetch messages from MARAGI server using `query` dictionary. The optional fields in the `query` dictionary are detailed here:

| Key | Datatype | Explanation |
|---|---|---|
| Start | `decimal` | Fetch messages occuring *on or after* specified time |
| End | `decimal` | Fetch messages occuring *on or before* specified time |
| UUID | `uuid v4` | Fetch message with specified UUID |
| Service | `string` | Fetch messages from specific service |
| Metadata | `dictionary` | Fetch messages with matching metadata fields |

The fetch function allows services to quickly and easily get information from MARAGI that they need. 

# Attributes

The client has the following attributes:

| Attribute | Datatype | Explanation |
|---|---|---|
| ip | `IP address, string` | IP address of the MARAGI server. Defaults to `127.0.0.1` (localhost) |
| port | `integer` | Network port of MARAGI server. Defaults to `9999` |
| default_query | `dictionary` | Allows you to create a standard query used by `fetch` method |
| default_metadata | `dictionary` | Allows you to create a standard metadata used by `send` method |

# Metadata

Metadata is the secret sauce of MARAGI. The purpose of metadata is to allow other services to find messages and data from other services. Metadata allows you to experiment with different organizations and cognitive architectures easily. 
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

