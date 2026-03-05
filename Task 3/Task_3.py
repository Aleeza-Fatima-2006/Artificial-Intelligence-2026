class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.previous_action = None  
    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"

        if action == self.previous_action:
            print("Action already done before.")
        else:
            print("New Action:", action)
        self.previous_action = action
        return action
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}
desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)
for room in rooms:
    temp = rooms[room]
    print("Room:", room)
    print("Temperature:", temp)
    agent.act(temp)