# Data Processing Tool

A command-line tool built in Python for loading, cleaning, filtering, and summarizing structured data (CSV and JSON).

---

## Features

- Load CSV and JSON datasets
- Clean data (trim whitespace, handle missing values)
- Filter rows using conditions (e.g., `age=25`)
- Select specific columns
- Generate dataset summaries
- Save cleaned data to CSV or JSON

---

## Project Structure

```text
data-processing-tool/
├── app/
│   └── main.py
├── data/
│   ├── sample.csv
│   ├── sample.json
│   └── cleaned.csv
├── .gitignore
├── README.md
├── requirements.txt
---

---

## Requirements

- Python 3.10+ recommended

---

## Usage

### Basic usage

```bash
python app/main.py --file data/sample.csv --summary-only
```

### Filter rows

```bash
python app/main.py --file data/sample.csv --filter age=25 --summary-only
```

### Select columns

```bash
python app/main.py --file data/sample.csv --columns name --summary-only
```

### Combine filtering and column selection

```bash
python app/main.py --file data/sample.csv --filter age=25 --columns name --summary-only
```

### Save cleaned output

```bash
python app/main.py --file data/sample.csv --output data/cleaned.csv
```

### Use JSON input

```bash
python app/main.py --file data/sample.json --summary-only
```

---

## Example Output

```text
=== DATA SUMMARY ===
Total rows: 1
Columns: ['name']

Missing values by column:
- name: 0
```