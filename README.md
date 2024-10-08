Free Space Eraser
The Free Space Eraser is a Python script designed to securely erase free space in a specified directory by overwriting it with random data. The script supports multiple overwrite passes, provides progress feedback, and shows the amount of free space both before and after the erasure process. It’s designed with safety in mind, ensuring no critical system directories are affected, and it handles interrupts gracefully.

Features
Multiple Passes: Supports user-defined overwrite passes for enhanced security.
Before and After Free Space Check: Displays the available free space in the directory before and after the secure erase operation.
Progress Feedback: Shows a progress bar and, in verbose mode, additional details such as estimated time left and remaining free space.
Directory Safety Check: Prevents erasing free space on critical directories (e.g., /, /root, /home, or C:\\).
Cross-Platform: Works on both macOS and Linux systems.
Graceful Exit: Handles interruptions (e.g., Ctrl+C) and cleans up files before exiting.
Desktop Notifications: Sends a notification upon the successful completion of the operation (using plyer).
Requirements
Python Version
Python 3.x
Required Libraries
tqdm: For displaying the progress bar.
plyer: For desktop notifications.
Installation of Dependencies
You can install the required dependencies using pip:

bash
Copy code
pip install tqdm plyer
For systems that may restrict pip system-wide installations (like Ubuntu or macOS), consider using a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install tqdm plyer
How It Works
Code Breakdown
Imports:

The script imports essential libraries such as os, shutil, time, and signal to handle file system operations, time tracking, and graceful handling of system interrupts.
External libraries such as tqdm (progress bar) and plyer (desktop notifications) are used to enhance user experience.
Key Functions:

is_safe_directory(directory): Ensures the user does not erase free space in critical system directories by checking against a list of unsafe directories (/, /root, /home, etc.).
get_free_space(directory): Returns the amount of free space (in bytes) in the specified directory.
write_to_free_space(directory, fill_char, verbose): Fills up the free space with the specified character (e.g., 0 or 1) and provides a progress bar. In verbose mode, additional details such as time left and the remaining space are printed.
secure_erase_free_space(directory, passes, verbose): Executes the secure erasure by calling write_to_free_space() for each pass, using different fill characters.
signal_handler(sig, frame): Handles interruptions (e.g., Ctrl+C) and exits gracefully, ensuring any temporary files are cleaned up.
notify_user(title, message): Sends a desktop notification upon completion of the process.
User Interaction:

The script first asks the user to input the number of overwrite passes and whether verbose mode should be enabled.
It checks if the specified directory is valid and safe, then calculates and displays the free space available both before and after the erasure.
Graceful Handling of Interrupts:

The script registers a signal handler for SIGINT (triggered by Ctrl+C) to cleanly exit the process without leaving behind incomplete or temporary files.
Example Output
Before starting the erasure:

arduino
Copy code
Free space available before secure erase: 10.56 GB
During the secure erase process (progress bar):

bash
Copy code
Overwriting free space: 25%|██████████                          | 50.0/200.0 MB [00:10<00:30, 5.0 MB/s]
After the process:

vbnet
Copy code
Free space available after secure erase: 10.32 GB
Secure Erase Complete. Your secure erase operation has finished successfully.
Installation and Setup
macOS and Linux
Clone the Repository:

First, clone this repository to your local machine:
bash
Copy code
git clone https://github.com/Harrygithubportfolio/Secure-Erase-Free-Space.git
Navigate to the Directory:

bash
Copy code
cd Secure-Erase-Free-Space
Install Dependencies:

On macOS and Linux, you can install the required libraries using pip:
bash
Copy code
pip install tqdm plyer
Run the Script:

Execute the script with Python 3:
bash
Copy code
python3 freespaceeraser.py
Usage Instructions
User Prompts: The script will prompt for the following inputs:

Number of passes: Input the number of passes (overwrites) you wish to perform.
Verbose mode: Choose whether to enable verbose mode for more detailed output (yes/no).
Directory path: Input the path to the directory where you want to erase free space.
Confirmation: The script will display the amount of free space before the erasure and ask for confirmation before proceeding.
Example Workflow:

bash
Copy code
Enter the number of passes for secure erasure: 3
Enable verbose mode? (yes/no): yes
Enter the directory you want to erase free space on: /home/user/Documents
Free space available before secure erase: 15.32 GB
Do you want to proceed with the secure erase? (yes/no): yes
Progress Bar: A progress bar will display the current status of the operation, showing how much free space has been overwritten.

Completion: Upon successful completion, the script will notify you of the amount of free space after the operation and send a desktop notification:

vbnet
Copy code
Free space available after secure erase: 15.05 GB
Secure Erase Complete. Your secure erase operation has finished successfully.
Example Usage on macOS and Linux
macOS
To run the script on macOS:

Install tqdm and plyer using pip:

bash
Copy code
pip install tqdm plyer
Run the script:

bash
Copy code
python3 freespaceeraser.py
Linux (Ubuntu/Debian-based systems)
To run the script on Linux:

Install tqdm and plyer:

bash
Copy code
sudo apt install python3-tqdm python3-plyer
Run the script:

bash
Copy code
python3 freespaceeraser.py
Safety Mechanisms
Critical Directory Protection:

The script prevents operations on system-critical directories (like /, /home, /root, and C:\\ on Windows).
If the user attempts to specify a protected directory, the operation will be aborted for safety.
Signal Handling:

The script gracefully handles interruptions such as Ctrl+C, ensuring that no incomplete files are left behind, and the system remains stable.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contributions
If you'd like to contribute, feel free to fork the repository, open issues, or submit pull requests with improvements or new features.

Author
Harry Graham
