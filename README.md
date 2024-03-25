# Tasks

## Task 1

This Python script automates the process of logging in to a captive portal by periodically checking the availability of a specified website. If the website is unreachable, it attempts to log in to the captive portal using credentials provided in a configuration file.

### Usage Instructions

### 1. Configuration File
Before running the script, you need to set up a configuration file (`config.txt`) containing your login credentials. Follow these steps to create the configuration file:

1. Create a text file named `config.txt`.
2. Enter your login credentials in the following format:

``` 
your_user_id
your_password
```
Replace `your_user_id` and `your_password` with your actual credentials.

### 2. Running the Script

#### Linux and Windows
To run the script on Linux/Windows, follow these steps:

1. Ensure you have Python installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/).
2. Open a terminal and navigate to the directory containing the script (`autologin.py`).
3. Run the script using the following command:

```
python autologin.py
```

### 3. Automating the Script
You can automate the execution of the script using tools like `cron` on Linux or Task Scheduler on Windows.

#### Linux (using `cron`)
To schedule the script to run periodically on Linux using `cron`, follow these steps:

1. Open a terminal and type the following command to open the crontab file:

```
crontab -e
```
2. Add a new line to the crontab file to specify the schedule for running the script. For example, to run the script every 5 minutes, add the following line:

```
*/5 * * * * /usr/bin/python /path/to/autologin.py
```
Replace `/path/to/autologin.py` with the actual path to the script file.

#### Windows (using Task Scheduler)
To schedule the script to run periodically on Windows using Task Scheduler, follow these steps:

1. Open Task Scheduler from the Start menu.
2. Click on "Create Basic Task" and follow the wizard to create a new task.
3. Specify the schedule for running the task and choose "Start a program" as the action.
4. Browse and select the Python executable (`python.exe`) as the program/script, and provide the path to the script file (`autologin.py`) as the argument.
5. Complete the wizard and save the task.

## Task 2

### Task Description:
The task involves opening a given binary file, analyzing its heap layout, and solving a specific question to capture the flag.

### OS used:
Ubuntu 22.04.03 LTS

### Analyzing the Question:
The heap layout in the binary file includes two heap data blocks, labeled as "input data" and "safe_var," along with their addresses.

### Question Asked:
The task requires overwriting the "safe_var" with the provided "input_data."

### Approach
1. **Analysis**: Examine the binary file to understand its structure and heap layout.
2. **Identify Heap Data and Addresses**: Locate the "input data" and "safe_var" blocks in the heap, along with their respective addresses.
3. **Gap Calculation**: Determine the gap between the addresses of the two heap blocks. In this case, it was observed to be 32 spaces apart.
4. **Overwriting safe_var**: Craft the input in a way that overwrites the "safe_var" with the desired data. In this case, input consisted of 32 characters of filler ("a") followed by the desired data ("ACMR").
5. **Execute**: Execute the binary file with the crafted input to overwrite "safe_var" and capture the flag.
### Result
Using the buffer input aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaACMR and overwrites the `safe_var` as ACMR and the flag `acm_ftw` was obtained

![Screenshot 2024-03-25 215556](https://github.com/adii2ma/acmtask/assets/164670196/7693c152-0101-476c-8e41-deb637df511d)
 
