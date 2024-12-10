import socket

def search_minecraft_server(host, port):
    try:
        status, protocol, version, title, numplayers, maxplayers = "未知状态", "\000", "\000", "\000", "\000", "\000"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            s.sendall(b'\xFE\x01')
            data = s.recv(1024).split(b'\x00\x00')

        if len(data) >= 6:
            packet_id = data[0][0]
            if packet_id == 255:
                status, protocol, version, title, numplayers, maxplayers = data[0], data[1], data[2], data[3], data[4], data[5]
        
        return status, protocol, version, title, numplayers, maxplayers

    except socket.error as e:
        print("Socket error:", e)
        return "离线", "\000", "\000", "\000", "\000", "\000"
    except Exception as e:
        print("Error:", e)
        return "离线", "\000", "\000", "\000", "\000", "\000"

def parse_minecraft_data(data):
    if len(data) >= 6:
        title = data[3].decode('utf-16be')
        numplayers = int(data[4].decode('utf-16be'))
        maxplayers = int(data[5].decode('utf-16be'))

        return title, numplayers, maxplayers
    return None, 0, 0

def myworld(host, port):
    status, protocol, version, title, numplayers, maxplayers = search_minecraft_server(host, port)
    
    if status != "离线":
        title, numplayers, maxplayers = parse_minecraft_data((status, protocol, version, title, numplayers, maxplayers))
        return f"服务器标题: {title}, 当前玩家: {numplayers}, 最大玩家: {maxplayers}"
    else:
        return "服务器离线"
