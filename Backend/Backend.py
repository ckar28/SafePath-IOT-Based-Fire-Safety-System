import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from collections import defaultdict
import heapq

# Set up Firebase credentials and initialize Firestore
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Replace with your service account key file
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to retrieve sensor data from Firestore
def retrieve_sensor_data():
    sensor_data = defaultdict(dict)
    docs = db.collection(u'sensor_data').stream()

    for doc in docs:
        node = doc.id
        data = doc.to_dict()
        temperature = data.get('temperature')
        smoke = data.get('smoke')
        timestamp = data.get('timestamp')
        sensor_data[node]['temperature'] = temperature
        sensor_data[node]['smoke'] = smoke
        sensor_data[node]['timestamp'] = timestamp

    return sensor_data

def assign_danger_level(data):
    danger_levels = []
    for entry in data:
        temp = entry[0]
        smoke = entry[1]
        
        danger_level = 1  # Default danger level
        
        # Assign danger level based on temperature
        if temp >= 100:
            danger_level = 5
        elif temp >= 80:
            danger_level = 4
        elif temp >= 60:
            danger_level = 3
        elif temp >= 40:
            danger_level = 2
        
        # Adjust danger level based on smoke
        if smoke >= 0.5:
            danger_level += 2
        elif smoke >= 0.3:
            danger_level += 1
        
        danger_levels.append(danger_level)
    
    return danger_levels

def update_danger_levels(graph, danger_levels):
    # Update the danger level for each node in the graph
    for i, node in enumerate(graph):
        graph[i][0] = danger_levels[i]

# Function to calculate the safest paths from each node to exit node using Dijkstra's algorithm
def calculate_safest_paths(graph, exit_node):
    # Create a dictionary to store the danger levels and paths from each node
    node_data = {node: {'danger_level': float('inf'), 'path': []} for node in graph}

    # Initialize the danger level of the exit node to 0
    node_data[exit_node]['danger_level'] = 0

    # Create a priority queue to store the nodes to be processed
    queue = [(0, exit_node)]

    while queue:
        danger_level, current_node = heapq.heappop(queue)

        # Check if a shorter path to the current node has already been found
        if danger_level > node_data[current_node]['danger_level']:
            continue

        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node]:
            new_danger_level = danger_level + weight

            # Update the danger level and path if a shorter path is found
            if new_danger_level < node_data[neighbor]['danger_level']:
                node_data[neighbor]['danger_level'] = new_danger_level
                node_data[neighbor]['path'] = node_data[current_node]['path'] + [neighbor]

                # Add the neighbor to the priority queue for further exploration
                heapq.heappush(queue, (new_danger_level, neighbor))

    # Return the safest paths for each node
    safest_paths = {node: node_data[node]['path'] for node in node_data}
    return safest_paths

# Function to update safest paths in Firestore
def update_safest_paths(safest_paths):
    # Erase previous safest paths
    db.collection(u'safest_paths').document(u'paths').delete()

    # Update the safest paths in Firestore
    db.collection(u'safest_paths').document(u'paths').set(safest_paths)

# Main function
def main():
    sensor_data = retrieve_sensor_data()
    danger_levels = assign_danger_level(data)

    graph = {
    1: [[1, 2], [1, 3]],
    2: [[1, 1], [1, 3], [1, 4]],
    3: [[1, 1], [1, 2], [1, 5]],
    4: [[1, 2], [1, 5], [1, 6]],
    5: [[1, 3], [1, 4], [1, 6]],
    6: [[1, 4], [1, 5]]
}

exit_node = 6  # Assuming node 6 is the exit node
    
    update_danger_levels(graph)
    safest_paths = calculate_safest_paths(graph,exit_node)
    update_safest_paths(safest_paths)

if __name__ == '__main__':
    main()







    
#     safest_paths = {
#     'node1': ['node2', 'node3', 'node4'],
#     'node2': ['node1', 'node3', 'node5', 'node6'],
#     'node3': ['node1', 'node4', 'node6'],
#     'node4': ['node2', 'node5', 'node6'],
#     'node5': ['node3', 'node6'],
#     'node6': []  # The exit node does not have any path beyond itself
# }
