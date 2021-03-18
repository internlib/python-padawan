def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ''.join(f'{k}="{v}" ' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}> {inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Python Course'),
            tag('strong', 'John', id='jj'),
            tag('span', 'e'),
            tag('strong', 'Marie', id='mm'),
            tag('span', '.'),
            html_class='alert'
            )
    )
