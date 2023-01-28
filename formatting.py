def formattedContent(label, content=[], content2=None):
    s = '\n'
    s+= '+' + "-" * 38 + '+\n'
    s+= '|' + format(label, '^38s') + '|\n'
    s+= '+' + "-" * 38 + '+\n'

    for line in content:
        s += '|' + line + '|\n'
    
    s+= '+' + "-" * 38 + '+\n'

    if content2:
        for line in content2:
            s += '|' + line + '|\n'
        s+= '+' + "-" * 38 + '+\n'

    return s

