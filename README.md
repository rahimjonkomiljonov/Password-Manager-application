# Password Manager

A GUI-based password manager built with Tkinter that generates, saves, and retrieves passwords for websites.

## Features
- Generate strong random passwords (8-10 letters, 2-4 numbers, 2-4 symbols)
- Automatically copy generated passwords to clipboard
- Save website credentials to a JSON file
- Search for saved credentials by website name
- Simple GUI interface with error handling

## Prerequisites
- Python 3.x
- Required Python packages:
  - `tkinter` (usually included with Python)
  - `pyperclip`
- Required asset:
  - `logo.png` (200x200 pixel image file)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```

2. Install dependencies:
```bash
pip install pyperclip
```

3. Ensure `logo.png` is in the project directory

## Usage
1. Run the application:
```bash
python password_manager.py
```

2. Use the GUI:
- Enter a website name
- Generate a password or enter your own
- Click "Add" to save
- Use "Search" to retrieve saved credentials

## How It Works
- **Password Generation**: Creates random passwords with:
  - 8-10 letters (upper/lowercase)
  - 2-4 numbers
  - 2-4 symbols (!#$%&()*+)
- **Storage**: Saves credentials in `pw_file.json`
- **Search**: Retrieves and displays saved credentials
- Validates input to prevent empty fields

## File Structure
- `password_manager.py`: Main application file
- `logo.png`: Lock icon for GUI (required)
- `pw_file.json`: Generated file for storing credentials

## GUI Components
- Website entry field
- Email/Username field (pre-filled with default email)
- Password entry field
- Generate Password button
- Search button
- Add button
- Logo display

## Data Format
Saved in `pw_file.json` as:
```json
{
    "website": {
        "username": "email@example.com",
        "password": "generated_password"
    }
}
```

## Notes
- Default email: "rahimonkomiljonov06@gmail.com"
- Passwords are automatically copied to clipboard when generated
- Error handling for empty fields and missing file
- Responsive grid layout with proper spacing
- Requires `logo.png` in the same directory

## Requirements.txt
```
pyperclip
```

## Customization
- Modify `username_entry.insert()` for different default email
- Adjust password generation parameters in `generate_password()`
- Change window title or button widths
- Update logo file path/name if different

## Limitations
- Basic search functionality (case-sensitive)
- No encryption of stored passwords
- Single-user focus
- Requires manual JSON file management

## License
[MIT License](LICENSE)

## Disclaimer
This is a basic password manager for educational purposes. For real-world use, consider:
- Adding encryption
- Implementing secure file handling
- Adding user authentication
```

