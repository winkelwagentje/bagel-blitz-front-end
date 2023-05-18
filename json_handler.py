import json

def listen():
    file = "java-output.json"
    Json = json.load(open(file))
    print(Json)
    return Json


def request(info):
    json_info = json.dumps(info)
    filename = "java back end test/python-output.json"
    with open(filename, 'w') as file:
        file.write(json_info)


def clear_local_JSON():
    json_info = json.dumps({"move-status": "NONE"})
    filename = "java-output.json"
    with open(filename, 'w') as file:
        file.write(json_info)


def move_request(board, piece, new_location):
    request({"board-layout": board.layout(), "piece-to-move": piece.name, "moves-to": new_location})
