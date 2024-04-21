# Cube Scrambler and State Parser
## Overview
This Python script utilizes the pycuber library to generate random scrambles for a Rubik's Cube and then parses the resulting cube states into a human-readable format. It's designed to help cube enthusiasts and researchers analyze different scramble sequences and their impact on cube states.

## Features
- Random Scramble Generation: Creates scramble moves for a Rubik's Cube.
- State Parsing: Converts the scrambled cube's state into a standardized format that lists the position of all edges and corners.
- File Output: Outputs multiple cube states to a text file, each corresponding to a different scramble.
## Installation
Before running the script, ensure you have Python installed on your system. This script was tested with Python 3.10. You'll also need to install the pycuber library, which can be installed via pip:
```
pip install pycuber
```

## Usage
To run the script, use the command line. The script requires one argument that specifies the number of cube states to generate and save:
```
python cuber.py <num_lines>
```
Where <num_lines> is the number of different scrambles (and corresponding cube states) you want to generate.

## Example
To generate 10 different cube states:
```
python cuber.py 10
```
This will create a file named scrambled_moves.txt containing 10 different cube states.

## Output Format
The output file scrambled_moves.txt will contain lines where each line represents a cube state. Each cube state is a list of all edges followed by all corners, with each piece represented by its colors in a specific order (e.g., UFR for Upper-Front-Right corner).

## Contributing
Feel free to fork the repository and submit pull requests. You can also open issues if you find bugs or have feature requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
