import os
import subprocess
import tempfile

from cryptography.fernet import Fernet


def connect_vpn():
    """FIXME"""
    VPN_CONF = r"C:\Program Files\OpenVPN\config\ULILLE_VPN_ETU_TCP_v4.ovpn"

    with open("vpn_auth.encrypted", "rb") as file:
        encrypted_data = file.read()
    with open("vpn_auth.key", "rb") as file:
        cipher_suite = Fernet(file.read())
    plain_text = cipher_suite.decrypt(encrypted_data).decode().replace('\r\n', '\n')

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as auth_file:
        auth_file.write(plain_text)
        auth_file.close()
        result = subprocess.run(["runas", "/user:Administrator",
                                 r"C:\Program Files\OpenVPN\bin\openvpn.exe", "--config", VPN_CONF,
                                 "--auth-user-pass", auth_file.name], check=True)

        os.unlink(auth_file.name)

    return result


def encrypt_file_and_store_key():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    with open("vpn_auth.txt", "rb") as file:
        data = file.read()
    cipher_text = cipher_suite.encrypt(data)
    with open("vpn_auth.encrypted", "wb") as file:
        file.write(cipher_text)
    with open("vpn_auth.key", "xb") as file:
        file.write(key)
