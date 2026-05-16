---
name: book-typesetter
description: Professional multilingual book typesetting for PDF and EPUB using LaTeX and Pandoc. Use when creating or refining high-quality book projects with modular structures, dynamic covers, and classical typography.
---

# Book Typesetter

This skill provides a comprehensive workflow and asset set for creating professional books (PDF and EPUB) from raw text or LaTeX source.

## Workflow

### 1. Project Initialization
- Create a dedicated directory for the book (e.g., `book-name-en/`).
- Copy the templates from `assets/templates/` to the new directory.
- Use `main-template.tex` as the central entry point.

### 2. Source Material Preparation
- **Chapters:** Organize book content into `chapters-[lang].tex`. Use `\chapter{}` for numbering and `\subtitle{...}` for descriptive headings.
- **Front Matter:** Configure `titlepage.tex`, `info.tex` (copyright), and `dedication.tex`.
- **Styling:** Use `prelude.sty` for typographic settings (memoir class, font selection, drop caps).

### 3. Typographic Refinement
- **Drop Caps:** Use `\lettrine[lraise=0.1, findent=2pt]{L}{etter}` for chapter openings.
- **Title Case:** Ensure subtitles use Title Case for a professional look.
- **ToC Integration:** Use the optional argument `\chapter[Table of Contents Title]{}` to include subtitles in the navigation.

### 4. Build System
- Use the provided `makefile` to automate the process.
- **PDF:** Multi-pass `pdflatex` to resolve ToC and internal links.
- **EPUB:** Flatten files and use `pandoc` with `--epub-cover-image` (PNG preferred for Kindle).
- **Cleanup:** Ensure `make clean` removes auxiliary files without deleting source templates or final binaries.

## Best Practices
- **Modular Design:** Keep LaTeX parts separated (`\include`) for easier maintenance.
- **Roman Numerals:** Use the `memoir` class defaults for classical chapter numbering.
- **Table of Contents:** Increase `\cftchapternumwidth` if Roman numerals overlap with titles (e.g., XVIII).
- **Kindle Compatibility:** Always convert SVG covers to PNG for the EPUB format.
