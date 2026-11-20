import base64
import io
import os
from pathlib import Path
import sys
import zipfile
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

source = Path(sys.argv[1]).read_bytes()
destination = Path(sys.argv[2])
destination.mkdir(parents=True, exist_ok=True)
key = base64.b64decode(os.environ["ESC05_KEY"], validate=True)
archive_bytes = AESGCM(key).decrypt(source[:12], source[12:], b"ESC05-20261120")
with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
    archive.extractall(destination)
