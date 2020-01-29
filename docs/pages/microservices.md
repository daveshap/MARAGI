---
title: Microservices
---

# Microservices

## What are Microservices?

- Tiny self-contained programs
- Talk to other programs via API
- Can be easily containerized (such as Docker)
- Interchangeable
- Easy to design and maintain

For more information, I recommend reading up on [Wikipedia: Microservices](https://en.wikipedia.org/wiki/Microservices)

## Why Microservices?

Intelligence, reasoning, and learning are all huge, complex tasks. It's too big and complex for a single human, or even a single team of humans, to comprehend. You can spend a lifetime studying just one domain, such as visual processing, and still not master it. Because of this complexity, AGI will be achieved by collaboration between many domain experts. Each aspect of intelligence can be worked on by individual teams and experts. MARAGI allows for the creation of a pluggable architecture, where new microservices can be easily added to the greater whole. 

# Design

MARAGI microservices all have two basic functions: *input* and *output*. This simplicity is reflected in the design of the MARAGI client and server. The third, hidden function is *processing*. Each microservice should process the information it takes in and produce something novel as part of the output. 

## Input

The input of a microservice can be an external device, such as a camera or microphone. Microservices can also consume the output of other microservices. Some microservices are dedicated to interacting with sensors, such as cameras, microphones, orientation, acceleration, and any other kind of hardware sensor. Other microservices rely on the input from other microservices. For instance, an object detection microservice relies on the input from camera microservices. 

## Output

The output of microservices can be deep learning inferences, raw data, evaluations, motor controls, or other output. Inference microservices consume data of some form and evaluate it with machine learning models. Hardware microservices take information from devices and translate it into JSON-friendly messages, such as raw video images or audio segments. 

# Create your own

MARAGI, at its core, is meant to be an ecosystem of microservices. The success of MARAGI relies on the participation and contribution of independent programmers, researchers, students, and professionals. 
