# CIDR to Addressable IPs Converter

This Python script allows users to convert CIDR blocks into their addressable IP addresses. It supports processing a single CIDR block or multiple blocks provided in a file.

## Features

- Converts a single CIDR block into a list of addressable IPs.
- Processes files containing multiple CIDR blocks (one per line).
- Validates input and handles errors gracefully.

## Requirements

- Python 3.6 or later.

## Installation

1. Clone the repository or download the script file.
2. Ensure Python is installed on your system.

## Usage

Run the script from the command line using the following syntax:

### Single CIDR Block
```bash
python script.py <CIDR_BLOCK>
```
Example:
```bash
python script.py 192.168.1.0/30
```
Output:
```
192.168.1.1
192.168.1.2
```

### File with CIDR Blocks
```bash
python script.py <FILE_PATH> --file
```
Example:
```bash
python script.py cidr_list.txt --file
```
Output:
```
192.168.1.0/30:
  192.168.1.1
  192.168.1.2
10.0.0.0/29:
  10.0.0.1
  10.0.0.2
  10.0.0.3
```

## Script Options

- `input`: Required. Accepts a CIDR block (e.g., `192.168.1.0/24`) or a file path.
- `-f`, `--file`: Optional. Indicates that the input is a file containing CIDR blocks.

## Error Handling

- Invalid CIDR blocks will produce an error message without crashing the script.
- Missing files will prompt a "File not found" message.

## Example File Format

For processing multiple CIDR blocks, create a text file (`cidr_list.txt`) with each CIDR block on a separate line:
```
192.168.1.0/30
10.0.0.0/29
172.16.0.0/28
```

