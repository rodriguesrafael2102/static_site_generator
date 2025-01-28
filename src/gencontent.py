from markdown_blocks import markdown_to_blocks, markdown_to_html_node
from copystatic import move_files, copy_files_from_source
import os
import shutil

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    is_there_h1 = False

    for block in blocks:
        if block.startswith("# "):
            title_in_string = block[2:]
            is_there_h1 = True
            break

    if not is_there_h1:
        raise Exception("There is no h1 title.")

    return title_in_string

def write_html_file(from_path, destination_direct, html_string):
    file_name = os.path.basename(from_path.replace(".md", ".html"))
    
    full_file_path = os.path.join(destination_direct, file_name)

    with open(full_file_path, "w", encoding="utf-8") as file:
        file.write(html_string)

    print(f"HTML file saved at: {full_file_path}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    with open(from_path, "r", encoding="utf-8") as file_markdown:
        content_from_path = file_markdown.read()

    with open(template_path, "r", encoding="utf-8") as file_html:
        content_template_path = file_html.read()

    html_parent_node = markdown_to_html_node(content_from_path)

    string_title = extract_title(content_from_path)

    html_string = html_parent_node.to_html()

    result_1 = content_template_path.replace("{{ Title }}", string_title)
    html_string = result_1.replace("{{ Content }}", html_string)
    write_html_file(from_path, dest_path, html_string)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_base_name_source = os.path.basename(dir_path_content)

    for file_name in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, file_name)

        if os.path.isdir(file_path):
            generate_pages_recursive(file_path, template_path, dest_dir_path)   
            continue
    
        if not os.path.dirname(dir_path_content) == ".": 
            new_destination_directory = f"{dest_dir_path}/{dir_base_name_source}"
            os.mkdir(new_destination_directory)
            print(f"Created directory: {new_destination_directory}")
            generate_page(file_path, template_path, new_destination_directory)
        else:
            generate_page(file_path, template_path, dest_dir_path) # como não criou o diretório, posso passar apenas o diretorio de destino, pois ele já é a base