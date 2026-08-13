"""Experiment runner for reproducible experiments with persistence."""
import json
from typing import Dict, Any
from ..db.session import get_session, init_db
from ..db.models import ExperimentResult

class Experiment:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def run(self) -> Dict[str, Any]:
        # Minimal runner: record config and a trivial result
        result = {"config": self.config, "observations": [], "metrics": {}, "status": "done"}
        # Example: run a simple generator experiment
        if self.config.get('type') == 'arithmetic':
            start = self.config.get('start', 0)
            diff = self.config.get('diff', 1)
            n = self.config.get('n', 10)
            seq = [start + i * diff for i in range(n)]
            result['observations'].append({'sequence': seq})
            result['metrics']['length'] = len(seq)
        # Persist result
        try:
            init_db()
            db = get_session()
            er = ExperimentResult(
                experiment_name=self.config.get('name', 'experiment'),
                config=self.config,
                observations=result['observations'],
                metrics=result.get('metrics'),
                status=result['status']
            )
            db.add(er)
            db.commit()
            result['db_id'] = er.id
        except Exception:
            # don't fail experiments due to persistence issues
            result['db_id'] = None
        finally:
            try:
                db.close()
            except Exception:
                pass
        return result

def run_experiment(config: Dict[str, Any]) -> Dict[str, Any]:
    e = Experiment(config)
    return e.run()
