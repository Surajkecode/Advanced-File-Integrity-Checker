import hashlib
import os
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Function to calculate file hash
def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """Calculate the hash value of a file using the specified hashing algorithm."""
    hash_obj = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# Logging setup for changes
def setup_logging():
    """Setup logging to record file changes."""
    logging.basicConfig(filename="file_integrity_log.txt", level=logging.INFO, 
                        format='%(asctime)s - %(message)s')

# Function to send email notifications
def send_email_notification(subject, body, to_email):
    """Send an email notification when the file changes."""
    from_email = "suraj9881392842@gmail.com"
    password = "jyhwaotsgogxfiag"  # Use your actual app password without spaces

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    # Set up the server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)  # Use the App Password here
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email notification sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to monitor file integrity
def monitor_file_integrity(file_path, hash_algorithm='sha256', check_interval=10, send_email=False, email=None):
    """Monitor the integrity of a file by calculating and comparing its hash value periodically."""
    # Calculate the initial hash value of the file
    initial_hash = calculate_file_hash(file_path, hash_algorithm)
    initial_size = os.path.getsize(file_path)
    print(f"Initial hash value of '{file_path}': {initial_hash}")
    print(f"Monitoring '{file_path}' for changes...")

    # Log initial file state
    logging.info(f"Initial hash: {initial_hash} | Size: {initial_size} bytes | Path: {file_path}")

    # Continuously monitor the file for changes
    try:
        while True:
            time.sleep(check_interval)

            # Get the current hash value and file size
            current_hash = calculate_file_hash(file_path, hash_algorithm)
            current_size = os.path.getsize(file_path)

            # Check if the file's hash or size has changed
            if current_hash != initial_hash or current_size != initial_size:
                change_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                change_message = f"File '{file_path}' modified at {change_time}."
                print(change_message)
                
                # Log the change
                logging.info(f"File changed - Hash: {current_hash} | Size: {current_size} bytes | Time: {change_time}")

                # Send email notification if enabled
                if send_email and email:
                    send_email_notification(
                        subject="File Integrity Change Detected",
                        body=change_message,
                        to_email=email
                    )

                # Update initial values after change
                initial_hash = current_hash
                initial_size = current_size
            else:
                print(f"The file '{file_path}' remains unchanged.")

    except KeyboardInterrupt:
        print("\nFile monitoring stopped.")

if __name__ == "__main__":
    setup_logging()

    # Get the file path and monitoring options from the user
    file_path = input("Enter the path of the file to monitor: ")

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
    else:
        # Get additional options
        hash_algorithm = input("Enter hash algorithm (default sha256): ").lower() or 'sha256'
        check_interval = int(input("Enter check interval (in seconds, default 10): ") or 10)
        send_email = input("Do you want to receive email notifications on changes? (y/n): ").lower() == 'y'

        if send_email:
            email = input("Enter your email address to receive notifications: ")
            # Ensure email is valid (basic check)
            if '@' not in email or '.' not in email.split('@')[1]:
                print("Invalid email address.")
                send_email = False
                email = None

        monitor_file_integrity(file_path, hash_algorithm, check_interval, send_email, email)
