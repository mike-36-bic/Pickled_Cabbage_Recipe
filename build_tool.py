# build_tool.py
import json
import argparse
import os

def clean_package_json(input_path, output_path, keep_dev_dependencies=False):
    """
    Reads a package.json file, removes devDependencies, and saves a new file.

    Args:
        input_path (str): The path to the source package.json file.
        output_path (str): The path where the new package.json file will be saved.
        keep_dev_dependencies (bool): If True, keeps devDependencies. Defaults to False.
    """
    try:
        with open(input_path, 'r') as f:
            package_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Failed to parse {input_path}. Is it a valid JSON file?")
        return

    # Check for the presence of devDependencies and remove if the flag is False
    if not keep_dev_dependencies and "devDependencies" in package_data:
        print("Removing devDependencies for production build...")
        del package_data["devDependencies"]

    # Reformat the JSON with a cleaner indentation for readability
    try:
        with open(output_path, 'w') as f:
            json.dump(package_data, f, indent=2)
        print(f"Successfully generated a new package.json at {output_path}")
    except IOError:
        print(f"Error: Could not write to the file {output_path}.")


def main():
    """
    Main entry point for the CLI application.
    """
    parser = argparse.ArgumentParser(description="A tool to manage local project builds.")
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Sub-parser for the 'clean' command
    clean_parser = subparsers.add_parser('clean', help='Remove devDependencies from package.json')
    clean_parser.add_argument('--keep-dev', action='store_true',
                              help='Keep devDependencies in the output file.')
    
    args = parser.parse_args()

    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'package.json')
    output_file = os.path.join(current_dir, 'dist', 'package.json')

    # Create 'dist' directory if it doesn't exist
    os.makedirs(os.path.join(current_dir, 'dist'), exist_ok=True)
    
    if args.command == 'clean':
        clean_package_json(input_file, output_file, keep_dev_dependencies=args.keep_dev)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
