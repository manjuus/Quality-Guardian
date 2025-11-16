from pydantic import BaseModel
from typing import List, Dict, Any

class Requirement(BaseModel):
    id: str
    title: str
    module: str
    raw_text: str

class TestCase(BaseModel):
    id: str
    requirement_id: str
    title: str
    preconditions: str
    steps: List[str]
    test_data: Dict[str, Any]
    expected_result: str
    priority: str = "Medium"
    reviewed: bool = False
