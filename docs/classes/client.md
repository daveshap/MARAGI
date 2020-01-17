# Client Overview
## Quick Start
```python
from maragi import Client
client = Client()
client.send({})
client.fetch({})
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

# Client Attributes


# Client Methods
