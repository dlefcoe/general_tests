
import subprocess
from pathlib import Path
from typing import cast

import extract_msg
from extract_msg import Message

base_dir = Path("read_outlook_msg")
input_file_name = "DRAFT_ PLEASE REVIEW_ Fixed Income Desk Performance and Risk.msg"
output_file_name = "email.pdf"
msg_path = base_dir / "messages" / input_file_name
temp_html = base_dir / "temp_email.html"
pdf_path = base_dir / "output_folder" / output_file_name

pdf_path.parent.mkdir(parents=True, exist_ok=True)

with extract_msg.openMsg(msg_path) as raw_msg:
    msg = cast(Message, raw_msg)
    
    # Use HTML body to preserve formatting; fall back to plain body if missing
    html_content = msg.htmlBody
    if html_content:
        if isinstance(html_content, str):
            html_content = html_content.encode("utf-8")
        temp_html.write_bytes(html_content)
    else:
        temp_html.write_text(f"<pre>{msg.body}</pre>", encoding="utf-8")

# Use Edge CLI to convert HTML to PDF
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

# Clean up the temporary HTML file
if temp_html.exists():
    temp_html.unlink()

print(f"Saved PDF to {pdf_path}")