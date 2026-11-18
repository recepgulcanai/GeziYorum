#!/usr/bin/env python3
"""GeziYorum şifreleme aracı. Şifre repoda tutulmaz; GEZI_SIFRE ortam değişkeniyle verilir.
  şifrele : python3 build.py enc <paket.html> <gezi.enc>
  çöz     : python3 build.py dec <gezi.enc> <paket.html>
Biçim: salt(16) | iv(12) | AES-256-GCM( html ), anahtar PBKDF2-SHA256 (ITER tur)."""
import os, sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
ITER = 300000
def key(pw, salt):
    return PBKDF2HMAC(hashes.SHA256(), 32, salt, ITER).derive(pw.encode())
pw = os.environ['GEZI_SIFRE']
mode, src, dst = sys.argv[1:4]
data = open(src, 'rb').read()
if mode == 'enc':
    salt, iv = os.urandom(16), os.urandom(12)
    ct = AESGCM(key(pw, salt)).encrypt(iv, data, None)
    open(dst, 'wb').write(salt + iv + ct)
else:
    salt, iv, ct = data[:16], data[16:28], data[28:]
    open(dst, 'wb').write(AESGCM(key(pw, salt)).decrypt(iv, ct, None))
