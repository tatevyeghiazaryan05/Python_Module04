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
            file: typing.IO[str] = open(file_name, "r")
            content = file.read()
            print("---\n")
            print(content)
            print("---")
            file.close()
            print(f"File '{file_name}' closed.")
            s = ""
            for line in content.split("\n"):
                if line:
                    s += line + "#\n"
            print("\nTransform data:")
            print("---\n")
            print(s)
            print("---")
            try:
                sys.stdout.write("Enter new file name (or empty): ")
                sys.stdout.flush()
                saving_file_name = sys.stdin.readline()
                saving_file_name = saving_file_name.strip()
                if (saving_file_name):
                    print(f"Saving data to '{saving_file_name}'")
                    new_file: typing.IO[str] = open(saving_file_name, "w")
                    new_file.write(s)
                    new_file.close()
                    print(f"Data saved in file '{saving_file_name}'.")
                else:
                    print("Not saving data.")
            except OSError as e:
                sys.stderr.write(f"[STDERR] Error opening file "
                                 f"'{saving_file_name}': {e}\n")
                print("Data not saved.")
        except OSError as e:
            sys.stderr.write(f"[STDERR] Error opening file "
                             f"'{file_name}': {e}\n")
