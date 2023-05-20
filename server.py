from vidstream import StreamingServer
import threading

receiver = StreamingServer('127.0.0.1', 65432)
t = threading.Thread(target=receiver.start_server)
t.start()

while input('') != 'STOP':
    continue

receiver.stop_server()