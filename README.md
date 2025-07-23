🖼️ Secure Image Locker – XOR Cipher Tool
Cyber Security Internship - SkillCraft Technology
Task 02 | Track Code: CS

🔐 Overview
This is a simple image locking and unlocking tool developed in Python.
It uses a password-based XOR cipher to transform any image file (like .jpg, .png) into a secured version that can only be restored with the same password.

The program features a terminal-based interface and offers a smooth, menu-driven interaction flow.

⚙️ Features
🔑 Key-based locking system using user-defined passwords

❌ Rejects incorrect passwords using embedded signature validation

🖼️ Supports common image formats: .jpg, .jpeg, .png

🔄 Uses XOR cipher logic for bidirectional transformation

📋 Console-based, user-friendly menu interface

📊 Displays real-time progress during processing

🛠️ How It Works
User chooses an image to lock

Provides a custom secret key (password)

The tool applies XOR encryption and adds a hidden marker

To unlock, the same key is required to reverse the process

If the wrong password is used, the image remains encrypted and a warning is shown

🚀 Technologies Used
Python 3

File I/O and byte-level manipulation

XOR cipher technique

Terminal input/output for user interaction

🧪 Sample Output
mathematica
Copy
Edit
🔒 Secure Image Handler 🔒
1. Lock an image
2. Unlock an image
3. Quit

📁 Enter image filename (same directory): myphoto.png
🔑 Enter secret key: pass1234
Progress: 90%
✅ Success! File saved as: myphoto_locked.png
📌 Notes
Make sure to use the same secret key for locking and unlocking the file

Output file naming convention:

original_locked.jpg (locked/encrypted)

original_unlocked.jpg (unlocked/decrypted)

Avoid renaming or modifying encrypted files before unlocking them

✅ Status
Task 02 Completed ✔
Successfully submitted as part of the Cyber Security Internship at SkillCraft Technology.

