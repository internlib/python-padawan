def tag_block(content, *args, select_class='success', inline=False):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)
    return f'<{tag} class="{select_class}">{html}</{tag}>'


def tag_list(*itens):
    list = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul> {list} </ul>'


if __name__ == '__main__':
    print(tag_block(tag_list('Item1', 'Item2'), select_class='info'))
    # mandatory to use named parameters
    print(tag_block(tag_list('x', 'y'), select_class='info', inline=True))
