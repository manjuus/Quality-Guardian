import csv
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path

EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)

def export_csv(job_id: str, testcases: list) -> str:
    out = EXPORT_DIR / f"{job_id}_testcases.csv"
    with out.open("w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "preconditions", "steps", "test_data", "expected", "priority"])
        for tc in testcases:
            writer.writerow([tc['id'], tc['title'], tc['preconditions'], " | ".join(tc['steps']), str(tc['test_data']), tc['expected_result'], tc['priority']])
    return str(out)

def export_pdf(job_id: str, requirement: dict, testcases: list) -> str:
    out = EXPORT_DIR / f"{job_id}_testplan.pdf"
    doc = SimpleDocTemplate(str(out), pagesize=A4)
    styles = getSampleStyleSheet()
    flow = []
    flow.append(Paragraph(f"Test Plan - {requirement.get('title')}", styles['Title']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph("Requirement:", styles['Heading2']))
    flow.append(Paragraph(requirement.get('raw_text', ''), styles['BodyText']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph("Test Cases:", styles['Heading2']))
    for tc in testcases:
        flow.append(Paragraph(tc['title'], styles['Heading3']))
        flow.append(Paragraph("Steps: " + "; ".join(tc['steps']), styles['BodyText']))
        flow.append(Paragraph("Expected: " + tc['expected_result'], styles['BodyText']))
        flow.append(Spacer(1, 6))
    doc.build(flow)
    return str(out)
