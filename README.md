# gemini-skills

A collection of personal Gemini skills.

## SKILLS

### `book-typesetter`

A skill for professional, multilingual book typesetting.

**Features:**
- **Dual-Language Workflow:** Streamlines the creation of books in multiple languages (e.g., English and Spanish) from a unified source structure.
- **Advanced LaTeX Formatting:** Implements classical typographic standards, including drop caps, Roman numerals, and custom title pages using the `memoir` class.
- **Automated Build System:** Comes with a robust `makefile` template that handles multi-pass PDF compilation and EPUB generation with `pandoc`.
- **Granular Control:** The `makefile` includes targets for building specific languages, formats, or combinations (`make spanish`, `make pdfs`, `make english-epub`).
- **Auxiliary Scripts:** Includes a new `scripts/` directory for housing text-processing and cleanup scripts, enhancing automation capabilities.

This skill was refined based on the experience building the dual-language edition of Machiavelli's *The Prince*.
