import argparse
import os
import glob
from pathlib import Path    

parser = argparse.ArgumentParser(
                    prog='Responsibilities Aggregator',
                    description='Extracts all responsibilities from a given folder')
       
parser.add_argument('-f', '--folder', help='folder you want to explore')      
args = parser.parse_args()

def find_md_files(folder_path):
    md_files = glob.glob(os.path.join(folder_path, '**/*.md'), recursive=True)
    return md_files

def resolve_path(folder_name):
    return  Path("../" + folder_name).resolve()

def extract_responsibilities(md_file_path):
    # Read the markdown file content with utf-8 encoding
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Find the specific table-like structure
    table_start = None
    lines = md_content.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith('| Owner | Responsibility |'):
            table_start = i
            break
    
    if table_start is None:
        return None
    
    skip_patterns = ['| Owner | Responsibility |', '| - | - |']

    table_lines = []
    for line in lines[table_start:]:

      if '|' in line and not any(line.strip().startswith(pattern) for pattern in skip_patterns):
        table_lines.append(line)
      elif '|' not in line:
        break

    if not table_lines:
       None

    responsibilities = []

    for line in table_lines:
        cols = [col.strip() for col in line.split('|')]

        if len(cols) >= 3:
            json_data = {
            'file_path': md_file_path,
            'owner': cols[1],
            'responsibility':  cols[2]
            }

            responsibilities.append(json_data)
       
    
    return responsibilities

def get_all_responsibilities(md_files):
    responsibilities = []
    for file in md_files:
        resp = extract_responsibilities(file)
        
        if resp:
            responsibilities.extend(extract_responsibilities(file))

    return responsibilities

def get_relative_path(target_path, base_file_path):
    rel_path = os.path.relpath(target_path, base_file_path)

    return rel_path

def convert_to_markdown_link(file_path):
    file_name = os.path.basename(file_path)
    title = os.path.splitext(file_name)[0]
    formatted_title = title.replace('-', ' ')

    formattedFilePath = file_path.replace(".md", "/").replace("\\", "/")
    markdown_link = f"[{formatted_title}]({formattedFilePath})"
    
    return markdown_link
    
def create_markdown_table(responsibilities, filePath):
    markdown_table = "| Owner | Governance Area | Responsibility |\n"
    markdown_table += "| - | - | - |\n"

    for item in responsibilities:
        relativePath = get_relative_path(item['file_path'], filePath)

        owner = item['owner']
        responsibility = item['responsibility']
        file_path = convert_to_markdown_link(relativePath)
        markdown_table += f"| {owner} | {file_path} | {responsibility} |\n"

    return markdown_table

def update_owner_table(owner, responsibilities):
    fileName = owner.replace(" ", "-") + ".md"

    problemOwnershipPath = os.path.join(resolve_path(os.path.join("docs", "Ways-of-Working", "Governance", "Problem-Ownership", fileName)))
    
    markdownTable = create_markdown_table(responsibilities, problemOwnershipPath)

    with open(problemOwnershipPath, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = content.replace('[[TableReplace]]', markdownTable)

    with open(problemOwnershipPath, 'w', encoding='utf-8') as file:
        file.write(updated_content)

folder_path = resolve_path(args.folder)
md_files = find_md_files(folder_path)

responsibilities = get_all_responsibilities(md_files)

sorted_data = sorted(responsibilities, key=lambda x: x['owner'])

owners = ['Delivery Owner', "Delivery Team", "Engineering Owner", "Problem Owner", "Product Lead", "UX Lead"]

for owner in owners:
    filtered_data = [item for item in responsibilities if item['owner'] == owner]
    update_owner_table(owner, filtered_data)
    print("Updated " + owner)

remainingResponsibilities = [item for item in responsibilities if item['owner'] not in owners]
update_owner_table("Other Responsibilities", remainingResponsibilities)

print("Updated Other Responsibilities")

