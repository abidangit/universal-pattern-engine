"""Experiment runner for reproducible experiments."""
import json
from typing import Dict, Any

class Experiment:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def run(self) -> Dict[str, Any]:
        # Minimal runner: record config and a trivial result
        result = {"config": self.config, "observations": [], "status": "done"}
        # Example: run a simple generator experiment
        if self.config.get('type') == 'arithmetic':
            start = self.config.get('start', 0)
            diff = self.config.get('diff', 1)
            n = self.config.get('n', 10)
            seq = [start + i * diff for i in range(n)]
            result['observations'].append({'sequence': seq})
        return result

def run_experiment(config: Dict[str, Any]) -> Dict[str, Any]:
    e = Experiment(config)
    return e.run()
