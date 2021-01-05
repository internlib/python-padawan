def tagblock(text, myclass='success', inline=False):
    tag = 'span' if inline else 'div'
    return f"<{tag} class={myclass}>{text}</{tag}>"


if __name__ == '__main__':

    print(tagblock('test1', 'info', True))
    print(tagblock('test2', inline=True))
    print(tagblock('fail', myclass='error'))