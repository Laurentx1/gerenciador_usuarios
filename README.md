Windows User Management Tool
Overview
A comprehensive Python-based command-line utility for managing Windows user accounts with administrative privileges. This tool provides a user-friendly interface for performing common user management tasks on Windows systems, including user creation, deletion, privilege management, and profile maintenance.
Features

User Account Management

Create new user accounts with password validation
Delete existing user accounts with safety confirmations
List all system users
Display detailed user information


Administrative Privileges

Add users to the Administrators group
Remove users from the Administrators group
Automatic privilege escalation requests


Password Management

Secure password input (hidden from display)
Password strength validation
Force password change on next login


Profile Management

Complete user profile deletion
Safe removal of user directories


Security Features

Input validation and sanitization
Confirmation prompts for destructive operations
Administrator privilege verification



Requirements

Windows operating system
Python 3.6 or higher
Administrator privileges (automatically requested)

Installation

Clone the repository:

bashgit clone https://github.com/yourusername/windows-user-manager.git
cd windows-user-manager

Run the script:

bashpython user_manager.py
The application will automatically request administrator privileges if not already running with elevated permissions.
Usage
Launch the application and select from the following options:

Create User - Add a new user account to the system
Delete User - Remove an existing user account
Add to Administrators - Grant administrative privileges to a user
Remove from Administrators - Revoke administrative privileges from a user
Force Password Change - Require password change on next login
Delete User Profile - Remove user profile directory and data
List Users - Display all system users
Show User Information - View detailed information about a specific user

Input Validation
The application includes comprehensive input validation:

Username length restrictions (maximum 20 characters)
Invalid character detection for Windows usernames
Password strength requirements (minimum 6 characters)
Confirmation prompts for destructive operations

Error Handling

Graceful handling of command execution failures
Detailed error messages with troubleshooting information
Safe operation cancellation for user protection

Security Considerations
This tool requires administrator privileges to function properly. Always ensure you:

Run the application on trusted systems only
Verify user credentials before making changes
Use strong passwords for new accounts
Review changes before confirming destructive operations

Platform Compatibility

Supported: Windows 10, Windows 11, Windows Server 2016+
Language Support: Portuguese and English Windows installations
Architecture: Compatible with both 32-bit and 64-bit systems

Technical Implementation

Built with Python standard library modules
Uses Windows net user and net localgroup commands
Implements Windows UAC (User Account Control) integration
Character encoding handling for Windows command prompt

Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Disclaimer
This tool modifies system user accounts and should be used with caution. Always test in a controlled environment before using in production systems. The authors are not responsible for any system modifications or data loss resulting from the use of this tool.
Support
For issues, feature requests, or questions, please open an issue on GitHub or contact the maintainers.
