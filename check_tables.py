from docx import Document
import re

doc = Document('Latchwork_Technical_Documentation.docx')

# Check tables
for i, table in enumerate(doc.tables):
    print(f"Table {i}: {len(table.rows)} rows x {len(table.columns)} cols")
    if table.rows:
        first_row = [cell.text[:30] for cell in table.rows[0].cells]
        print(f"  Headers: {first_row}")
