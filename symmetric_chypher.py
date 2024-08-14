msg = "this is my secret message"
key = 24

def symmetric_chypher(msg, key = 555):

    chyper_text = ""
    for m in msg:
        unicode = ord(m)
        after_xor = unicode ^ key
        chyper_m = chr(after_xor)
        chyper_text += chyper_m
    return chyper_text


encrypted = symmetric_chypher(msg)
print(encrypted)
decrypted = symmetric_chypher(encrypted)
print(decrypted)

