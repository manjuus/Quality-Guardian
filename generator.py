"""Template-driven test case generator."""
from models import TestCase
import uuid

PRIORITY_KEYWORDS = {
    "login": "High",
    "payment": "High",
    "error": "High",
}

def score_priority(text: str) -> str:
    t = text.lower()
    for k, v in PRIORITY_KEYWORDS.items():
        if k in t:
            return v
    return "Medium"

def generate_testcases(requirement_id: str, features: list) -> list:
    testcases = []
    for f in features:
        tid = str(uuid.uuid4())
        title = f"Verify: {f['summary'][:80]}"
        pre = "System in normal state"
        steps = [
            "Open the application",
            f"Perform action described: {f['summary']}",
            "Observe the result"
        ]
        expected = f['acceptance_criteria'][0]
        priority = score_priority(f['summary'])
        tc = TestCase(
            id=tid,
            requirement_id=requirement_id,
            title=title,
            preconditions=pre,
            steps=steps,
            test_data={"example": "data"},
            expected_result=expected,
            priority=priority
        )
        testcases.append(tc.dict())
    return testcases
