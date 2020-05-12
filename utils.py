from collections import deque

queue = deque()
matches = {}

find_match(name):
    if name not in matches:
        matches[name] = None
    if not queue:
        queue.append(name)
        return None
    if queue[0] == name:
        return None
    if matches[name] != None:
        return matches[name]
    else:
        match = queue.popleft()
        matches[match] = name
        matches[name] = match
        return match

remove_match(name, match):
    matches[name] = None
    matches[match] = None

find_new_match(name, match):
    remove_match(name, match)
    if queue and queue[0] == match:
        return None
    return find_match(name, match)
