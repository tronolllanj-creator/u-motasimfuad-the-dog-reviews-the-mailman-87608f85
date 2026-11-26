"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Write a specific text line to the output directory as entry.txt.
"""

import os

LINE = "I barked my face off at him for four straight years until he finally stopped running away and now I have no idea why he keeps coming back to my yard to accept my yelling."


def main():
    content = LINE + "\n"
    
    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
    
    # Check for exactly one line (excluding the trailing newline if counted as terminator, or strictly one newline)
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    primary_path = os.path.join(output_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort to also write to /output/entry.txt if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
