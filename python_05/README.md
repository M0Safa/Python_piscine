## This project has been created as part of the 42 curriculum by [mosafa]<https://profile-v3.intra.42.fr/users/mosafa>

## introduction:

This project focuses on understanding and applying the concepts of inheritance and polymorphism in Python through stream processing. It demonstrates how object-oriented programming principles can be used to design flexible, reusable, and maintainable code while efficiently handling data streams.

## ex0: stream_processor

The goal of this exercise is to design an abstract DataProcessor class that defines the common structure and behavior for data processing tasks. Multiple specialized classes then inherit from this base class, each responsible for handling and validating a specific type of data, such as numeric, text, or log data. By overriding the parent class methods, each subclass customizes the processing logic while maintaining a consistent interface, demonstrating the effective use of inheritance and polymorphism in Python.

## ex1: data_stream

This exercise follows the same object-oriented design approach as the previous one, but focuses on processing data streams of different types, such as sensor readings, transactions, and events. Each stream is first filtered to remove invalid or unnecessary inputs, then processed according to its specific logic. The system uses inheritance and polymorphism to create specialized processors that handle each data type while sharing a common interface and structure.

## ex2: nexus_pipeline

In the final exercise, we design a flexible data pipeline capable of handling multiple data formats, such as JSON, CSV, and real-time streams. Each pipeline is composed of customizable stages — including input, transformation, and output — that work together to convert raw data into structured and usable information. The entire workflow is managed by a central NexusManager class, which coordinates the different components. This design highlights the use of protocol-based programming and duck typing, allowing different objects to interact seamlessly as long as they implement the required behavior, regardless of their specific types.


