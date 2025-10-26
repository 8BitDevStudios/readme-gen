import os
import datetime
import platform
import subprocess

OUTPUT_FOLDER = "output"

README_TEMPLATE = """# {project_name}

{description}

## Installation
{installation}

{usage_section}## Author

{author}
"""

MIT_LICENSE_TEMPLATE = """MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def ensure_output_folder():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_readme(project_name, description, installation, author, usage):
    usage_section = ""
    if usage:
        usage_section = f"\n## Usage\n``````\n"
    content = README_TEMPLATE.format(
        project_name=project_name,
        description=description,
        installation=installation,
        author=author,
        usage_section=usage_section
    )
    with open(os.path.join(OUTPUT_FOLDER, "README.md"), "w", encoding="utf-8") as f:
        f.write(content)

def generate_license(author):
    year = datetime.datetime.now().year
    content = MIT_LICENSE_TEMPLATE.format(author=author, year=year)
    with open(os.path.join(OUTPUT_FOLDER, "LICENSE"), "w", encoding="utf-8") as f:
        f.write(content)

def open_output_folder():
    folder_path = os.path.abspath(OUTPUT_FOLDER)
    try:
        if platform.system() == "Windows":
            os.startfile(folder_path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", folder_path])
        else:
            subprocess.Popen(["xdg-open", folder_path])
    except Exception as e:
        print(f"Could not open folder automatically: {e}")
        print(f"Please open the folder manually at: {folder_path}")

def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required. Please enter a value.")

def main():
    project_name = input_non_empty("Project name (required): ")
    description = input_non_empty("Description (required): ")
    installation = input_non_empty("Installation instructions (required): ")
    author = input_non_empty("Author (required): ")
    usage = input("Usage (optional, leave empty to skip): ").strip()

    ensure_output_folder()
    generate_readme(project_name, description, installation, author, usage)

    if input("Add MIT License? (y/n): ").strip().lower() == "y":
        generate_license(author)

    open_output_folder()

if __name__ == "__main__":
    main()