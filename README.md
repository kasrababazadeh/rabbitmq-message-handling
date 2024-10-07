# RabbitMQ message handling

### Overview

This project demonstrates the usage of RabbitMQ for message control using Python. We will cover the installation of RabbitMQ and Erlang, the creation of a message sender and receiver using the Pika library, and a comparison between RabbitMQ and MQTT protocols.

### Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [RabbitMQ Management Panel](#rabbitmq-management-panel)
- [Sending Messages](#sending-messages)
- [Receiving Messages](#receiving-messages)
- [Running the Project](#running-the-project)
- [Comparison of RabbitMQ and MQTT](#comparison-of-rabbitmq-and-mqtt)
- [Conclusion](#conclusion)
- [License](#license)

### Prerequisites

- Python installed on your machine
- RabbitMQ and Erlang installed

### Installation

1. Install RabbitMQ and Erlang on your system.
2. Access the RabbitMQ management panel at `http://localhost:15672`.
   - Use the username and password both set to `guest`.

### RabbitMQ Management Panel

Once logged in, you will see the management panel, where you can monitor your queues, exchanges, and messages.

### Sending Messages

1. To send messages, install the Pika library:
   ```bash
   pip install pika

### Running the Project

1. Open two terminals.

2. In the first terminal, run the receiver:

   ```bash
   python receive.py

3. In the second terminal, run the sender multiple times:

   ```bash
   python send.py

### Receiving Messages Confirmation

You should see the messages being received each time you run the sender.

### Comparison of RabbitMQ and MQTT

#### Purpose

- **MQTT**: Designed for small devices with low bandwidth.
- **RabbitMQ**: General-purpose messaging system.

#### Messaging Techniques

- **MQTT**: Utilizes only publish-subscribe.
- **RabbitMQ**: Supports multiple techniques including publish-subscribe, round-robin, and queues.

#### Transactions

- **MQTT**: Does not support transactions.
- **RabbitMQ**: Supports various acknowledgment types for transactions.

#### Target Audience

- **MQTT**: Ideal for IoT devices and low-power networks.
- **RabbitMQ**: Acts as a middleware for peer-to-peer data transfer and various messaging scenarios.

### Conclusion

This project demonstrates the fundamentals of RabbitMQ message control with Python. The difference between RabbitMQ and MQTT highlights the versatility and capabilities of RabbitMQ in various messaging scenarios.

### License

This project is licensed under the MIT License.
