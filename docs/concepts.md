# Concepts and Core Design

This document explains core concepts used throughout the Universal Pattern Engine:

- Pattern: a standard internal object with id, name, category, parameters, initial_conditions, generator, transformations, sequence, statistics, complexity, entropy, confidence, and metadata.
- Pipeline stages: Generate → Transform → Analyze → Discover → Experiment → Persist
- Generators: deterministic (arithmetic, geometric, polynomial, recurrence), stochastic, chaotic, learned
- Transforms: differences, ratios, accumulation, derivatives
- Analyzers: statistics, entropy, periodicity, growth, classifier
- Discovery: candidate generation, scoring (MSE), mutation/evolution, confidence estimation

Design principles:
- Start with math, then add search and ML
- Small modular components with clear interfaces
- Reproducibility: experiments are parameterized, seeded, and persisted
