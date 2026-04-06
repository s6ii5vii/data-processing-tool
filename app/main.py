import csv
import argparse


def load_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print("File not found.")
        return []


def clean_data(data):
    cleaned = []
    for row in data:
        clean_row = {k: v.strip() if v else None for k, v in row.items()}
        cleaned.append(clean_row)
    return cleaned


def summarize_data(data):
    if not data:
        print("No data to summarize.")
        return

    print(f"\nTotal rows: {len(data)}")
    print(f"Columns: {list(data[0].keys())}\n")


def main():
    parser = argparse.ArgumentParser(description="Simple Data Processing Tool")
    parser.add_argument("--file", required=True, help="Path to CSV file")

    args = parser.parse_args()

    data = load_csv(args.file)
    cleaned = clean_data(data)
    summarize_data(cleaned)


if __name__ == "__main__":
    main()