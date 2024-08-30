# Secure Erase Free Space

## Overview
This Python script securely erases the free space on a specified directory by overwriting it with data multiple times. It provides an option for the user to specify the number of passes, which increases the security of the erasure by making it harder to recover the overwritten data. The script includes a verbose mode for detailed progress information and uses the `plyer` library to send desktop notifications once the operation is complete.

## Features
- **Secure Free Space Erasure**: Overwrites the free space in the specified directory with data multiple times.
- **Customizable Passes**: Allows the user to specify the number of overwrite passes for added security.
- **Verbose Mode**: Provides detailed progress updates, including the estimated time remaining.
- **Signal Handling**: Gracefully handles interruptions (e.g., Ctrl+C) by cleaning up and exiting.
- **Cross-Platform Support**: Compatible with both Windows and Unix-based systems.
- **Desktop Notifications**: Notifies the user upon completion of the secure erase operation.

## Prerequisites
- **Python 3.x**
- **Required Libraries**: Install the necessary Python libraries using the following command:
  ```sh
  pip install tqdm plyer
  ```

## Usage
1. **Run the Script**:
   - Execute the script from the command line:
     ```sh
     python secure_erase_free_space.py
     ```

2. **Input Number of Passes**:
   - The script will prompt you to enter the number of passes for secure erasure. The more passes, the more secure the erasure.

3. **Enable Verbose Mode (Optional)**:
   - You can choose to enable verbose mode to receive detailed progress updates during the operation.

4. **Directory Selection**:
   - The script automatically selects the appropriate directory based on your operating system. Ensure the directory used is correct for your situation.

5. **Confirmation**:
   - The script will display the available free space and ask for confirmation before proceeding with the secure erase.

6. **Completion Notification**:
   - Once the secure erase is complete, a desktop notification will inform you that the operation has finished successfully.

## Important Notes
- **Warning**: This script is intended to securely erase free space. Be cautious and ensure that you are not attempting to erase critical system directories (e.g., `/`, `C:\`, or your home directory). The script includes checks to prevent accidental erasure of such directories.
- **Performance**: Depending on the amount of free space and the number of passes, the operation may take a considerable amount of time.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions
Contributions are welcome! Please feel free to submit a pull request or report issues.

## Author
Harry Graham

## Acknowledgements
- `tqdm` for progress bar implementation.
- `plyer` for cross-platform desktop notifications.
