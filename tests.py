import unittest
from websocket import create_connection
import ssl
import time
# https://github.com/websocket-client/websocket-client
# pip3 install websocket-client

class TestStringMethods(unittest.TestCase):

    def testPingPong(self):
        ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})
        ws2 = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})

        ws.send("player1")
        ws2.send("ESP")

        time.sleep(1)

        ws.send("Ping")
        print("Sent Ping")
        result = ws2.recv()

        ws.close()
        ws2.close()

        self.assertEqual(result, 'Ping')
    
    def testESP(self):
        ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})

        ws.send("ESP")

        time.sleep(1)

        result = ws.recv()

        ws.close()

        self.assertEqual(result, 'ESP Connected')

    # def setESP():
    #     ws = create_connection("wss://www.kazar4.com:9001", sslopt = {"cert_reqs": ssl.CERT_NONE})
    #     print(ws.recv())
    #     print("Sending 'Hello, World'...")
    #     ws.send("Hello, World")
    #     print("Sent")
    #     print("Receiving...")
    #     result =  ws.recv()
    #     print("Received '%s'" % result)
    #     ws.close()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()