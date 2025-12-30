# JSON Syntax Validator (Strict)

A linter that parses JSON files strictly according to the standard. It flags trailing commas, comments, and other non-standard features that often break parsers in other languages.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Strict Parsing**: Identifies errors that lenient parsers might miss.
*   **Exact Location**: Reports line and column number of the syntax error.
*   **Recursive**: Scans entire directories for `.json` files.

## Usage

```bash
python run_validator.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_validator.py config/
```

**2. Detects**
```json
{
  "key": "value", // Comments not allowed
  "oops": "comma", 
}
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
