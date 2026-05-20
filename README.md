# InstaPyFlow

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-orange?style=flat" alt="Status">
</p>

A powerful Python-based Instagram automation tool that enables automated photo uploads, batch processing, and smart notifications.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Upload (autoinsta.py)](#basic-upload-autoinstapy)
  - [Advanced Automation (autoinsta_2.py)](#advanced-automation-autoinsta_2py)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [Supported Image Formats](#supported-image-formats)
- [Important Notes](#important-notes)
- [License](#license)
- [Contributing](#contributing)

---

## Overview

InstaPyFlow is an automation toolkit designed to simplify Instagram account management through Python. It provides two operational modes: a simple photo uploader for quick posts and an advanced automation system with batch processing, format conversion, and email notifications.

---

## Features

### Basic Features (autoinsta.py)
- Instagram account authentication
- Single photo upload with custom captions
- JPEG/JPG format support

### Advanced Features (autoinsta_2.py)
- **Random Photo Selection** - Automatically picks random photos from a designated folder
- **Format Conversion** - Converts PNG images to JPEG before uploading
- **Storage Management** - Tracks photo库存 and sends notifications
- **Email Notifications** - SMTP-based alerts for:
  - Available photo count updates
  - Low storage warnings (when photos ≤ 10)
- **Auto-cleanup** - Removes uploaded photos from storage after posting

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.x |
| **Core Library** | instabot |
| **Image Processing** | Pillow (PIL) |
| **Email Protocol** | smtplib (Python built-in) |
| **Virtual Environment** | Python venv |
| **Package Manager** | pip |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        InstaPyFlow                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────┐      ┌─────────────────────┐     │
│  │    autoinsta.py     │      │   autoinsta_2.py    │     │
│  │   (Simple Mode)     │      │   (Advanced Mode)   │     │
│  └──────────┬──────────┘      └──────────┬──────────┘     │
│             │                            │                 │
│             ▼                            ▼                 │
│  ┌─────────────────────┐      ┌─────────────────────┐     │
│  │     instabot       │◄─────│     instabot       │     │
│  │    (API Layer)     │      │    (API Layer)     │     │
│  └──────────┬──────────┘      └──────────┬──────────┘     │
│             │                            │                 │
│             ▼                            ▼                 │
│  ┌─────────────────────┐      ┌─────────────────────┐     │
│  │  Instagram API     │      │  Instagram API     │     │
│  └─────────────────────┘      └─────────────────────┘     │
│                                     │                       │
│                                     ▼                       │
│                            ┌─────────────────────┐         │
│                            │    SMTP Email       │         │
│                            │   (Notifications)   │         │
│                            └─────────────────────┘         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Project Structure

```
InstaPyFlow/
├── autoinsta.py           # Basic Instagram bot (single upload)
├── autoinsta_2.py         # Advanced automation bot
├── requirements.txt      # Project dependencies
├── photos/               # Photo storage directory (auto-created)
├── .venv/                # Python virtual environment
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/InstaPyFlow.git
cd InstaPyFlow
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Basic Upload (autoinsta.py)

A simple script for uploading a single photo with caption.

```python
from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# Upload photo with caption
bot.upload_photo("image.jpg", "Your caption here")
```

**Run:**
```bash
python autoinsta.py
```

---

### Advanced Automation (autoinsta_2.py)

A comprehensive automation script with random photo selection, format conversion, and email notifications.

**Features:**
- Randomly selects photos from `photos/` folder
- Converts PNG to JPEG automatically
- Sends email notifications when storage is low (≤10 photos)
- Removes uploaded photos after posting
- Sends confirmation email with photo count

**Setup:**
1. Create a `photos` folder in the project directory
2. Add your images to the folder
3. Configure email credentials in the script

**Run:**
```bash
python autoinsta_2.py
```

---

## Configuration

### For autoinsta.py

Edit the credentials in `autoinsta.py`:

```python
bot.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")
bot.upload_photo("image.jpg", "Your Caption")
```

### For autoinsta_2.py

Configure these variables at the top of the file:

```python
# Instagram Credentials
bot.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")

# Email Configuration (Gmail SMTP)
email = "your_email@gmail.com"
email_password = "your_app_password"

# Email Recipients
send_email("receiver@example.com", "Subject", "Message")
```

---

## Requirements

```
instabot
Pillow>=9.0.0
```

Install via:
```bash
pip install instabot Pillow
```

---

## Supported Image Formats

| Format | Basic Mode | Advanced Mode |
|--------|------------|---------------|
| JPEG   | ✅          | ✅             |
| JPG    | ✅          | ✅             |
| PNG    | ❌          | ✅ (auto-converts) |

---

## Important Notes

### Security
- **Never commit credentials** to version control
- Use environment variables for sensitive data
- Consider using **App Passwords** instead of your main password for Gmail SMTP

### Instagram Terms of Service
- Automated actions may violate Instagram's [Terms of Service](https://help.instagram.com/581066165581870)
- Use responsibly and at your own risk
- Avoid excessive automation to prevent account restrictions

### Rate Limiting
- Instagram enforces rate limits on automated actions
- Implement delays between operations
- Monitor account for unusual activity

### Gmail SMTP Setup
If using Gmail, you need to:
1. Enable 2-Step Verification
2. Generate an App Password: [Google App Passwords](https://myaccount.google.com/apppasswords)

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 InstaPyFlow

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Disclaimer

This tool is for **educational purposes only**. Automated actions on Instagram may violate their Terms of Service. The author is not responsible for any account restrictions, bans, or other consequences resulting from the use of this software.

---

## Author

**Mr.AJ**

---

<p align="center">
  ⭐ Star this repository if you found it helpful!
</p>

*Last updated: May 2026*