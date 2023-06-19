# SafePath: Intelligent Fire Safety System

SafePath is an intelligent fire safety system designed to provide the safest evacuation routes in case of a fire emergency. It utilizes temperature and smoke sensors placed strategically within a building to monitor the environment and assess the risk levels in different areas. By analyzing real-time sensor data and applying the Dijkstra algorithm, SafePath calculates and updates the safest paths for evacuation, helping occupants make informed decisions during fire emergencies.

## Tech Stack

SafePath is built using the following technologies:

- Raspberry Pi: The Raspberry Pi acts as the central control unit and connects to the temperature and smoke sensors within the building.
- Python: The programming language used for developing the Raspberry Pi code, backend application, and data processing.
- Google Firestore: The cloud-based database service provided by Google Cloud Platform is used to store and manage the sensor data, danger levels, and safest paths.
- Flask: The Flask framework is used for developing the backend application and serving the frontend of SafePath.
- Dijkstra Algorithm: The Dijkstra algorithm is employed to calculate the safest evacuation routes based on the danger levels assigned to different areas within the building.
- Firebase Admin SDK: The Firebase Admin SDK is utilized to establish a connection between the backend application and Google Firestore for data retrieval and updates.

## Features

### Integration of temperature and smoke sensors
SafePath integrates temperature and smoke sensors placed throughout the building to continuously monitor the environment. The sensors gather real-time data on temperature levels and smoke concentrations, which are essential indicators of potential fire hazards.

### Calculation of danger levels based on sensor data
Using the data collected from the temperature and smoke sensors, SafePath calculates danger levels for different areas of the building. By analyzing the sensor readings, the system can assess the severity of the fire hazard in each location.

### Application of the Dijkstra algorithm to determine the safest evacuation routes
SafePath applies the Dijkstra algorithm to calculate the safest paths for evacuation from each node or area within the building. The algorithm considers the danger levels assigned to different areas and finds the shortest and safest routes to guide occupants to safety.

### Real-time updates of the safest paths in the cloud (Google Firestore)
The calculated safest paths are updated in real-time and stored in the cloud using Google Firestore. This ensures that the evacuation routes remain up-to-date and can be accessed by occupants in real-time.

### User-friendly frontend application for occupants to access the safest evacuation routes
SafePath provides a user-friendly frontend application that allows occupants within the building to access the safest evacuation routes. Using their mobile devices or computers, occupants can easily view the recommended paths and navigate to safety.

### Configurable and scalable system architecture
The SafePath system is designed with a configurable and scalable architecture, allowing it to adapt to various building layouts and sizes. The number and placement of sensors can be customized, and the system can scale to accommodate larger buildings or multiple interconnected structures.
