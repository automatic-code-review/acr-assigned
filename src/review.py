def review(config):
    merge = config['merge']

    comments = []

    if 'assignee' not in merge or merge['assignee'] is None:
        if 'message' in config:
            message = config['message']
        else:
            message = "Assignned não atribuído"

        comment = {
            "id": "NOT_ASSIGNED",
            "comment": message
        }

        if 'processorArgs' in config:
            comment['processorArgs'] = config['processorArgs']

        comments.append(comment)

    else:
        author = merge['author']
        assigned_to = merge['assignee']

        if 'allowList' in config:
            allow_list = config['allowList']
            allow_list = [username.replace("${AUTHOR_MERGE}", author) for username in allow_list]

            if assigned_to not in allow_list:
                message = config['allowMessage'].replace("${USERS}", ", ".join(allow_list))
                comments.append({
                    "id": "ALLOW_LIST",
                    "comment": message
                })

        if 'denyList' in config:
            deny_list = config['denyList']
            deny_list = [username.replace("${AUTHOR_MERGE}", author) for username in deny_list]

            if assigned_to in deny_list:
                message = config['denyMessage'].replace("${USERS}", ", ".join(deny_list))
                comments.append({
                    "id": "DENY_LIST",
                    "comment": message
                })

    return comments
