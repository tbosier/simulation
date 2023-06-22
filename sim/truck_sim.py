import simpy
import random

# Global variable to keep track of total repair costs
total_repair_cost = 0
total_breakdowns = 0

class Truck:
    def __init__(self, env, name, maintenance_shop):
        self.env = env
        self.name = name
        self.broken = False
        self.maintenance_shop = maintenance_shop
        self.distance_driven = 0
        self.breakdown_probability = 0.01  # starting probability of breaking down

        # Start the truck process
        self.action = env.process(self.run())

    def run(self):
        global total_repair_cost
        global total_breakdowns
        while True:
            # Drive for a week
            yield self.env.timeout(7)
            
            # Increment the distance driven
            self.distance_driven += random.gauss(1000, 200)  # hypothetical distribution

            # Check if the truck has broken down
            if random.random() < self.breakdown_probability:
                self.broken = True
                self.env.process(self.maintenance())

            # Increase the probability of breaking down as the weeks go by
            self.breakdown_probability += 0.01

    def maintenance(self):
        yield self.env.timeout(1)  # Truck is out of market for 1 day
        self.broken = False
        cost = 1500
        global total_repair_cost
        total_repair_cost += cost
        global total_breakdowns
        total_breakdowns += 1


# Create the simulation environment
env = simpy.Environment()

# Create a maintenance shop resource (assuming infinite capacity)
maintenance_shop = simpy.Resource(env, capacity=float("inf"))

# Create n trucks
n = 10000
trucks = [Truck(env, f'Truck-{i}', maintenance_shop) for i in range(n)]

# Run the simulation for x days
days = 180
env.run(until=days)

# Output the total repair cost
print(f"Total repair cost for all trucks: ${total_repair_cost}")
print(f"Total breakdowns over {days} days")