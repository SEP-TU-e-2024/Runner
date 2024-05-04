import psutil
import sys
import datetime
import time

class Runner():
    #----------------------------------------------------------------
    # PUBLIC METHODS
    #----------------------------------------------------------------
    def __init__(self, config: dict):
        self.config: dict = config
        self.target: psutil.Popen = None

    def run(self):
        start_wall_time = time.time()

        with open(self.config['target']['logs'], '+a') as f:
            f.write(f'Time: {datetime.datetime.now()}\tConfig settings:\n{self.config}\nTarget output:\n')
            self.target = psutil.Popen(self.config['target']['args'], stdout=f)
        
        while self.target.poll() == None:
            self.update_metrics()
            time.sleep(config['runner']['tick_delay'])

        print(f'Target return status: {self.target.wait()}')
        print(f"Rough wall time: {time.time() - start_wall_time}")        
    
    #----------------------------------------------------------------
    # PRIVATE METHODS
    #----------------------------------------------------------------
    def update_metrics(self):
        with self.target.oneshot():
            print(self.target.cpu_percent())
            print(self.target.memory_full_info())

#----------------------------------------------------------------
# Testing
#----------------------------------------------------------------
if __name__ == "__main__":
    import json

    with open('config.json', 'r') as f:
        config = json.load(f)
        r = Runner(config)
        r.run()