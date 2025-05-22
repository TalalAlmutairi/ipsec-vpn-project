# Simulated Federated Learning for 5G Network Slicing Security

import random

def local_training():
    print("Training local model...")
    accuracy = round(random.uniform(0.80, 0.95), 4)
    return {"accuracy": accuracy, "weights": [random.random() for _ in range(10)]}

def central_aggregation(results):
    print("Aggregating local models...")
    avg_accuracy = sum(r['accuracy'] for r in results) / len(results)
    print(f"Average accuracy after aggregation: {avg_accuracy:.4f}")

if __name__ == "__main__":
    print("Simulating federated learning...")
    nodes = 5
    results = [local_training() for _ in range(nodes)]
    central_aggregation(results)