from mcstatus import JavaServer
def check_server_status(server_address):
    try:
        server = MinecraftServer.lookup(server_address)
        status = server.status()
        print("服务器在线")
        print("服务器版本: ", status.version.name)
        print("在线玩家数量: ", status.players.online)
        print("最大玩家数量: ", status.players.max)
    except Exception as e:
        print("服务器离线或无法连接")

# 服务器地址
server_address = "103.71.69.122"

# 检查服务器状态
check_server_status(server_address)