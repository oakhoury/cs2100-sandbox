# Introduction

This example was created by Claude, when it was prompted to generate an example client application that can demonstrate encapsulation, inheritance, and polymorphism. It's been verified and edited by Alvaro Monge.

# Background
Your data lives in a dozen apps and none of them agree on anything: Spotify exports JSON in milliseconds, Netflix a CSV of `HH:MM:SS` strings, a fitness app uses minutes and local time. Connectors are the classes that tame them, and they sit at the **boundary**; pandas does the analysis in the middle.

* **Encapsulation**: (visibility, properties, immutability): a client that must not leak its secret, and a `StreamingSession` record that cannot be edited.
* **Inheritance and polymorphism**: a `Connector` base class, two subclasses, and one pipeline function that never asks which class it has.

All data is invented (shaped like real exports). Real exports contain usernames and IP addresses, so WARNING: if you try own data files, keep them on your own machine and DO NOT upload them to shared tools or AI systems.

## Commands (run from the top-level folder containing this README)

    pytest                                        # tests/ (3 pass)
    pytest exercises/encapsulation                # fails on the starter, on purpose
    CLIENT_MODULE=solutions.client pytest exercises/encapsulation      # solution: all pass
    python -m demos.encapsulation_demo

### Available once additional code is in repository
    python -m demos.inheritance_demo
    java java/ConnectorDemo.java                  # Java 16+
    mypy
