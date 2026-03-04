from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newNodes.append(node)
        else:
            splitOnDelimiter = node.text.split(delimiter)
            if len(splitOnDelimiter) % 2 == 0:
                raise Exception("Invalid Markdown")
            for i, part in enumerate(splitOnDelimiter):
                if len(part) == 0:
                   continue 
                if i % 2 == 0:
                    newNodes.append(TextNode(splitOnDelimiter[i], TextType.TEXT))
                else:
                    newNodes.append(TextNode(splitOnDelimiter[i], text_type))    
    return newNodes

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
    node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes2 = split_nodes_delimiter([node2], "`", TextType.CODE)
    print(new_nodes2)
    for i in new_nodes:
        print(i)

if __name__ == "__main__":
    main()