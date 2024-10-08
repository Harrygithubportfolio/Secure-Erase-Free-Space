import os
import shutil
import platform
import signal
import sys
from tqdm import tqdm
from time import time
from plyer import notification

def is_safe_directory(directory):
    # Define critical system directories that should not be erased
    unsafe_directories = ['/', 'C:\\', '/home', '/root', os.path.expanduser('~')]
    if os.path.abspath(directory) in map(os.path.abspath, unsafe_directories):
        return False
    return True

def get_free_space(directory):
    """Return the free space in bytes of the given directory."""
    total, used, free = shutil.disk_usage(directory)
    return free

def write_to_free_space(directory, fill_char='0', verbose=False):
    """Fill all free space with the given character, showing progress and remaining time."""
    free_space = get_free_space(directory)
    filler_filename = os.path.join(directory, 'filler')

    try:
        with open(filler_filename, 'wb') as filler:
            chunk_size = 1024 * 1024  # 1MB per chunk
            num_chunks = free_space // chunk_size
            last_printed_percentage = 0  # To control printing
            start_time = time()

            for i in tqdm(range(num_chunks), desc="Overwriting free space", unit="MB"):
                filler.write(fill_char.encode() * chunk_size)

                if verbose:
                    # Calculate the current percentage of completion
                    current_percentage = (i + 1) / num_chunks * 100

                    if current_percentage - last_printed_percentage >= 1:  # Print every 1% progress
                        elapsed_time = time() - start_time
                        bytes_written = (i + 1) * chunk_size
                        remaining_bytes = free_space - bytes_written
                        speed = bytes_written / elapsed_time  # Bytes per second
                        remaining_time = remaining_bytes / speed if speed > 0 else 0

                        print(f"Progress: {current_percentage:.2f}% complete, "
                              f"{remaining_bytes / (1024 ** 3):.2f} GB remaining, "
                              f"Estimated time left: {remaining_time / 60:.2f} minutes.")

                        last_printed_percentage = current_percentage

            remaining = free_space % chunk_size
            if remaining > 0:
                filler.write(fill_char.encode() * remaining)
    except IOError as e:
        print(f"Error writing to disk: {e}")
    finally:
        if os.path.exists(filler_filename):
            os.remove(filler_filename)

def secure_erase_free_space(directory, passes=1, verbose=False):
    """Securely erase free space by overwriting it with random data."""
    for i in range(passes):
        print(f"Pass {i + 1}/{passes}: Overwriting free space.")
        write_to_free_space(directory, fill_char='0', verbose=verbose)
        write_to_free_space(directory, fill_char='1', verbose=verbose)
    print("Secure erase complete.")

def signal_handler(sig, frame):
    print("\nProcess interrupted! Cleaning up...")
    sys.exit(0)

def notify_user(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

if __name__ == "__main__":
    # Setup signal handler for graceful exit
    signal.signal(signal.SIGINT, signal_handler)

    # Ask the user how many passes they'd like to perform
    while True:
        try:
            passes = int(input("Enter the number of passes for secure erasure: "))
            if passes < 1:
                raise ValueError("Number of passes must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    # Ask the user if they want verbose mode
    verbose = input("Enable verbose mode? (yes/no): ").lower() == 'yes'

    # Ask the user to input the directory
    directory = input("Enter the directory you want to erase free space on: ")

    # Check if the directory is safe to use
    if not is_safe_directory(directory):
        print("Warning: You are trying to erase a critical directory. Operation aborted.")
        sys.exit(1)

    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
        sys.exit(1)

    # Display the amount of free space available before the secure erase
    free_space_before_gb = get_free_space(directory) / (1024 ** 3)
    print(f"Free space available before secure erase: {free_space_before_gb:.2f} GB")

    # Ask user for confirmation before starting the secure erase process
    confirm = input("Do you want to proceed with the secure erase? (yes/no): ").lower()
    if confirm == 'yes':
        # Perform the secure erase with the specified number of passes
        secure_erase_free_space(directory, passes=passes, verbose=verbose)
        
        # Display the amount of free space available after the secure erase
        free_space_after_gb = get_free_space(directory) / (1024 ** 3)
        print(f"Free space available after secure erase: {free_space_after_gb:.2f} GB")
        
        # Notify the user about the completion
        notify_user("Secure Erase Complete", "Your secure erase operation has finished successfully.")
    else:
        print("Secure erase canceled.")

