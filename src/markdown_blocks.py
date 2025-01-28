
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph="paragraph"
block_type_heading="heading"
block_type_code="code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())
        
    return filtered_blocks

def block_to_block_type(single_block):
    lines = single_block.split("\n")
    
    if single_block.startswith(("# ","## " , "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    
    if len(lines) > 1 and lines[1].startswith("```") or lines[-1].startswith("```"):
        return block_type_code
    
    if single_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    if single_block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    
    if single_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist

    if single_block.startswith("1. "):
        i=1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i+=1
        return block_type_olist
    
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def create_quote_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def create_paragraph_html_node(block):
    split_block = block.split("\n")
    block_without_new_line = " ".join(split_block)
    children=text_to_children(block_without_new_line)
    return ParentNode("p", children, None) 

def create_heading_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def create_code_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[3:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def create_ulist_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def create_olist_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children=[]
    for block in blocks:
        #Determine the type of block (you already have a function for this)
        block_type = block_to_block_type(block)
        #Based on the type of block, create a new HTMLNode with the proper data
        if block_type == block_type_heading:
            html_node = create_heading_html_node(block)
        if block_type == block_type_code:
            html_node = create_code_html_node(block)
        if block_type == block_type_quote:
            html_node = create_quote_html_node(block)
        if block_type == block_type_ulist:
            html_node = create_ulist_html_node(block)
        if block_type == block_type_olist:
            html_node = create_olist_html_node(block)
        if block_type == block_type_paragraph:
            html_node = create_paragraph_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


