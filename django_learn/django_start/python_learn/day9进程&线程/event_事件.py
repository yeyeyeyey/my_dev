# import time,threading,random
#
# event = threading.Event
#
#
# def light():
#     if not event.is_set():
#         event.set()#wait就不阻塞，绿灯
#         #