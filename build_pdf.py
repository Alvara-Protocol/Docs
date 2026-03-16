#!/usr/bin/env python3
"""Build a single PDF from all Alvara documentation markdown files."""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable
)

DOCS_DIR = "/Users/cal/Documents/GitHub/Docs/docs"
OUTPUT = "/Users/cal/Documents/GitHub/Docs/Alvara-Documentation.pdf"

# Ordered list of sections and their files, following SUMMARY.md
SECTIONS = [
    ("Welcome", [
        ("README.md", None),
    ]),
    ("Getting Started", [
        ("getting-started/what-is-alvara.md", None),
        ("getting-started/core-concepts.md", None),
        ("getting-started/connecting-your-wallet.md", None),
        ("getting-started/supported-networks.md", None),
    ]),
    ("BSKTs", [
        ("bskts/what-is-a-bskt.md", None),
        ("bskts/exploring-bskts.md", None),
        ("bskts/investing-in-a-bskt.md", None),
        ("bskts/redeeming-your-position.md", None),
        ("bskts/understanding-performance.md", None),
    ]),
    ("BSKT Lab", [
        ("bskt-lab/creating-a-bskt.md", None),
        ("bskt-lab/composing-your-allocation.md", None),
        ("bskt-lab/designing-your-bskt.md", None),
        ("bskt-lab/funding-and-deployment.md", None),
    ]),
    ("Fund Managers", [
        ("managers/overview.md", None),
        ("managers/rebalancing.md", None),
        ("managers/emergency-controls.md", None),
        ("managers/claiming-fees.md", None),
        ("managers/leaderboard.md", None),
        ("managers/identity.md", None),
    ]),
    ("Staking & veALVA", [
        ("staking/what-is-vealva.md", None),
        ("staking/lock-types.md", None),
        ("staking/how-to-stake.md", None),
        ("staking/staking-rewards.md", None),
    ]),
    ("DAO Governance", [
        ("dao/how-the-dao-works.md", None),
        ("dao/gauge-weight-voting.md", None),
        ("dao/epochs.md", None),
        ("dao/claiming-dao-rewards.md", None),
    ]),
    ("ALVA Token", [
        ("alva-token/overview.md", None),
        ("alva-token/tokenomics.md", None),
        ("alva-token/erc-7621.md", None),
    ]),
    ("Security", [
        ("security/audits.md", None),
        ("security/mev-protection.md", None),
        ("security/risk-disclosures.md", None),
    ]),
    ("Resources", [
        ("resources/faq.md", None),
        ("resources/glossary.md", None),
        ("resources/community.md", None),
        ("resources/disclaimer.md", None),
    ]),
]

# Colors
PINK = HexColor("#E84393")
DARK_BG = HexColor("#1A1530")
PURPLE_DARK = HexColor("#2D1B4E")
TEXT_MUTED = HexColor("#6B7280")
LINK_COLOR = HexColor("#E84393")


def build_styles():
    """Create custom paragraph styles."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="DocTitle",
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=34,
        textColor=PINK,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="DocSubtitle",
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=TEXT_MUTED,
        spaceAfter=30,
    ))
    styles.add(ParagraphStyle(
        name="SectionHeader",
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=26,
        textColor=PINK,
        spaceBefore=0,
        spaceAfter=14,
    ))
    styles.add(ParagraphStyle(
        name="PageTitle",
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=24,
        textColor=black,
        spaceBefore=0,
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="H2",
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=20,
        textColor=HexColor("#111827"),
        spaceBefore=16,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="H3",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=HexColor("#374151"),
        spaceBefore=12,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="H4",
        fontName="Helvetica-BoldOblique",
        fontSize=11,
        leading=14,
        textColor=HexColor("#374151"),
        spaceBefore=10,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="BodyText2",
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=HexColor("#374151"),
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BulletItem",
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=HexColor("#374151"),
        leftIndent=20,
        spaceAfter=3,
        bulletIndent=8,
    ))
    styles.add(ParagraphStyle(
        name="NumberItem",
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=HexColor("#374151"),
        leftIndent=20,
        spaceAfter=3,
        bulletIndent=8,
    ))
    styles.add(ParagraphStyle(
        name="CodeBlock",
        fontName="Courier",
        fontSize=8,
        leading=11,
        textColor=HexColor("#1F2937"),
        backColor=HexColor("#F3F4F6"),
        leftIndent=12,
        rightIndent=12,
        spaceBefore=4,
        spaceAfter=8,
        borderPadding=(6, 6, 6, 6),
    ))
    styles.add(ParagraphStyle(
        name="TOCSection",
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=22,
        textColor=PINK,
        spaceBefore=10,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="TOCItem",
        fontName="Helvetica",
        fontSize=10,
        leading=18,
        textColor=HexColor("#374151"),
        leftIndent=16,
    ))
    styles.add(ParagraphStyle(
        name="BoldText",
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=15,
        textColor=HexColor("#374151"),
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="HRule",
        fontName="Helvetica",
        fontSize=4,
        leading=10,
        spaceAfter=8,
        spaceBefore=8,
    ))

    return styles


def escape_xml(text):
    """Escape XML special characters for ReportLab paragraphs."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def process_inline(text):
    """Process inline markdown: bold, italic, code, links."""
    # Inline code (must be first to avoid nested processing)
    text = re.sub(r'`([^`]+)`', r'<font name="Courier" size="9" color="#E84393">\1</font>', text)
    # Bold + italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'<font color="#E84393">\1</font>', text)
    return text


