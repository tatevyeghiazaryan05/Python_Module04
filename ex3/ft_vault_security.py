def secure_archive(file_name: str, action: str = "read",
                   add_line: str | None = None) -> tuple[bool, str]:
    if action in ("read", "write"):
        if action == "read":
            try:
                with open(file_name, "r") as file:
                    content = file.read()
                    return (True, content)
            except OSError as e:
                return (False, str(e))
        elif action == "write":
            try:
                with open(file_name, "w") as file:
                    if add_line or add_line == "":
                        file.write(add_line)
                        return (True, "Content successfully written to file")
                    else:
                        return (False, "No content provided")
            except OSError as e:
                return (False, str(e))
    return (False, "Invalid action")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/non/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("ancient_fragment.txt", "write", "Hello"))
