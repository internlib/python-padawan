def tagblock(text, myclass='success', inline=False):
    tag = 'span' if inline else 'div'
    return f"<{tag} class={myclass}>{text}</{tag}>"


def tag_list(*items):
    list = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul>{list}</ul>'


if __name__ == '__main__':

    print(tagblock('test1', 'info', True))
    print(tagblock('test2', inline=True))
    print(tagblock('fail', myclass='error'))
    print(tagblock(inline=True, text="test3", myclass="info"))
    print(tagblock(tag_list('Item1', 'Item2', 'Item3'), myclass='info'))
