import os

def find_file(filename):
    # 1. Try the name exactly as typed (works for full paths too)
    if os.path.exists(filename):
        return filename
    # 2. Try the folder where this script is saved
    try:
        script_folder = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_folder, filename)
        if os.path.exists(path):
            return path
    except NameError:
        pass
    return None

def count_words(filename):
    path = find_file(filename)
    if path is None:
        print(f"Error: The file '{filename}' was not found.")
        print("Current folder:", os.getcwd())
        return None
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return len(content.split())
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
    except Exception as e:
        print("Something went wrong:", e)
    return None

def main():
    print("=== Word Counter ===")
    filename = input("Enter the text file name (e.g. sample.txt): ")
    total = count_words(filename)
    if total is not None:
        print(f"Total number of words: {total}")

main()
