"""Simple rule-based requirement analyzer."""
from typing import List, Dict
import re

SENTENCE_END = re.compile(r"(?<=[.!?])\s+")

def split_sentences(text: str) -> List[str]:
    return [s.strip() for s in SENTENCE_END.split(text) if s.strip()]

def extract_features(raw_text: str) -> List[Dict]:
    sentences = split_sentences(raw_text)
    features = []
    for i, s in enumerate(sentences):
        if any(k in s.lower() for k in ["should", "must", "able to", "so that", "can ", "allows "]):
            features.append({
                "feature_id": f"feat_{i+1}",
                "summary": s,
                "acceptance_criteria": [s]
            })
    if not features:
        features.append({
            "feature_id": "feat_1",
            "summary": raw_text.strip(),
            "acceptance_criteria": [raw_text.strip()]
        })
    return features
