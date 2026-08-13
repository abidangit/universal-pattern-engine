"""CLI entrypoint: run API or experiments."""
import argparse
import uvicorn
from src.pattern_engine.experiments.engine import run_experiment

parser = argparse.ArgumentParser(prog='upe')
sub = parser.add_subparsers(dest='cmd')

api = sub.add_parser('run-api')
api.add_argument('--host', default='127.0.0.1')
api.add_argument('--port', type=int, default=8000)

exp = sub.add_parser('run-exp')
exp.add_argument('--type', required=True)
exp.add_argument('--n', type=int, default=10)

if __name__ == '__main__':
    args = parser.parse_args()
    if args.cmd == 'run-api':
        uvicorn.run('pattern_engine.api.main:app', host=args.host, port=args.port, reload=False)
    elif args.cmd == 'run-exp':
        cfg = {'type': args.type, 'n': args.n}
        print(run_experiment(cfg))
    else:
        parser.print_help()
