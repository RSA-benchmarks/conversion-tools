from python.roco import read_vtp, write_msh
from sys import argv


def vtp_to_msh(name_vtp, name_msh):
    """ Converts an vtp file to a Gmsh (.msh) file
    """
    pd = read_vtp(name_vtp)
    write_msh(name_msh, pd)


if __name__ == "__main__":
    if len(argv) == 1:
        print("Please state file for conversion")
        exit()
    n1 = argv[2]
    if len(argv) == 2:
        n2 = n1[:-4] + ".msh"
    if len(argv) == 3:
        n2 = argv[3]
    print("Converting", n1, "to", n2)
    vtp_to_msh(n1, n2)
    print("done.")
