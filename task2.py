import os
from time import sleep

MARKER = b'IMGLOCK'  # Signature to verify decryption integrity

def xor_lock_unlock(file_path, secret):
    if not os.path.isfile(file_path):
        print("🚫 Error: File not found.")
        return

    with open(file_path, 'rb') as image:
        content = bytearray(image.read())

    key_bytes = bytearray(secret.encode())
    key_size = len(key_bytes)

    is_encrypting = not file_path.endswith('_locked.jpg') and not file_path.endswith('_locked.png')

    if is_encrypting:
        content = bytearray(MARKER) + content  # Add signature before encryption

    print("\n🔧 Working on it...")
    for idx in range(len(content)):
        content[idx] ^= key_bytes[idx % key_size]
        if idx % (len(content)//10 + 1) == 0:
            print(f"Progress: {int((idx / len(content)) * 100)}%", end='\r')
            sleep(0.01)

    if not is_encrypting:
        if content[:len(MARKER)] != MARKER:
            print("❗ Decryption error: Incorrect password.")
            return
        content = content[len(MARKER):]  # Remove signature after decryption

    result_path = generate_output_filename(file_path)
    with open(result_path, 'wb') as out_file:
        out_file.write(content)

    print(f"\n✅ Success! File saved as: {result_path}")

def generate_output_filename(original_name):
    name_part, extension = os.path.splitext(original_name)
    if name_part.endswith('_locked'):
        return name_part[:-7] + '_unlocked' + extension
    else:
        return name_part + '_locked' + extension

def user_interface():
    while True:
        print("\n🔒 Secure Image Handler 🔒")
        print("1. Lock an image")
        print("2. Unlock an image")
        print("3. Quit")

        user_choice = input("Select an option (1-3): ").strip()

        if user_choice == '1':
            file_name = input("📁 Enter image filename (same directory): ").strip()
            key = input("🔑 Enter secret key: ").strip()
            xor_lock_unlock(file_name, key)

        elif user_choice == '2':
            file_name = input("📂 Enter locked image filename: ").strip()
            key = input("🔑 Enter secret key: ").strip()
            xor_lock_unlock(file_name, key)

        elif user_choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid selection. Try again.")

if __name__ == "__main__":
    user_interface()
