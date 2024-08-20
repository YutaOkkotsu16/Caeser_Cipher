# Caeser_Cipher

This Python script cracks Caesar cipher encrypted text by trying all 26 possible shifts.

## Features

- Reads input from stdin
- Processes multiple lines of text
- Preserves non-alphabetic characters
- Outputs all 26 possible decryptions

## How it works

1. Reads input lines
2. For each shift (0-25):
   - Creates mapping dictionaries
   - Shifts each letter in the input
   - Prints the result

## Note

- Only processes lowercase letters
- Uppercase letters will remain unchanged
