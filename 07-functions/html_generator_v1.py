def tagblock(text, myclass='success'):
    return f"<div class={myclass}>{text}</div>"


if __name__ == '__main__':
    # test with assertions
    assert tagblock('Success') == "<div class=success>Success</div>"
    assert tagblock('impossible to delete',
                    'error') == "<div class=error>impossible to delete</div>"
    print(tagblock('Success'))
