import unittest
from websocket import create_connection
import ssl
import time
# https://github.com/websocket-client/websocket-client
# pip3 install websocket-client

class TestWebsocketMethods(unittest.TestCase):

    # tests basic integration between mocked webapp and mocked ESP
    # both can send commands to each other
    def testPingPong(self):
        ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})
        ws2 = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})

        ws.send("player1")
        ws2.send("ESP")
        ws.recv()
        ws2.recv()

        time.sleep(1)

        ws.send("Ping")
        #print("Sent Ping")
        result = ws2.recv()

        ws.close()
        ws2.close()

        self.assertEqual(result, 'Ping')
    
    # tests that a mock ESP can be created
    def testESP(self):
        ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})

        ws.send("ESP")

        result = ws.recv()

        ws.close()

        self.assertEqual(result, 'ESP Connected')
    
    # tests that a mock player can be created
    def testPlayer1(self):
        ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})

        ws.send("player1")

        result = ws.recv()

        ws.close()

        self.assertEqual(result, 'player1 Connected')
    
    # tests that an invalid game command is thrown out/ignored
    def invalidCommand(self):
        ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})

        ws.send("player1")
        ws.recv()

        time.sleep(1)

        ws.send("A VERY INVALID COMMAND")

        result = ws.recv()

        ws.close()

        self.assertEqual(result, 'invalid command')
    
    # tests that a valid game command is sent from player to ESP
    def testGameMove(self):
        ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})
        ws2 = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})

        ws.send("player1")
        ws2.send("ESP")
        ws.recv()
        ws2.recv()

        time.sleep(1)

        ws.send("U")
        #print("Sent Up")
        result = ws2.recv()

        ws.close()
        ws2.close()

        self.assertEqual(result, 'U')

if __name__ == '__main__':
    unittest.main()