from textnode import TextNode, TextType
from copystatic import move_files
from gencontent import generate_pages_recursive


def main():
    dummy_textnode = TextNode("This is a text node", TextType.BOLD.value, "https://www.boot.dev")
    print(dummy_textnode.__repr__())

    dir_path_public = "./public"
    dir_path_content = "./content"
    dir_path_static = "./static"
    move_files(dir_path_public, dir_path_static)

    file_path_template = "./template.html"
    generate_pages_recursive(dir_path_content, file_path_template, dir_path_public)

main()