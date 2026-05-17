---
name: book-typesetter
description: Professional multilingual book typesetting for PDF and EPUB using LaTeX and Pandoc. Use when creating or refining high-quality book projects with modular structures, dynamic covers, and classical typography.
---

# Book Typesetter

This skill provides a comprehensive workflow and asset set for creating professional books (PDF and EPUB) from raw text or LaTeX source.

## Workflow

### 1. Project Initialization
- Organize your repository with language-specific files (e.g., `-en.tex`, `-es.tex`).
- Copy the templates from `assets/templates/` to the root directory.
- Use language-prefixed entry points like `main-en.tex` and `main-es.tex`.

### 2. Source Material Preparation
- **Extraction:** When extracting from PDFs or raw text, use regex to purge footnote markers (e.g., `word123` -> `word`) and artifacts (headers, page numbers).
- **Chapters:** Organize content into `chapters-[lang].tex`. Use `\chapter[ToC Title]{}` for numbering and `\subtitle{...}` for descriptive headings.
- **Front Matter:** Configure `titlepage-[lang].tex`, `info-[lang].tex` (copyright), and `dedication-[lang].tex`.
- **Formatting:** Hard-wrap source files to ~80 characters for better version control and CLI readability.

### 3. Typographic Refinement
- **Drop Caps:** Use `\lettrine[lraise=0.1, findent=2pt]{L}{etter}` for every chapter opening. Ensure no space exists between the lettrine command and the rest of the word.
- **Verse:** Use the `verse` environment with `\itshape` for poetry or concluding quotes.
- **Spacing:** Ensure `\chapter` and `\subtitle` are on adjacent lines. For Chapter I, consider consolidating text into a single paragraph if appropriate for the edition.

### 4. Build System
- Use a robust `makefile` with granular and descriptive targets:
  - `make english` / `make spanish`: Build all formats for a specific language.
  - `make pdfs` / `make epubs`: Build all editions in a specific format.
  - `make english-pdf`: Target a specific language and format.
- **PDF:** Perform 3+ `pdflatex` passes to resolve complex Table of Contents and cross-references.
- **EPUB:** Use `pandoc` to flatten modular LaTeX files into a single eBook, applying language-specific metadata.

## Best Practices
- **Multi-Pass Builds:** Always build multiple times to ensure Table of Contents and links are synchronized.
- **UTF-8:** Ensure all source files use UTF-8 encoding to support multilingual characters.
- **Clean Workspace:** Regularly use `make clean` to remove transient `.aux`, `.log`, and `.toc` files.
- **History Management:** Never commit large source PDFs or temporary extraction scripts to the repository history.
