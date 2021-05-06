import yaml

CONFIGURATION = None;
with open('configuration.yaml','w') as input_stream:
    yaml.dump([{"nee":40}],input_stream)
