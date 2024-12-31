# Task 1 : Advanced-File-Integrity-Checker
---

# Advanced File Integrity Checker

## Project Overview
**Title:** Advanced File Integrity Checker  
**Developer:** Suraj Borkute  
**Company:** Codtech IT Solutions  
**Employee ID:** CT08DSM  
**Domain:** Cyber Security & Ethical Hacking  
**Duration:** Dec 2024 to Jan 2025  
**Mentor:** Neela Santosh Kumar
# Title: Advanced-File-Integrity-Checker

This project aims to provide an advanced solution for monitoring file integrity by utilizing various hashing algorithms and offering additional features such as email notifications, logging, and configurable intervals.


![image](https://github.com/user-attachments/assets/d88b6adf-802f-4538-a6a9-bd9ca9248a7a)

![image](https://github.com/user-attachments/assets/035a7cc2-6f3d-47e7-88e5-883be0bbf93d)

![image](https://github.com/user-attachments/assets/60432962-9613-4005-bfc1-355a7ef8a788)



## Features

- **Logging Changes:**  
  - Keep a log of detected changes with timestamps for tracking modifications.
  
- **Email Notifications:**  
  - Send an email when a file's integrity is compromised or modified.

- **Multiple File Monitoring:**  
  - Monitor multiple files or an entire directory for changes, making it suitable for diverse use cases.
  
- **Configurable Hash Algorithms:**  
  - Allow users to select from different hash algorithms such as **SHA-1**, **SHA-256**, **SHA-512**, and **MD5**.

- **File Size Monitoring:**  
  - Detect changes based on file size in addition to hash comparison to ensure more comprehensive monitoring.
  
- **Customizable Check Interval:**  
  - Let the user specify the time interval between each check, giving flexibility based on the use case.

- **Graceful Exit:**  
  - The script will continue monitoring the file until you stop it manually by pressing **Ctrl + C**.

## Hash Algorithms

This tool supports multiple hash algorithms, each with its own benefits and trade-offs:

- **SHA-256 (Recommended):**  
  - Secure and resistant to collision attacks. It is the recommended algorithm for most applications due to its balance between performance and security.
  
- **SHA-1:**  
  - Faster but less secure than SHA-256. It is considered vulnerable to attacks and should only be used when performance is more important than security.

- **MD5:**  
  - Similar to SHA-1, MD5 is fast but not recommended for security-critical applications due to vulnerabilities.

- **SHA-512:**  
  - Provides a stronger hash value than SHA-256, useful for highly sensitive applications where maximum security is required.

## Setup Instructions

### Prerequisites
Make sure you have the following installed on your machine:
- Python 3.x
- `pip` for installing dependencies

### Installing Dependencies

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/advanced-file-integrity-checker.git
   cd advanced-file-integrity-checker
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have the `requirements.txt` file, you can install the necessary dependencies directly using:
   ```bash
   pip install hashlib smtplib logging
   ```

### Configuring Email Notifications

To enable email notifications, you need to configure an **App Password** for your Gmail account (if you have 2-step verification enabled):

1. Go to your [Google Account Security Settings](https://myaccount.google.com/security).
2. Enable **2-Step Verification** if it's not enabled.
3. Under **App Passwords**, create an app password specifically for this script:
   - Select **Mail** and **Windows Computer** (or other option as suitable).
   - Generate the app password.

4. Use this app password in the script as follows:
   ```python
   password = "your-app-password-here"
   ```
   **For further instructions on how to generate an app password, refer to this video:**  
   [How to Set Up App Passwords for Gmail](https://youtu.be/dM_DlzyeWW8?feature=shared)

### Running the Script

1. After setting up the configuration, run the script by executing:
   ```bash
   python file_integrity_checker.py
   ```

2. You will be prompted to:
   - Enter the **file path** of the file(s) to monitor.
   - Select the **hash algorithm** to use.
   - Set the **check interval** (in seconds).
   - Choose whether to receive **email notifications** upon file changes.

### Example Usage

```bash
Enter the path of the file to monitor: /path/to/your/file.txt
Enter hash algorithm (default sha256): SHA-512
Enter check interval (in seconds, default 10): 10
Do you want to receive email notifications on changes? (y/n): y
Enter your email address to receive notifications: youremail@gmail.com
```

### Stopping the Monitoring

To stop the monitoring, simply press **Ctrl + C**.

## Logging

All detected changes are logged in a file named `file_integrity_log.txt` with the following format:

```
YYYY-MM-DD HH:MM:SS - File changed - Hash: <new_hash> | Size: <new_size> bytes | Time: <change_time>

```
Contact
## Suraj Borkute
### GitHub: [https://github.com/Surajkecode]

### Email: [surajborkute9881392842@gmail.com]

### 🔗 Links
For questions or inquiries, feel free to contact us:

[LinkedIn Profile]: (https://www.linkedin.com/in/suraj-borkute-512665341)


## Contribution

Feel free to fork this repository and create a pull request for improvements or bug fixes. Please ensure that any changes made are thoroughly tested.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
