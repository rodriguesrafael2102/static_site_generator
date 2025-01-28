import re
from textnode import TextNode, TextType

def create_text_node(list_strings, type_text):
    list_text_nodes = []
    for i in range(0, len(list_strings)):
        if list_strings[i] != "":
            if i%2==0:
                list_text_nodes.append(TextNode(list_strings[i], type_text.NORMAL))
            else:
                list_text_nodes.append(TextNode(list_strings[i], type_text))
    return list_text_nodes
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
        for item in old_nodes:
            if delimiter == "**":
                list_strings = item.text.split("**")
                list_text_nodes = create_text_node(list_strings, text_type)
            
            if delimiter == "*":
                list_strings = item.text.split("*")
                list_text_nodes = create_text_node(list_strings, text_type)
            
            if delimiter == "`":
                list_strings = item.text.split("`")
                list_text_nodes = create_text_node(list_strings, text_type)

        return list_text_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL: # anything different than TextType.NORMAL is automatically 
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        images = extract_markdown_images(original_text) # this is extracting tuples that containg image_alt and image_link
        if len(images) == 0:
            new_nodes.append(old_node)
            continue # this is in case there are no images markdown inside this particular old_node. Just append it to the list.

        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1) # this is to split the section into two right on top of the image on the iteration
            
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed.") # if it's not split into two, it is not a valid markdown with an image.
            
            if sections[0] != "": # only appending real text. If the text starts with an image_alt and image_link, will append it directly.
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1] # altering the original_text variable to be the next item of the list, that is, the rest of the text.  
        
    
        if original_text != "": # after the last image is checked, there'll be a lasting text. This one is also checked to see if it needs to become a 
            #TextNode. And with the logic of splitting the original_text, it'll always not be an image.
            new_nodes.append(TextNode(original_text, TextType.NORMAL))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL: # anything different than TextType.NORMAL is automatically added to the list of new_nodes
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        links = extract_markdown_links(original_text) # this is extracting tuples that containg link_text and href_link
        if len(links) == 0:
            new_nodes.append(old_node)
            continue # this is in case there are no images markdown inside this particular old_node. So no list is created. Just append it to the list.

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1) # this is to split the section into two right on top of the link
            #on the iteration
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed.") # if it's not split into two, it is not a valid markdown with an link.
            
            if sections[0] != "": # only appending real text. If the text starts with an link_text and href_link, will append it directly.
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1] # altering the original_text variable to be the next item of the list, that is, the rest of the text.  
        
    
        if original_text != "": # after the last image is checked, there'll be a lasting text. This one is also checked to see if it needs to become a 
            #TextNode. And with the logic of splitting the original_text, it'll always not be an image.
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
            
    return new_nodes

def text_to_textnodes(text):    
    original_textnode=TextNode(text, TextType.NORMAL)
    old_nodes = [original_textnode]
    new_nodes_split_bold = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
    new_nodes_split_italic = []

    for item in new_nodes_split_bold:
        if item.text_type == TextType.NORMAL:
            temp_new_nodes = split_nodes_delimiter([item], "*", TextType.ITALIC)
            new_nodes_split_italic += temp_new_nodes
        else:
            new_nodes_split_italic.append(item)

    new_nodes_split_code = []
    for item in new_nodes_split_italic:
        if item.text_type == TextType.NORMAL:
            temp_new_nodes = split_nodes_delimiter([item], "`", TextType.CODE)
            new_nodes_split_code += temp_new_nodes
        else:
            new_nodes_split_code.append(item)

    new_nodes_split_image = []
    for item in new_nodes_split_code:
        if item.text_type == TextType.NORMAL:
            temp_new_nodes = split_nodes_image([item])
            new_nodes_split_image+=temp_new_nodes
        else:
            new_nodes_split_image.append(item)
    
    definite_new_nodes = []
    for item in new_nodes_split_image:
        if item.text_type == TextType.NORMAL:
            temp_new_nodes = split_nodes_link([item])
            definite_new_nodes+=temp_new_nodes
        else:
            definite_new_nodes.append(item)

    return definite_new_nodes


