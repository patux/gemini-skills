#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Adapt Spain Spanish text into Mexican Spanish.

Features:
- UTF-8 safe
- Capitalization preservation
- Safer regex replacements
- Backup support
- Dry-run mode
- Output file support
- Extensible vocabulary dictionary

Usage:
    python adapt_spanish.py input.txt
    python adapt_spanish.py input.txt -o output.txt
    python adapt_spanish.py input.txt --dry-run
"""

import re
import argparse
import shutil
import unicodedata
from pathlib import Path


# -------------------------------------------------------------------
# Vocabulary replacements
# -------------------------------------------------------------------

VOCABULARY_MAP = {
    # Pronouns
    r"\bvosotros\b": "ustedes",
    r"\bvosotras\b": "ustedes",
    r"\bvuestro\b": "su",
    r"\bvuestra\b": "su",
    r"\bvuestros\b": "sus",
    r"\bvuestras\b": "sus",

    # Common Spain vocabulary
    r"\bcoche\b": "carro",
    r"\bordenador\b": "computadora",
    r"\bmóvil\b": "celular",
    r"\bconducir\b": "manejar",
    r"\bzumo\b": "jugo",
    r"\bgafas\b": "lentes",
    r"\bautobús\b": "camión",
    r"\bpatata\b": "papa",
    r"\bacera\b": "banqueta",
    r"\bcoger\b": "tomar",  # Important regional adaptation
}


# -------------------------------------------------------------------
# Helper functions
# -------------------------------------------------------------------

def preserve_case(original: str, replacement: str) -> str:
    """
    Preserve capitalization style from original text.
    """
    if original.isupper():
        return replacement.upper()

    if original[0].isupper():
        return replacement.capitalize()

    return replacement


def safe_replace(pattern: str, replacement: str, text: str) -> str:
    """
    Perform safe regex replacement preserving capitalization.
    """

    regex = re.compile(pattern, flags=re.IGNORECASE)

    def repl(match):
        original = match.group(0)
        return preserve_case(original, replacement)

    return regex.sub(repl, text)


def normalize_utf8(text: str) -> str:
    """
    Normalize Unicode text.
    """
    return unicodedata.normalize("NFC", text)


# -------------------------------------------------------------------
# Linguistic adaptation
# -------------------------------------------------------------------

# Safer vosotros verb conversions
# Avoid replacing words like "país"

def replace_vosotros_verbs(text: str) -> str:
    exceptions = {
        "país",
        "País",
        "PAÍS",
    }
    patterns = [
        (r"\b(\w+)áis\b", r"\1an"),
        (r"\b(\w+)éis\b", r"\1en"),
        (r"\b(\w+)ís\b", r"\1en"),
    ]
    for pattern, replacement in patterns:
        regex = re.compile(pattern, flags=re.IGNORECASE)
        def repl(match):
            word = match.group(0)
            if word in exceptions:
                return word
            return re.sub(pattern, replacement, word, flags=re.IGNORECASE)
        text = regex.sub(repl, text)
    return text

def adapt_to_mexican_spanish(text: str) -> str:
    """
    Adapt Peninsular Spanish into Mexican Spanish.
    """

    text = normalize_utf8(text)

    # Vocabulary replacements
    for pattern, replacement in VOCABULARY_MAP.items():
        text = safe_replace(pattern, replacement, text)

    # Safer vosotros verb conversions
    # NOTE:
    # This remains heuristic.
    # Full conjugation conversion would require NLP libraries.

    verb_patterns = [
        (r"\b(\w+)áis\b", r"\1an"),
        (r"\b(\w+)éis\b", r"\1en"),
        (r"\b(\w+)ís\b", r"\1en"),
    ]
    text = replace_vosotros_verbs(text)

    return text


# -------------------------------------------------------------------
# File processing
# -------------------------------------------------------------------

def process_file(input_path: Path,
                 output_path: Path = None,
                 backup: bool = True) -> None:

    with open(input_path, "r", encoding="utf-8") as f:
        original_text = f.read()

    adapted_text = adapt_to_mexican_spanish(original_text)

    # Default output behavior
    if output_path is None:
        output_path = input_path

    # Backup original file
    if backup and output_path == input_path:
        backup_path = input_path.with_suffix(input_path.suffix + ".bak")
        shutil.copy2(input_path, backup_path)
        print(f"[INFO] Backup created: {backup_path}")

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(adapted_text)

    print(f"[INFO] Adapted file written to: {output_path}")


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="Adapt Spain Spanish UTF-8 text files to Mexican Spanish."
    )

    parser.add_argument(
        "input_file",
        help="Input UTF-8 text file"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Optional output file"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print adapted text without modifying files"
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Do not create backup files"
    )

    args = parser.parse_args()

    input_path = Path(args.input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        original_text = f.read()

    adapted_text = adapt_to_mexican_spanish(original_text)

    if args.dry_run:
        print(adapted_text)
        return

    output_path = Path(args.output) if args.output else None

    process_file(
        input_path=input_path,
        output_path=output_path,
        backup=not args.no_backup
    )


if __name__ == "__main__":
    main()
