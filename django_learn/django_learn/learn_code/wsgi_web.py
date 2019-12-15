from  wsgiref.simple_server import make_server
def run_server():
    print('heiheihei')
s=make_server('localhost',8070,run_server)
s.serve_forever()