# InstaPyFlow

A simple Python-based Instagram automation tool for uploading photos to your Instagram account.

## Overview

InstaPyFlow provides a straightforward interface for automating Instagram photo uploads using Python. It leverages the instabot library to handle authentication and media posting.

## Features

- Instagram account authentication
- Photo upload support (JPEG/JPG formats)
- Custom caption support for posts
- Simple and clean API

## Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.x |
| **Core Library** | instabot |
| **Virtual Environment** | Python venv |

## Architecture

```
InstaPyFlow/
├── autoinsta.py       # Main application entry point
├── requirements.txt  # Project dependencies
├── .venv/            # Virtual environment
└── README.md         # Project documentation
```

### Core Components

**autoinsta.py**
- Initializes the Instagram bot
- Handles user authentication
- Manages photo uploads with captions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/InstaPyFlow.git
cd InstaPyFlow
```

2. Create and activate virtual environment:
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Configuration

Edit `autoinsta.py` to configure your Instagram credentials:

```python
from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# Upload a photo with caption
bot.upload_photo("image.jpg", "Your caption here")
```

### Running the Bot

```bash
python autoinsta.py
```

## Requirements

- Python 3.7+
- instabot

## Supported Image Formats

- JPEG (.jpg, .jpeg)

## Important Notes

1. **Two-Factor Authentication**: If your Instagram account has 2FA enabled, you may need to disable it or use an app password.
2. **Rate Limiting**: Instagram has rate limits. Avoid excessive automated requests.
3. **Terms of Service**: Be aware that automated Instagram use may violate their Terms of Service. Use responsibly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Automated actions on Instagram may violate their Terms of Service. Use at your own risk.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Mr.AJ

---

*Last updated: 2026*