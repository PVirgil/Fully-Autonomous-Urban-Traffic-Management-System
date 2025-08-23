import numpy as np
import random
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
import networkx as nx

class TrafficManagementSystem:
    """
    Autonomous traffic management system for urban environments.
    """

    def __init__(self, num_intersections=10):
        self.intersections = self._generate_intersections(num_intersections)
        self.traffic_model = RandomForestRegressor()
        self.routing_model = KMeans(n_clusters=3)

    def _generate_intersections(self, num):
        """
        Simulate an urban road network with intersections.
        """
        graph = nx.grid_2d_graph(int(np.sqrt(num)), int(np.sqrt(num)))
        return graph

    def collect_traffic_data(self):
        """
        Simulate data collection from IoT devices.
        """
        traffic_data = {
            node: {"traffic_flow": random.randint(50, 500), "accidents": random.choice([0, 1])}
            for node in self.intersections.nodes
        }
        return traffic_data

    def optimize_traffic_lights(self, traffic_data):
        """
        Optimize traffic light timings based on real-time data.
        """
        for intersection, data in traffic_data.items():
            flow = data["traffic_flow"]
            if data["accidents"] > 0:
                light_duration = 0  # Stop all traffic
            elif flow > 300:
                light_duration = 60  # Longer green light
            else:
                light_duration = 30  # Standard green light

            traffic_data[intersection]["optimized_light_duration"] = light_duration
        return traffic_data

    def predict_traffic_congestion(self, traffic_data):
        """
        Predict future congestion using machine learning.
        """
        features = np.array([list(data.values()) for data in traffic_data.values()])
        congestion_scores = self.traffic_model.predict(features)
        return {
            intersection: congestion_score
            for intersection, congestion_score in zip(traffic_data.keys(), congestion_scores)
        }

    def reroute_traffic(self, traffic_data, congestion_threshold=400):
        """
        Reroute traffic to reduce congestion.
        """
        high_congestion_nodes = [
            node for node, data in traffic_data.items() if data["traffic_flow"] > congestion_threshold
        ]
        rerouted_paths = nx.shortest_path(self.intersections, weight="traffic_flow")
        return {node: rerouted_paths[node] for node in high_congestion_nodes}

    def run(self):
        """
        Run the traffic management system.
        """
        # Collect data
        traffic_data = self.collect_traffic_data()
        print("Collected traffic data:", traffic_data)

        # Optimize traffic lights
        optimized_data = self.optimize_traffic_lights(traffic_data)
        print("Optimized traffic light durations:", optimized_data)

        # Predict congestion
        congestion_predictions = self.predict_traffic_congestion(optimized_data)
        print("Predicted congestion scores:", congestion_predictions)

        # Reroute traffic
        reroutes = self.reroute_traffic(optimized_data)
        print("Rerouted paths for high-congestion areas:", reroutes)

if __name__ == "__main__":
    tms = TrafficManagementSystem()
    tms.run()

