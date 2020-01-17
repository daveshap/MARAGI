---
title: MARAGI Server Class
---

# Server Overview

## Quick Start

```python
from maragi import Server
server = Server()
server.run()
```

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

# Class Methods

## run()

# Class Attributes

## port

## ip
