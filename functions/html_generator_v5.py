def get_atrs(attributes):
    return ''.join(f'{k.split("_")[-1]}="{v}"'
                   for k, v in attributes.items())


def tag_block(content, *args, select_class='success', inline=False, **new_atrs):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args, **new_atrs)
    attributes = get_atrs(new_atrs)
    return f'<{tag} {attributes} class="{select_class}">{html}</{tag}>'


def tag_list(*itens, **new_atrs):
    list = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul{get_atrs(new_atrs)}> {list} </ul>'


if __name__ == '__main__':
    print(tag_block(tag_list('itemx', 'itemy'), select_class='info',
                    block_accesskey='m', block_id='content', ul_id='list', inline=True))
