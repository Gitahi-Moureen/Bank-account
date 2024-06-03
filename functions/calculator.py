# def add (x,y):
#     result = x+y
#     return result

# def divide(a,b):
#     result = a/b
#     return result

# def multiply(c,d):
#     result = c*d
#     return result

# def sum(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total 

# def multiply_many(*digits):
#     total = 1
#     for digit in digits:
#         total *= digit
#     return total 

class AnkaraFabric:
    def __init__(self, base_design):
        self.base_design = base_design

    def predict_design_change(self, temperature, mood):
        # Simulated logic for predicting design change based on temperature and mood
        if temperature > 25 and mood == 'happy':
            return "Vibrant floral pattern"
        elif temperature < 15:
            return "Subdued geometric shapes"
        else:
            return "Standard Ankara design"

# Simulated temperature and mood data
temperature = 30
mood = 'happy'

fabric = AnkaraFabric("Traditional print")
predicted_design = fabric.predict_design_change(temperature, mood)
print(f"Predicted fabric design: {predicted_design}")
