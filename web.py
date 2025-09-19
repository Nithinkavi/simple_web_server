from http.server import HTTPServer,BaseHTTPRequestHandler
content ="""<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: rgb(96, 216, 250);
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1 {
            color: #0b0b0b;
            text-align: center;
        }

        table {
            width: 80%;
            max-width: 800px;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #5ffffa;
        }

        th, td {
            border: 3px solid #0a0a0a;
            padding: 12px;
            text-align: left;
            vertical-align: top;
        }

        th {
            background-color: #09a2f4;
            color: rgb(5, 5, 5);
        }

        tr:nth-child(even) {
            background-color: #28f7f7;
        }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>

    <table>
        <tr>
            <th>Layer</th>
            <th>Protocols</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>
                HTTP<br>
                HTTPS<br>
                FTP<br>
                DNS<br>
                Telnet<br>
                SSH
            </td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>
                TCP<br>
                UDP
            </td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>
                IP<br>
                ICMP<br>
                IPv4<br>
                IPv6<br>
            </td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>
                Ethernet<br>
                Wi-Fi (IEEE 802.11)<br><br>
            </td>
        </tr>
    </table>
</body>
</html>"""
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request recevied...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()