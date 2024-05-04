import psutil
import time
import csv

class Runner():
    #----------------------------------------------------------------
    # PUBLIC METHODS
    #----------------------------------------------------------------
    def __init__(self, config: dict):
        self.config: dict = config
        self.target: psutil.Popen = None
        self.metrics: list[dict] = list()

        print(f'Settings: {config}')

    def run(self):
        start_wall_time = time.time()

        with open(self.config['target']['log'], '+w') as f:
            self.target = psutil.Popen(self.config['target']['args'], stdout=f)
        
        while self.target.poll() == None:
            self.metrics.append(self.target.as_dict(attrs=self.config['runner']['metrics']['attrs']))
            time.sleep(config['runner']['tick_delay'])

        self.write_metrics()

        print(f'Target return status: {self.target.wait()}')
        print(f"Rough wall time: {time.time() - start_wall_time}")        
    
    #----------------------------------------------------------------
    # PRIVATE METHODS
    #----------------------------------------------------------------
    def write_metrics(self):
        flat_metrics: list[dict] = [self.flatten_metric(metric) for metric in self.metrics]

        with open(self.config['runner']['metrics']['out'], '+w') as f:
            dict_writer = csv.DictWriter(f, flat_metrics[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(flat_metrics)
    
    def flatten_metric(self, metric: dict) -> dict:
        flat = dict()

        for key, metric_val in metric.items():
            if isinstance(metric_val, int | float | str | bool):
                flat[key] = metric_val
            else:  # Should be a named tuple according to the psutils docs
                for name, tuple_val in metric_val._asdict().items():
                    flat[f'{key}-{name}'] = tuple_val

        return flat



#----------------------------------------------------------------
# Testing
#----------------------------------------------------------------
if __name__ == "__main__":
    import json

    with open('config.json', 'r') as f:
        config = json.load(f)
        r = Runner(config)
        r.run()