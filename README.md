# Free Space Eraser

This Python script securely erases free space on a given directory by overwriting it with random data and allows users to check the available free space before and after the process. It provides an option to perform multiple overwrite passes for enhanced security and features a progress bar for visual feedback during the erasure process.

## Features

- **Secure Erasure**: The script securely overwrites free space in a given directory with random data to prevent data recovery.
- **Multiple Passes**: The script allows the user to specify how many times they want to overwrite the free space for added security.
- **Before and After Free Space**: It displays the amount of free space available in the directory before and after the secure erase process.
- **Progress Bar**: A progress bar (`tqdm`) is shown during the overwrite process to visualize the progress.
- **Verbose Mode**: An optional verbose mode shows additional details like remaining time and the amount of free space left.
- **System Safety**: The script ensures that critical directories (like `/` or `C:\`) are protected by preventing the user from performing dangerous operations on them.
- **Graceful Exit**: The script captures `Ctrl+C` (SIGINT) to allow for a clean exit, ensuring that the system remains stable even if interrupted.
- **Notification**: The script uses the `plyer` module to send a desktop notification upon the successful completion of the secure erasure.

## Requirements

- Python 3.x
- Required libraries:
  - `tqdm`
  - `plyer`

You can install the required packages using pip:

```bash
pip install tqdm plyer

