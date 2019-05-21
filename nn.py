import json

data = json.load(open("layer.json", "r"))

inputs = {}

for key, layer in data.items():
    for key, weight in layer["weights"].items():
        total_sum = 0
        for k, w in weight.items():
            if k not in inputs:
                inputs[k] = 1
            total_sum += eval(w) * inputs[k]

        inputs[key] = total_sum

print(inputs)

