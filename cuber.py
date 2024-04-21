import pycuber as pc
import random
import sys

def generate_scramble(length=25):
    moves = ['U', 'D', 'L', 'R', 'F', 'B']
    modifiers = ['', "'", '2']
    scramble = ' '.join(random.choice(moves) + random.choice(modifiers) for _ in range(length))
    return scramble

def parse_pycuber_output(mycube):
    # Assuming cube_output is a list of strings as shown in your example
    # This will extract the individual color markings and convert them to standard notation
    edges = []
    corners = []
    
    edges.append(str(mycube.get_face('U')[2][1])+str(mycube.get_face('F')[0][1])) #UF
    edges.append(str(mycube.get_face('U')[1][2])+str(mycube.get_face('R')[0][1])) #UR
    edges.append(str(mycube.get_face('U')[0][1])+str(mycube.get_face('B')[0][1])) #UB
    edges.append(str(mycube.get_face('U')[1][0])+str(mycube.get_face('L')[0][1])) #UL

    edges.append(str(mycube.get_face('D')[0][1])+str(mycube.get_face('F')[2][1])) #DF
    edges.append(str(mycube.get_face('D')[1][2])+str(mycube.get_face('R')[2][1])) #DR
    edges.append(str(mycube.get_face('D')[2][1])+str(mycube.get_face('B')[2][1])) #DB
    edges.append(str(mycube.get_face('D')[1][0])+str(mycube.get_face('L')[2][1])) #DL

    edges.append(str(mycube.get_face('F')[1][2])+str(mycube.get_face('R')[1][0])) #FR
    edges.append(str(mycube.get_face('F')[1][0])+str(mycube.get_face('L')[1][2])) #FL
    edges.append(str(mycube.get_face('B')[1][0])+str(mycube.get_face('R')[1][2])) #BR
    edges.append(str(mycube.get_face('B')[1][2])+str(mycube.get_face('L')[1][0])) #BL
    #UFR
    corners.append(str(mycube.get_face('U')[2][2])
                   +str(mycube.get_face('F')[0][2])
                   +str(mycube.get_face('R')[0][0]))
    #URB
    corners.append(str(mycube.get_face('U')[0][2])
                   +str(mycube.get_face('R')[0][2])
                   +str(mycube.get_face('B')[0][0]))
    #UBL
    corners.append(str(mycube.get_face('U')[0][0])
                   +str(mycube.get_face('B')[0][2])
                   +str(mycube.get_face('L')[0][0]))
    #ULF
    corners.append(str(mycube.get_face('U')[2][0])
                   +str(mycube.get_face('L')[0][2])
                   +str(mycube.get_face('F')[0][0]))
    #DRF
    corners.append(str(mycube.get_face('D')[0][2])
                   +str(mycube.get_face('R')[2][0])
                   +str(mycube.get_face('F')[2][2]))
    #DFL
    corners.append(str(mycube.get_face('D')[0][0])
                   +str(mycube.get_face('F')[2][0])
                   +str(mycube.get_face('L')[2][2]))
    #DLB
    corners.append(str(mycube.get_face('D')[2][0])
                   +str(mycube.get_face('L')[2][0])
                   +str(mycube.get_face('B')[2][2]))
    #DBR
    corners.append(str(mycube.get_face('D')[2][2])
                   +str(mycube.get_face('B')[2][0])
                   +str(mycube.get_face('R')[2][2]))

    return ' '.join(edges + corners)


def main():
    # Check for the command line argument
    if len(sys.argv) != 2:
        print("Usage: python cuber.py <num_lines>")
        sys.exit(1)
    
    try:
        num_lines = int(sys.argv[1])  # Convert the first argument to an integer
    except ValueError:
        print("Error: <num_lines> must be an integer.")
        sys.exit(1)
    
    output_filename = 'scrambled_moves.txt'
    
    with open(output_filename, 'w') as file:
        for _ in range(num_lines):
            mycube = pc.Cube()
            scramble = generate_scramble()
            mycube(scramble)
            cube_state = parse_pycuber_output(mycube)
            file.write(cube_state + '\n')

    print(f"Generated {num_lines} cube states and saved them to '{output_filename}'.")

if __name__ == "__main__":
    main()
