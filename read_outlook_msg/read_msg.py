

from pathlib import Path
from typing import cast

import extract_msg
from extract_msg import Message

base_dir = Path("read_outlook_msg")
FILE_NAME = "DRAFT_ PLEASE REVIEW_ Fixed Income Desk Performance and Risk.msg"
msg_path = base_dir / "messages" / FILE_NAME
output_dir = base_dir / "output_folder"

output_dir.mkdir(parents=True, exist_ok=True)

# Context manager ensures the file handle closes properly
with extract_msg.openMsg(msg_path) as raw_msg:
    msg = cast(Message, raw_msg)

    print("Subject:", msg.subject)
    print("Sender:", msg.sender)
    print("Body:\n", msg.body)

    for attachment in msg.attachments:
        attachment.save(customPath=str(output_dir))

