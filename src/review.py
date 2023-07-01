def review(config):
    merge = config['merge']

    comments = []

    if 'assignee' not in merge or merge['assignee'] is None:
        comments.append({
            "id": "1",
            "comment": "Assignned não atribuído"
        })

    return comments
