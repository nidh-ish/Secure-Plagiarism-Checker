# ASTRA_AES_Python

## Instructions to run: 

### Dependencies:
- ast api
- astor
- nltk
- bitarray


### Installing dependencies:
pip3 install -r requirements.txt


### Command to run the main file:
python main.py <code_index_1> <path/to/code/1> <code_index_2> <path/to/code/2>


### Examples:
- python main.py 1 TestFiles/Test0_10/15.py 2 TestFiles/Test0_10/37.py
- python main.py 1 TestFiles/Test0_10/6095.py 2 TestFiles/Test0_10/6006.py


### How to run all test files:
python generate_timestamps.py


### Running the analysis to get the averages:
- python generate_timestamps.py
- python analysis.py