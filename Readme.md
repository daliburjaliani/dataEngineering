# Data Engineering Task

### 1. SQL
### 2. Python

## Python Scripts

### Used Libraries
1. Python 3.9
2. Pandas

### Run Code

#### For Linux/Unix Users:

1. Open a terminal.
2. Navigate to the directory containing the Python script.
3. Make the script executable:
    ```bash
    chmod +x main.py
    ```
4. Run the Python script:
    ```bash
    ./main.py steam-200k.csv new.csv --chunk_size 4000 --max_workers 3
    ```
    - Adjust `--chunk_size` and `--max_workers` as needed.

#### For Windows Users:

1. Open a command prompt.
2. Navigate to the directory containing the Python script.
3. Run the Python script:
    ```bash
    python main.py steam-200k.csv new.csv --chunk_size 4000 --max_workers 2
    ```    
   - Adjust `--chunk_size` and `--max_workers` as needed.
