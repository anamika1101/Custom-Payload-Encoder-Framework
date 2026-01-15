import base64
import random
import string
import codecs

# =====================================
# Encoding Functions
# =====================================

def base64_encode(payload):
    return base64.b64encode(payload.encode()).decode()

def xor_encode(payload, key):
    result = ""
    for char in payload:
        result += chr(ord(char) ^ key)
    return result

def rot13_encode(payload):
    return codecs.encode(payload, 'rot_13')


# =====================================
# Obfuscation Functions
# =====================================

def random_insertion(payload):
    junk = string.ascii_letters
    result = ""
    for char in payload:
        result += char + random.choice(junk)
    return result

def split_and_concat(payload):
    mid = len(payload) // 2
    return payload[mid:] + payload[:mid]

def escape_obfuscation(payload):
    result = ""
    for char in payload:
        result += "\\x" + format(ord(char), "02x")
    return result


# =====================================
# Detection Module
# =====================================

def signature_detection(payload):
    signatures = ["cmd.exe", "powershell", "whoami"]
    for sig in signatures:
        if sig.lower() in payload.lower():
            return "Detected"
    return "Not Detected"


# =====================================
# Main Program
# =====================================

def main():
    print("Custom Payload Encoder & Obfuscation Framework")
    print("---------------------------------------------")

    payload = input("Enter payload to test: ")

    print("\nOriginal Payload:")
    print(payload)
    print("Detection Result:", signature_detection(payload))

    print("\n--- Encoding Results ---")

    b64 = base64_encode(payload)
    print("\nBase64 Encoded:")
    print(b64)
    print("Detection Result:", signature_detection(b64))

    xor = xor_encode(payload, 5)
    print("\nXOR Encoded:")
    print(xor)
    print("Detection Result:", signature_detection(xor))

    rot = rot13_encode(payload)
    print("\nROT13 Encoded:")
    print(rot)
    print("Detection Result:", signature_detection(rot))

    print("\n--- Obfuscation Results ---")

    rand_obs = random_insertion(payload)
    print("\nRandom Insertion Obfuscation:")
    print(rand_obs)
    print("Detection Result:", signature_detection(rand_obs))

    split_obs = split_and_concat(payload)
    print("\nSplit & Concatenate Obfuscation:")
    print(split_obs)
    print("Detection Result:", signature_detection(split_obs))

    escape_obs = escape_obfuscation(payload)
    print("\nEscape Sequence Obfuscation:")
    print(escape_obs)
    print("Detection Result:", signature_detection(escape_obs))


if __name__ == "__main__":
    main()
