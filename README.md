# payout-calc

## About this program
`payout-calc.py` is a command-line program designed to calculate payouts for gambling/betting pools or similar situations when provided with a list of overall earnings and losses. It will generate a `.txt` file listing each step of the payout - who pays whom and how much. 

## Usage

### Requirements
To run this program, make `payout-calc.py` executable on your computer (such as through the use of the `chmod` command) and make sure that you have a working Python installation (python3). 

### Running this program
`payout-calc` accepts several command-line parameters: `payout-calc.py [-h] [-v] [-c {d,e,p,y}] [-o] [-d] data destination`

The required parameters are: 
- `data`: The input file to read from. This should be a `.csv` file following the format shown in `example_input.csv` and described below.
- `destination`: The file path where output should be written. The file name should be specified (for example: `./output.txt`).

The program also accepts several optional parameters:
- `-h`, `--help`: Shows a help message and exits.
- `-v`, `--verbose`: Enables verbose mode. When verbose mode is enabled, each payout step will be printed as the program runs as well as written to the output file. If verbose mode is not enabled, payout steps will only be written to the output file.
- `-c`, `--currency`: Specifies an optional currency symbol to add to the output. Currently, the program only supports $ (`d`), € (`e`), £ (`p`), and ¥ (`y`). If not specified, no currency symbol will be added.
- `-o`, `--optimize`: Enabling this option will cause the program to run the calculation slightly differently. This may result in cleaner output (more optimized payouts), but at the cost of performance when run on long input lists (depending on your computer's hardware).
- `-d`, `--debug`: Enabling this option causes snapshots of the current state to be printed as the program runs. Debug output is not written to the output file. Only enable this option if you are encountering issues or are curious how information is stored. If you find a bug in the program, please create an issue on the project's Github [page](https://github.com/oliverhalberg/payout-calc).


## Example Input File
- Input files should be structured like the following example and should be in `.csv` format. Losses should be recorded as negative numbers. An example .csv file (`example_input.csv`) is included in the repository. Header lines or other lines not containing numerical data in the second column will be skipped.

<table>
<tr>
<td>Name</td><td>Earnings</td>
</tr>
<tr>
<td>A</td><td>50</td>
</tr>
<tr>
<td>B</td><td>-20</td>
</tr>
<tr>
<td>C</td><td>-40</td>
</tr>
<tr>
<td>D</td><td>10</td>
</tr>
</table>

Running the program with `example_input.csv` as input will result in the following being written to the output file:

C pays A 40.0

B pays A 10.0

B pays D 10.0