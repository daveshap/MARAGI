# Stream of Consciousness

Stream of consciousness microservice for AGI. The stream of consciousness is a nexus of thought. This service captures the key components of thought; time, context, and a descriptive experience. 

# SOC records

SOC records are comprised of a few basic components:

- time 
- class
- metadata
- message
- service

## time

A simple unix epoch time such as `1007937724.181841`.
The time is used to construction a temporally linear experience.
This allows different services to easily gather a context, which is especially for multimodal information as well as reconstructing time-series events.

## class

The class is a taxonomical text string such as `sense.audio.speech`.
Taxonomical strings such as this allow for arbitrarily complex classification.
Major senses, such as audio and video, tend to be simple to classify.
However, propioceptive senses can be incredibly specific, for instance `sense.orientation.left_arm.forearm` or `sense.pressure.left_hand.thumb.tip`.

## metadata

The metadata of a message is also an arbitrarily long string with similar construction as the class.
Where the class identifies the context of a message within the stream of consciousness, the metadata describes the message or payload.
In other words, the metadata can be thought of as labels, tags, and descriptions of the main payload. 
For example, a speech service may include the spoken words in the `message` and information about the speaker in the `metadata`, such as `male_voice.sarcastic_tone`.
Alternatively, an image recognition service may include confidence and description, such as `orange.upper_left_fov.confidence_86.5%` where the message is `roadcone`.

## service

The service indicates the originating service of the message. 
This is necessary for diagnostic purposes.
The stream of consciousness can have hundreds, thousands, or even tens of thousands of services contributing.
Thus, labeling the service is required for the sake of evaluating cause-and-effect as well as complex interactions between services.

## message

The message of the SOC record is an arbitrarily long string. The following are some examples:

- Speech service: `How now brown cow?`
- Enclopedia service: `Rome is a city on the Italian peninsula...`
