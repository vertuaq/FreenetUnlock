GNU nano 6.2                                                                       decrypt.py
#!/usr/bin/env python3
'''
Copyright (C) 【Krispies™】

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# print a GPL notice
copyrightNotice = '''FreenetUnlock, Copyright (C) 2020  V3řtual_freeňet 【Krispies™】\n
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
'''
print(copyrightNotice)

from argparse import ArgumentParser

from typing import Callable, List, ByteString, Tuple, Dict, NewType

from base64 import b64decode

from Crypto.Hash import SHA1
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

valueMap: List[str] = [
    'payload',
    'payloadProxyURL',
    'shouldNotWorkWithRoot',
    'lockPayloadAndServers',
    'expiryDate',
    'hasNotes',
    'noteField2',
    'sshAddress',
    'onlyAllowOnMobileData',
    'unlockRemoteProxy',
    'unknown',
    'vpnAddress',
    'sslSni',
    'shouldConnectUsingSSH',
    'udpgwPort',
    'lockPayload',
    'hasHWID',
    'hwid',
    'noteField1',
    'unlockUserAndPassword',
    'sslAndPayloadMode',
    'enablePassword',
    'password'
]

xorList = ['。', '〃', '〄', '々', '〆', '〇', '〈', '〉', '《', '》', '「', '」', '『', '』', '【', '】', '〒', '〓', '〔', '〕']

def decrypt(contents, key):
    decryption_key = SHA1.new(data=bytes(key, 'utf-8')).digest()[:16]

    return AES.new(decryption_key, AES.MODE_ECB).decrypt(contents)

def deobfuscate(contents):
    encrypted_string = contents.decode('utf-8')
    deobfuscated_contents = b''

    for index in range(len(encrypted_string)):
        deobfuscated_contents += bytes([ord(encrypted_string[index]) ^ ord(xorList[index % len(xorList)])])

    return b64decode(deobfuscated_contents)

embeddedKeyList = '''1:hc_reborn___7
1:hc_reborn_tester
1:hc_reborn_tester_5
