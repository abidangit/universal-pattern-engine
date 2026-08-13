"""FastAPI endpoints for analysis, generation, and discovery."""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any, Dict

from ..core.engine import Engine
from ..generators.arithmetic import arithmetic_sequence
from ..generators.geometric import geometric_sequence
from ..generators.fibonacci import fibonacci
from ..discovery.search import Discovery

app = FastAPI(title="Universal Pattern Engine API")
engine = Engine()
discoverer = Discovery()

class SeqIn(BaseModel):
    sequence: List[float]

class GenerateIn(BaseModel):
    type: str
    params: Dict[str, Any]

@app.post('/analyze')
def analyze(payload: SeqIn):
    return engine.analyze_sequence(payload.sequence)

@app.post('/discover')
def discover(payload: SeqIn):
    return discoverer.discover(payload.sequence)

@app.post('/generate')
def generate(payload: GenerateIn):
    t = payload.type.lower()
    p = payload.params
    if t == 'arithmetic':
        return {"sequence": arithmetic_sequence(p.get('start', 0), p.get('diff', 1), p.get('n', 10))}
    if t == 'geometric':
        return {"sequence": geometric_sequence(p.get('start', 1), p.get('ratio', 2), p.get('n', 10))}
    if t == 'fibonacci':
        return {"sequence": fibonacci(p.get('n', 10))}
    return {"error": "unknown generator"}
