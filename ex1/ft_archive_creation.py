import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        try:
            file: typing.IO[str] = open(file_name)
            content = file.read()
            print("---\n")
            print(content)
            print("---")
            file.close()
            print(f"File '{file_name}' closed.")
            split_content = content.split('\n')
            new_list = []
            for line in split_content:
                if line != '':
                    new_str = line + '#'
                    new_list.append(new_str)
            s = ''
            for i in new_list:
                s += i
                s += '\n'

            print("\nTransform data:")
            print("---\n")
            print(s)
            print("---")
            saving_file_name = input("Enter new file name (or empty): ")
            if (saving_file_name):
                new_file: typing.IO[str] = open(saving_file_name, "w")
                print(f"Saving data to '{saving_file_name}'")
                new_file.write(s)
                print(f"Data saved in file '{saving_file_name}'.")
                new_file.close()
            else:
                print("Not saving data.")
        except OSError as e:
            print(f"Error opening file '{file_name}': {e}")
