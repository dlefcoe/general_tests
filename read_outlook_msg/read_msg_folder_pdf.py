import subprocess
from pathlib import Path
from typing import cast

import extract_msg
from extract_msg import Message

BASE_DIR = Path("read_outlook_msg")
MESSAGES_DIR = BASE_DIR / "messages"
OUTPUT_DIR = BASE_DIR / "output_folder"


def convert_msg_to_pdf(
    input_file_name: str | Path,
    messages_folder: Path = MESSAGES_DIR,
    output_folder: Path = OUTPUT_DIR,
) -> Path:
    """Converts a single .msg file to .pdf and extracts attachments."""
    msg_path = Path(messages_folder) / input_file_name
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    # Generate output PDF name based on input file stem
    pdf_path = output_folder / f"{msg_path.stem}.pdf"
    temp_html = output_folder / f"temp_{msg_path.stem}.html"

    with extract_msg.openMsg(msg_path) as raw_msg:
        msg = cast(Message, raw_msg)

        # Save any attachments to the output folder
        for attachment in msg.attachments:
            attachment.save(customPath=str(output_folder))

        # Extract HTML/plain text body
        html_content = msg.htmlBody
        if html_content:
            if isinstance(html_content, str):
                html_content = html_content.encode("utf-8")
            temp_html.write_bytes(html_content)
        else:
            temp_html.write_text(f"<pre>{msg.body}</pre>", encoding="utf-8")

    # Render HTML to PDF via Edge
    edge_path = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
    subprocess.run(
        [
            edge_path,
            "--headless",
            "--disable-gpu",
            "--silent",
            "--log-level=3",
            f"--print-to-pdf={pdf_path.resolve()}",
            str(temp_html.resolve()),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Clean up temp file
    if temp_html.exists():
        temp_html.unlink()

    return pdf_path


def process_folder(
    input_folder: Path = MESSAGES_DIR,
    output_folder: Path = OUTPUT_DIR,
) -> list[Path]:
    """Processes all .msg files in a directory."""
    input_path = Path(input_folder)
    created_pdfs = []

    for file_path in input_path.glob("*.msg"):
        pdf_file = convert_msg_to_pdf(
            input_file_name=file_path.name,
            messages_folder=input_path,
            output_folder=output_folder,
        )
        created_pdfs.append(pdf_file)
        print(f"Saved: {pdf_file.name}")

    return created_pdfs


# Example Usage:
if __name__ == "__main__":
    # Convert all .msg files in the default messages folder
    process_folder()