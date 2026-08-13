from celery import Celery
from ..experiments.engine import run_experiment
from ..db.session import get_session, init_db
from ..db.models import ExperimentResult

celery_app = Celery('upe', broker='redis://localhost:6379/0')

@celery_app.task
def run_experiment_task(config: dict):
    # Run experiment and persist via experiments.engine (it already attempts persistence)
    result = run_experiment(config)
    return result

@celery_app.task
def persist_result(result: dict):
    try:
        init_db()
        db = get_session()
        er = ExperimentResult(
            experiment_name=result.get('config', {}).get('name', 'experiment'),
            config=result.get('config'),
            observations=result.get('observations'),
            metrics=result.get('metrics'),
            status=result.get('status')
        )
        db.add(er)
        db.commit()
        db.refresh(er)
        db_id = er.id
        db.close()
        return {'db_id': db_id}
    except Exception as e:
        return {'error': str(e)}
