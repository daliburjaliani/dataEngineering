import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor
import argparse


# function for measuring execution time
def timeMeasure(func):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time: {end_time - start_time} S")
            return result
        except Exception as e:
            print(f"Error: {e}")
    return wrapper


def deduplicateChunk(chunk):
    # Exclude 'purchase' cause are all 1.0
    chunk = chunk[(chunk['Action'] != 'purchase')]

    # Deduplicate based on 'ID', 'Game'
    return chunk.drop_duplicates(subset=['ID', 'Game'])


@timeMeasure
def deduplicate_dataset_parallel(input_data, output_data, chunk_size, max_workers):
    try:
        df = pd.read_csv(input_data, header=None, names=['ID', 'Game', 'Action', 'Value1', 'Value2'])

        # Drop the 'Value2' column cause all are 0
        df = df[['ID', 'Game', 'Action', 'Value1']]

        # Split the DataFrame into chunks
        chunks = [df[i:i + chunk_size] for i in range(0, len(df), chunk_size)]

        # Use ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(deduplicateChunk, chunks))

        df_deduplicated = pd.concat(results)

        # drop Action column cause all are play / change name of value1
        df_deduplicated = df_deduplicated[['ID', 'Game', 'Value1']].rename(columns={'Value1': 'PlayTime'})

        df_deduplicated.to_csv(output_data, index=False)
    except Exception as e:
        print(f"Error: {e}")


def main():
    try:
        # use argparse to parse command line arguments
        parser = argparse.ArgumentParser(description='Deduplicate records in a CSV file.')
        parser.add_argument('input_data', help='Path to the input CSV file')
        parser.add_argument('output_data', help='Path to the output CSV file')
        parser.add_argument('--chunk_size', type=int, default=10000, help='Size of chunks for parallel processing')
        parser.add_argument('--max_workers', type=int, default=4, help='Maximum number of parallel workers')

        args = parser.parse_args()

        deduplicate_dataset_parallel(args.input_data, args.output_data, args.chunk_size, args.max_workers)
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()
