# Architecture

Phase 1 focuses on a small, well-tested mathematical core: sequence representations, generators, transforms, and simple discovery algorithms. An API and experiment runner expose this functionality for reproducible research and integration.

Components:
- pattern_engine.core: Sequence and Engine
- pattern_engine.generators: arithmetic, geometric, polynomial, recurrence, fibonacci
- pattern_engine.transforms: differences, ratios
- pattern_engine.analyzers: statistics
- pattern_engine.discovery: simple search heuristics
- API: FastAPI endpoints for analyze/discover/generate
- experiments: reproducible experiment runner
