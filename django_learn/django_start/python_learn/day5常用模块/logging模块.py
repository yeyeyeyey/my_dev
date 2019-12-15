import logging
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('This is a new file')
# logging.info('So should this')
# logging.warn('And this,too')
#


# logger提供了应用程序可以直接使用的接口；
#
# handler将(logger创建的)日志记录发送到合适的目的输出；
#
# filter提供了细度设备来决定输出哪条日志记录；
#
# formatter决定日志记录的最终输出格式。
# logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m %d %Y '
#                                                              '%I:%M:%S %P')
# logging.warn('is when this event was logged')
#
#logger
# 每个程序在输出信息之前都要获得一个Logger。Logger通常对应了程序的模块名

LOG = logging.getLogger('chat.gui')

LOG.lo