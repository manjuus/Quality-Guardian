# Architecture Overview

1. Client -> POST /requirements -> Orchestrator
2. Orchestrator triggers Analyzer Agent (nlp.extract_features)
3. Orchestrator triggers Test Case Generator Agent (generator.generate_testcases) - parallelizable
4. Results saved to Job Store (jobs.py) and can be exported with exporter
5. Memory (memory.py) stores reviewer edits

Agents are simple Python modules in this prototype; in a production version they'd be microservices with an A2A protocol, tracing, and a job queue.
