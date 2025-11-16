import json
from pathlib import Path
from typing import List, Dict

MEM_FILE = Path("memory_bank.json")

if not MEM_FILE.exists():
    MEM_FILE.write_text(json.dumps({"edits": [], "patterns": []}))

def load_memory() -> Dict:
    return json.loads(MEM_FILE.read_text())

def save_memory(obj: Dict):
    MEM_FILE.write_text(json.dumps(obj, indent=2))

def add_edit(edit: Dict):
    mem = load_memory()
    mem["edits"].append(edit)
    save_memory(mem)

def query_patterns(query: str) -> List[Dict]:
    mem = load_memory()
    return [p for p in mem.get("patterns", []) if query.lower() in p.get("example", "").lower()]
