def lab1(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            values = line.split(",")
            values = [int(x) for x in values]
            print(
                f"The average of {values[0]} and {values[1]} is {(values[0] + values[1]) / 2}"
            )


lab1(input('Enter the file name:'))


def reverse(infile, outfile):
    with open(infile) as ifile:
        lines = list(reversed(ifile.readlines()))
        lines[0] = lines[0] + '\n'
        with open(outfile, "w") as ofile:
            ofile.writelines(lines)

            ofile.close()
        ifile.close()


reverse("input.txt", "output.txt")