def parse_markdown_to_flowables(md_text, styles, is_first_page=False):
    """Convert markdown text to ReportLab flowables."""
    flowables = []
    lines = md_text.split("\n")
    i = 0
    in_code_block = False
    code_lines = []
    in_table = False
    table_rows = []
    first_heading_skipped = False

    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith("```"):
            if in_code_block:
                # End code block
                code_text = escape_xml("\n".join(code_lines))
                flowables.append(Paragraph(code_text.replace("\n", "<br/>"), styles["CodeBlock"]))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Table detection
        if "|" in line and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # Check if separator row
            if all(re.match(r'^[-:]+$', c) for c in cells):
                i += 1
                continue
            table_rows.append(cells)
            # Peek ahead to see if table continues
            if i + 1 < len(lines) and "|" in lines[i + 1] and lines[i + 1].strip().startswith("|"):
                i += 1
                continue
            else:
                # End of table, render it
                if table_rows:
                    # Process inline formatting in cells
                    processed_rows = []
                    for row in table_rows:
                        processed_row = []
                        for cell in row:
                            cell_text = process_inline(cell)
                            processed_row.append(Paragraph(cell_text, styles["BodyText2"]))
                        processed_rows.append(processed_row)

                    # Normalize column count
                    max_cols = max(len(r) for r in processed_rows)
                    for row in processed_rows:
                        while len(row) < max_cols:
                            row.append(Paragraph("", styles["BodyText2"]))

                    col_width = (letter[0] - 2 * inch) / max_cols
                    t = Table(processed_rows, colWidths=[col_width] * max_cols)
                    t.setStyle(TableStyle([
                        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#F3F4F6")),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTSIZE", (0, 0), (-1, -1), 9),
                        ("TEXTCOLOR", (0, 0), (-1, -1), HexColor("#374151")),
                        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#E5E7EB")),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("TOPPADDING", (0, 0), (-1, -1), 4),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                        ("LEFTPADDING", (0, 0), (-1, -1), 6),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ]))
                    flowables.append(Spacer(1, 4))
                    flowables.append(t)
                    flowables.append(Spacer(1, 6))
                    table_rows = []
                i += 1
                continue

        stripped = line.strip()

        # Empty line
        if not stripped:
            i += 1
            continue

        # Horizontal rule
        if stripped in ("---", "***", "___"):
            flowables.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#E5E7EB")))
            i += 1
            continue

        # Headings
        if stripped.startswith("# "):
            heading_text = process_inline(stripped[2:])
            if not first_heading_skipped and not is_first_page:
                # Use PageTitle for the first H1 (page title)
                flowables.append(Paragraph(heading_text, styles["PageTitle"]))
                first_heading_skipped = True
            elif is_first_page:
                flowables.append(Paragraph(heading_text, styles["DocTitle"]))
                first_heading_skipped = True
            else:
                flowables.append(Paragraph(heading_text, styles["PageTitle"]))
            i += 1
            continue
        elif stripped.startswith("## "):
            heading_text = process_inline(stripped[3:])
            flowables.append(Paragraph(heading_text, styles["H2"]))
            i += 1
            continue
        elif stripped.startswith("### "):
            heading_text = process_inline(stripped[4:])
            flowables.append(Paragraph(heading_text, styles["H3"]))
            i += 1
            continue
        elif stripped.startswith("#### "):
            heading_text = process_inline(stripped[5:])
            flowables.append(Paragraph(heading_text, styles["H4"]))
            i += 1
            continue

        # Bullet points
        if re.match(r'^[-*]\s', stripped):
            bullet_text = process_inline(stripped[2:])
            flowables.append(Paragraph(
                f"<bullet>&bull;</bullet> {bullet_text}",
                styles["BulletItem"]
            ))
            i += 1
            continue

        # Numbered list
        num_match = re.match(r'^(\d+)\.\s(.*)', stripped)
        if num_match:
            num = num_match.group(1)
            text = process_inline(num_match.group(2))
            flowables.append(Paragraph(
                f"<bullet>{num}.</bullet> {text}",
                styles["NumberItem"]
            ))
            i += 1
            continue

        # Regular paragraph
        para_text = process_inline(stripped)
        flowables.append(Paragraph(para_text, styles["BodyText2"]))
        i += 1

    return flowables


def build_cover_page(styles):
    """Build the cover/title page."""
    flowables = []
    flowables.append(Spacer(1, 2 * inch))
    flowables.append(Paragraph("Alvara Protocol", styles["DocTitle"]))
    flowables.append(Spacer(1, 8))
    flowables.append(Paragraph("Documentation", ParagraphStyle(
        name="CoverSub",
        fontName="Helvetica",
        fontSize=18,
        leading=24,
        textColor=TEXT_MUTED,
    )))
    flowables.append(Spacer(1, 24))
    flowables.append(HRFlowable(width="40%", thickness=2, color=PINK))
    flowables.append(Spacer(1, 24))
    flowables.append(Paragraph(
        "Decentralized asset management built on the Basket Token Standard (ERC-7621)",
        ParagraphStyle(
            name="CoverDesc",
            fontName="Helvetica",
            fontSize=11,
            leading=16,
            textColor=TEXT_MUTED,
        )
    ))
    flowables.append(Spacer(1, inch))
    flowables.append(Paragraph(
        "app.alvara.xyz",
        ParagraphStyle(
            name="CoverLink",
            fontName="Helvetica",
            fontSize=10,
            textColor=PINK,
        )
    ))
    flowables.append(PageBreak())
    return flowables


def build_toc(styles):
    """Build the table of contents."""
    flowables = []
    flowables.append(Paragraph("Table of Contents", styles["DocTitle"]))
    flowables.append(Spacer(1, 16))

    for section_name, files in SECTIONS:
        flowables.append(Paragraph(section_name, styles["TOCSection"]))
        for filepath, _ in files:
            # Read first line to get title
            full_path = os.path.join(DOCS_DIR, filepath)
            if os.path.exists(full_path):
                with open(full_path, "r") as f:
                    first_line = f.readline().strip()
                    title = first_line.lstrip("# ").strip()
                    if title == "Welcome to Alvara":
                        title = "Welcome"
                    flowables.append(Paragraph(title, styles["TOCItem"]))

    flowables.append(PageBreak())
    return flowables


def add_page_number(canvas, doc):
    """Add page numbers and a subtle footer."""
    page_num = canvas.getPageNumber()
    if page_num <= 2:  # Skip cover + TOC
        return
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawCentredString(letter[0] / 2, 0.5 * inch, f"{page_num}")
    # Subtle top line
    canvas.setStrokeColor(HexColor("#E5E7EB"))
    canvas.setLineWidth(0.5)
    canvas.line(inch, letter[1] - 0.6 * inch, letter[0] - inch, letter[1] - 0.6 * inch)
    # Header text
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(inch, letter[1] - 0.55 * inch, "Alvara Protocol Documentation")
    canvas.restoreState()


def main():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        topMargin=0.8 * inch,
        bottomMargin=0.7 * inch,
        leftMargin=inch,
        rightMargin=inch,
        title="Alvara Protocol Documentation",
        author="Alvara Protocol",
        subject="Protocol documentation for Alvara — decentralized asset management on ERC-7621",
    )

    styles = build_styles()
    story = []

    # Cover page
    story.extend(build_cover_page(styles))

    # Table of contents
    story.extend(build_toc(styles))

    # Content
    for section_idx, (section_name, files) in enumerate(SECTIONS):
        # Section header page
        if section_idx > 0:  # Skip for Welcome (it IS the first content)
            story.append(Paragraph(section_name, styles["SectionHeader"]))
            story.append(HRFlowable(width="100%", thickness=1.5, color=PINK))
            story.append(Spacer(1, 12))

        for file_idx, (filepath, _) in enumerate(files):
            full_path = os.path.join(DOCS_DIR, filepath)
            if not os.path.exists(full_path):
                print(f"  WARNING: {full_path} not found, skipping")
                continue

            with open(full_path, "r") as f:
                md_text = f.read()

            is_first = (section_idx == 0 and file_idx == 0)
            flowables = parse_markdown_to_flowables(md_text, styles, is_first_page=is_first)
            story.extend(flowables)

            # Add spacing between files in same section, page break between sections
            if file_idx < len(files) - 1:
                story.append(Spacer(1, 20))
                story.append(HRFlowable(width="30%", thickness=0.5, color=HexColor("#E5E7EB")))
                story.append(Spacer(1, 16))

        # Page break after each section
        if section_idx < len(SECTIONS) - 1:
            story.append(PageBreak())

    # Build
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF generated: {OUTPUT}")
    print(f"Total sections: {len(SECTIONS)}")
    total_files = sum(len(files) for _, files in SECTIONS)
    print(f"Total pages of content: {total_files}")


if __name__ == "__main__":
    main()
