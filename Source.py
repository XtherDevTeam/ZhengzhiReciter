def LoadSource(Path: str):
    with open(Path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        result = []
        temp = {
            'title': '',
            'points': []
        }
        for line in lines:
            while line.endswith('\n') or line.endswith(' '):
                line = line[0:-1]
            if line.startswith('#'):
                if temp['title'] != '':
                    result.append(temp)
                    temp = {
                        'title': '',
                        'points': []
                    }
                temp['title'] = line[1:]
                if temp['title'].startswith(' '):
                    temp['title'] = temp['title'][1:]
            if line.startswith('-'):
                line = line[1:]
                if line.startswith(' '):
                    temp['points'].append(line[1:])
                else:
                    temp['points'].append(line)

        if temp['title'] != '':
            result.append(temp)

        return result
