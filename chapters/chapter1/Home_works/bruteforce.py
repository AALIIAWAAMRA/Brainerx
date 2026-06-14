cipcher_message = "axeeh"

for i in range (26):
      decrypted_message = ""
      for char in cipcher_message:
         if char.isupper():
               decrypted_message += chr((ord(char) - i - 65) % 26 + 65)
         elif char.islower():
               decrypted_message += chr((ord(char) - i - 97) % 26 + 97)
         else:
               decrypted_message += char
      print(f"Key {i}: {decrypted_message}")