# encoding=utf-8
# !/usr/bin/python


# import pymysql
import json
import os
import requests
import boto3
from django.http import HttpResponse
from snippets import randomId
import json
import pymysql
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
import subprocess


import sys

# xhqb test1-3
mysqlHost = 'xhtestdb01.cq5skzcvpodr.rds.cn-north-1.amazonaws.com.cn'
mysqlUser = 'xhtest'
mysqlPasswd = 'xh_test'
mysqlDataBase = 'underwriter'
# xhqb test6
mysqlHost6 = 'testdb01.cq5skzcvpodr.rds.cn-north-1.amazonaws.com.cn'


class Mysql(object):
    """
        MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现
        获取连接对象：conn = Mysql.getConn()
        释放连接对象;conn.close()或del conn
    """
    #连接池对象
    db1 = None
    db6 = None

    @staticmethod
    def getConn1():
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        if Mysql.db1 is None:
            db1 = PooledDB(creator=pymysql, mincached=1 , maxcached=20 ,
                              host=mysqlHost , port=3306, user=mysqlUser, passwd=mysqlPasswd,
                              db=mysqlDataBase,use_unicode=False,charset='utf8',cursorclass=DictCursor)
        return db1.connection()

    @staticmethod
    def getConn6():
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        if Mysql.db6 is None:
            db6 = PooledDB(creator=pymysql, mincached=1 , maxcached=20 ,
                              host=mysqlHost6 , port=3306, user=mysqlUser, passwd=mysqlPasswd,
                              db=mysqlDataBase,use_unicode=False,charset='utf8',cursorclass=DictCursor)
        return db6.connection()

    @staticmethod
    def getDbInstance(testEnv):
        if testEnv in ['test1', 'test2', 'test3']:
            return Mysql.getConn1()
        if testEnv in ['test6']:
            return Mysql.getConn6()



# 打开数据库连接
# db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
# db1 = pymysql.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDataBase, charset='utf8')
# db6 = pymysql.connect(mysqlHost6, mysqlUser, mysqlPasswd, mysqlDataBase, charset='utf8')


def getDbInstance(testEnv):
    if testEnv in ['test1','test2','test3']:
        PooledDB(creator=pymysql, mincached=1, maxcached=20,
                 host=mysqlHost, port=3306, user=mysqlUser, passwd=mysqlPasswd,
                 db=mysqlDataBase, use_unicode=False, charset='utf8', cursorclass=pymysql.cursors)
    if testEnv in ['test6']:
        return PooledDB(creator=pymysql, mincached=1 , maxcached=20 ,
                              host=mysqlHost6 , port=3306, user=mysqlUser, passwd=mysqlPasswd,
                              db=mysqlDataBase,use_unicode=False,charset='utf8',cursorclass=pymysql.cursors)


def getCurrentJson(execute_action='查询反欺诈1',cid='',testEnv='test1',decisionName='decision'):
    # mmxy
    # mysqlHost = 'krtestdb01.c1gls1uyilgy.rds.cn-northwest-1.amazonaws.com.cn'
    # mysqlUser = 'fengyu'
    # mysqlPasswd = 'e1e29c84ea7'
    # mysqlDataBase = 'underwriter'

    db = Mysql.getDbInstance(testEnv)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    if decisionName == 'decision':
        if cid != '' :
            sqlStr = """
            SELECT
                b.out_param,
                a.reality_execute_user_id,
             a.orderId
            FROM
                underwriter.t_flow_point_execute a
                    LEFT JOIN
                underwriter.t_flow_point_execute_param
                b ON a.execute_point_id = b.execute_point_id
            WHERE
                a.execute_action = '"""+execute_action+"""'
                and a.reality_execute_user_id = '"""+cid.encode("GB18030")+"""'
                and b.out_param is not NULL
            ORDER BY a.operate_time desc  limit 1
            """
        else:
            sqlStr = """
            SELECT
                b.out_param,
                a.reality_execute_user_id,
             a.orderId
            FROM
                underwriter.t_flow_point_execute a
                    LEFT JOIN
                underwriter.t_flow_point_execute_param
                b ON a.execute_point_id = b.execute_point_id
            WHERE
                a.execute_action = '"""+execute_action+"""'
                and b.out_param is not NULL
            ORDER BY a.operate_time desc  limit 1
            """
    elif decisionName == 'lc-decision':
        if cid != '' :
            sqlStr = """
            SELECT
                b.out_param,
                a.reality_execute_user_id,
             a.orderId
            FROM
                minos_zlj.t_flow_point_execute a
                    LEFT JOIN
                minos_zlj.t_flow_point_execute_param
                b ON a.execute_point_id = b.execute_point_id
            WHERE
                a.execute_action = '"""+execute_action+"""'
                and a.reality_execute_user_id = '"""+cid.encode("GB18030")+"""'
                and b.out_param is not NULL
            ORDER BY a.operate_time desc  limit 1
            """
        else:
            sqlStr = """
            SELECT
                b.out_param,
                a.reality_execute_user_id,
             a.orderId
            FROM
                minos_zlj.t_flow_point_execute a
                    LEFT JOIN
                minos_zlj.t_flow_point_execute_param
                b ON a.execute_point_id = b.execute_point_id
            WHERE
                a.execute_action = '"""+execute_action+"""'
                and b.out_param is not NULL
            ORDER BY a.operate_time desc  limit 1
            """


    # print sqlStr
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sqlStr)


    # 使用fetchall函数，将结果集（多维元组）存入rows里面
    rows = cursor.fetchall()
    # print rows
    cursor.close()

    # print  rows
    if len(rows) < 1:
        return  ""
    else:
        jsonStr = rows[0]['out_param']
        # print  jsonStr
        jsonObj = json.loads(str(jsonStr))

        result = {}
        # print  jsonObj['control']['alias']
        # print jsonObj['outputFields']

        result[jsonObj['control']['alias']] = {"outputFields":jsonObj['outputFields']}
        # result[jsonObj['control']['alias']]['outputFields'] = result[jsonObj['outputFields']]

        return json.dumps(result)


# cid：20181029000000012030
def createReport(cid):
    # mysqlHost = 'krtestdb01.c1gls1uyilgy.rds.cn-northwest-1.amazonaws.com.cn'
    # mysqlUser = 'fengyu'
    # mysqlPasswd = 'e1e29c84ea7'
    # mysqlDataBase = 'underwriter'
    allInputFileds = {}
    allInputFiledsInAllPoint ={}
    allStrategy = {}
    allOutputFields = {}
    allOutputFieldsInAllPoint = {}

    # 打开数据库连接
    # db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    # db = pymysql.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDataBase)
    db = Mysql.getDbInstance('test6')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("""
select * from (
   SELECT
    	a.execute_action 审批节点,
    	b.out_param 出参,
    	a.operate_time
    FROM
    	underwriter.t_flow_point_execute a
    LEFT JOIN underwriter.t_flow_point_execute_param b ON a.execute_point_id = b.execute_point_id
    WHERE
    	a.reality_execute_user_id = '"""+cid.encode("GB18030")+"""'
		and b.out_param like '{"control":{"alias%'
    ORDER BY
    	a.operate_time desc limit 10) a
        order by operate_time

    """)
    # and a.execute_action = '查询反欺诈1'

    # 使用fetchall函数，将结果集（多维元组）存入rows里面
    rows = cursor.fetchall()
    cursor.close()

    for row in rows:
        if row[1] in ('None', 'null'):
            allOutputFieldsInAllPoint[row[0]] = row[1]

        elif str(row[1]).startswith("{\"control\":{\""):
            # print(row[1])

            tmp = json.loads(str(row[1]))
            # print(tmp['inputFields'])
            # 策略包别名
            # print(tmp['control']['alias'])
            allStrategy[tmp['control']['alias']] = row[0]
            allOutputFieldsInAllPoint[tmp['control']['alias']] = {}
            for filed in tmp['outputFields']:
                # print(tmp['inputFields'][filed])
                allOutputFieldsInAllPoint[tmp['control']['alias']][filed] = tmp['outputFields'][filed]
                if not (filed in allOutputFieldsInAllPoint):
                    allOutputFields[filed] = {}
                if not tmp['control']['alias'] in allOutputFields[filed]:
                    allOutputFields[filed][tmp['control']['alias']] = tmp['outputFields'][filed]
                else:
                    print("策略包%s字段%s已存在，新值为%s" % (tmp['control']['alias'], filed, tmp['outputFields'][filed]))
            # print(row[1])
        else:
            allOutputFieldsInAllPoint[row[0]] = row[1]

        for row in rows:
            if row[1] in ('None', 'null'):
                allInputFiledsInAllPoint[row[0]] = row[1]

            elif str(row[1]).startswith("{\"control\":{\""):
                # print(row[1])

                tmp = json.loads(str(row[1]))
                # print(tmp['inputFields'])
                # 策略包别名
                # print(tmp['control']['alias'])
                allStrategy[tmp['control']['alias']] = row[0]
                allInputFiledsInAllPoint[tmp['control']['alias']] = {}
                for filed in tmp['outputFields']:
                    # print(tmp['inputFields'][filed])
                    allInputFiledsInAllPoint[tmp['control']['alias']][filed] = tmp['outputFields'][filed]
                    if not (filed in allInputFiledsInAllPoint):
                        allInputFileds[filed] = {}
                    if not tmp['control']['alias'] in allInputFileds[filed]:
                        allInputFileds[filed][tmp['control']['alias']] = tmp['outputFields'][filed]
                    else:
                        print("策略包%s字段%s已存在，新值为%s" % (tmp['control']['alias'], filed, tmp['outputFields'][filed]))
                # print(row[1])
            else:
                allInputFiledsInAllPoint[row[0]] = row[1]
    return (allInputFiledsInAllPoint, allOutputFieldsInAllPoint, allStrategy)





# print getCurrentJson(cid="2018102900000001203")


def gitPushMock(mockText):
    url = 'http://192.168.157.131:8080/jenkins/job/modify-mock-config/buildWithParameters'
    d = {'mockText': mockText}
    r = requests.post(url, data=d,auth=('fengyu','111111'))
    print(r.text)

# gitPushMock()



def publishSQS(queueName,sqsStr):
    # Get the queue
    sqs = boto3.resource('sqs')
    # queue = sqs.get_queue_by_name(QueueName='kr-underwriter-batch-apiSalvationFail-kr-test1')
    queue = sqs.get_queue_by_name(QueueName=queueName)
    # print queue.url

    # Create a new message
    response = queue.send_message(MessageBody=sqsStr)
    # print response.get('MessageId')

# publishSQS('kr-underwriter-batch-apiSalvationFail-kr-test1', '20190107000000013123')
# publishSQS('kr-underwriter-batch-apiPatchSalvationFail-kr-test1','20190107000000013123')


def checkApply(cid):
    # mysqlHost = 'krtestdb01.c1gls1uyilgy.rds.cn-northwest-1.amazonaws.com.cn'
    # mysqlUser = 'fengyu'
    # mysqlPasswd = 'e1e29c84ea7'
    # mysqlDataBase = 'underwriter'
    allInputFileds = {}
    allInputFiledsInAllPoint = {}
    allStrategy = {}
    # allOutputFields = {}
    # allOutputFieldsInAllPoint = {}

    # 打开数据库连接
    # db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    # db = pymysql.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDataBase)
    db = Mysql.getDbInstance('test6')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("""
       SELECT
        	a.execute_action 审批节点,
        	a.examine_remark,
        	a.operate_time
        FROM
        	underwriter.t_flow_point_execute a
        LEFT JOIN underwriter.t_flow_point_execute_param b ON a.execute_point_id = b.execute_point_id
        WHERE
        	a.reality_execute_user_id = '""" + cid.encode("GB18030") + """'
        ORDER BY
        	a.operate_time desc limit 8

        """)
    rows = cursor.fetchall()
    cursor.close()
    # print rows

    results = []
    for row in rows:
        tmp = {}
        tmp['execute_action'] = row[0]
        tmp['examine_remark'] = row[1]
        tmp['operate_time'] = str(row[2])
        results.append(tmp)

    return json.dumps(results,ensure_ascii=False)

#重置身份证

def customer_update(identity_no):
    updateId = randomId.getRandom()
    customer_base(updateId)
    customer_credentials(updateId)
    user_base(updateId)
    edb_user_credential(updateId)
    return HttpResponse('success')

def customer_base(identity_no):
    # mysqlHost = 'krtestdb01.c1gls1uyilgy.rds.cn-northwest-1.amazonaws.com.cn'
    # mysqlUser = 'chenqiongsen'
    # mysqlPasswd = 'e1f6ff7bde1aad'
    # mysqlDataBase = 'cifdb'

    # 打开数据库连接
    # db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    # db = pymysql.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDataBase)
    db = Mysql.getDbInstance('test6')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    #updateId = randomId.getRandom()
    #userInputId = getUserInput()   #接收前端用户输入
    userInputId = '45242119821103002X'   #接收前端用户输入


    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("""update cifdb.t_customer_base set identity_no ='"""+identity_no+"""' where identity_no='"""+userInputId+"""'""")
    #cursor.execute('update cifdb.t_customer_base set identity_no =' + updateId + ' where identity_no=' + userInputId)
    db.commit()
    cursor.close()
    return HttpResponse(identity_no)


#kr-test1, cifdb.t_customer_credentials

def customer_credentials(identity_no):
    # mysqlHost = 'krtestdb01.c1gls1uyilgy.rds.cn-northwest-1.amazonaws.com.cn'
    # mysqlUser = 'chenqiongsen'
    # mysqlPasswd = 'e1f6ff7bde1aad'
    # mysqlDataBase = 'cifdb'

    # 打开数据库连接
    # db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    # db = pymysql.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDataBase)
    db = Mysql.getDbInstance('test6')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    #updateId = randomId.getRandom()
    #userInputId = getUserInput()   #接收前端用户输入
    userInputId = '45242119821103002X'   #接收前端用户输入


    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("""update cifdb.t_customer_credentials set idcard_no ='"""+identity_no+"""' where idcard_no='"""+userInputId+"""'""")
    db.commit()
    cursor.close()
    return HttpResponse(identity_no)

#mm-test1, edbcif.t_user_base
def user_base(identity_no):
    # mysqlHost = 'mmtestdb01.c1gls1uyilgy.rds.cn-northwest-1.amazonaws.com.cn'
    # mysqlUser = 'chenqiongsen'
    # mysqlPasswd = 'f6ff7bde1aad'
    # mysqlDataBase = 'edbcif'

    # 打开数据库连接
    # db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    # db = pymysql.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDataBase)
    db = Mysql.getDbInstance('test6')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    #updateId = randomId.getRandom()
    #userInputId = getUserInput()   #接收前端用户输入
    userInputId = '45242119821103002X'   #接收前端用户输入


    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("""update edbcif.t_user_base set identity_no ='"""+identity_no+"""' where identity_no='"""+userInputId+"""'""")
    db.commit()
    cursor.close()
    return HttpResponse(identity_no)


#mm-test1, edbcif.t_user_credential
def edb_user_credential(identity_no):
    # mysqlHost = 'mmtestdb01.c1gls1uyilgy.rds.cn-northwest-1.amazonaws.com.cn'
    # mysqlUser = 'chenqiongsen'
    # mysqlPasswd = 'f6ff7bde1aad'
    # mysqlDataBase = 'edbcif'

    # 打开数据库连接
    # db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    # db = pymysql.connect(mysqlHost, mysqlUser, mysqlPasswd, mysqlDataBase)
    db = Mysql.getDbInstance('test6')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    #updateId = randomId.getRandom()
    #userInputId = getUserInput()   #接收前端用户输入
    userInputId = '45242119821103002X'   #接收前端用户输入


    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("""update edbcif.t_user_credential set credential_no ='"""+identity_no+"""' where credential_no='"""+userInputId+"""'""")
    db.commit()
    return HttpResponse(identity_no)


# checkApply('20190107000000013123')
def query_execute_action_name(testEnv,decisionName, key):
    # reload(sys)
    # sys.setdefaultencoding('utf8')
    db = Mysql.getDbInstance(testEnv)
    cursor = db.cursor()

    # print "key:" + key
    # print "decisionName:" + decisionName
    # 使用 execute()  方法执行 SQL 查询
    if decisionName == 'decision':
        cursor.execute("""
                    SELECT 
                        a.execute_action
                    FROM
                        underwriter.t_flow_point_execute a
                            LEFT JOIN
                        underwriter.t_flow_point_execute_param b ON a.execute_point_id = b.execute_point_id
                    WHERE
                        a.execute_action LIKE  '%""" + key + """%'
                            AND b.out_param LIKE '{"control":{"alias%'
                    GROUP BY a.execute_action
                    limit 20
                    """)
    elif decisionName == 'lc-decision':
        cursor.execute("""
            SELECT 
                a.execute_action
            FROM
                minos_zlj.t_flow_point_execute a
                    LEFT JOIN
                minos_zlj.t_flow_point_execute_param b ON a.execute_point_id = b.execute_point_id
            WHERE
                a.execute_action LIKE  '%""" + key + """%'
                    AND b.out_param LIKE '{"control":{"alias%'
            GROUP BY a.execute_action
            limit 20
            """)

    rows = cursor.fetchall()
    # print("rows:")
    # print(rows)
    result = []
    for i in rows:
        # print(str(i['execute_action']))
        result.append(str(i['execute_action'].decode('utf-8')))
    cursor.close
    return json.dumps(result,ensure_ascii=False)


def cmd(shell):
    return subprocess.Popen(shell,stdout=subprocess.PIPE,shell=True).communicate()

#获取证件节点
def get_credential_point(testEnv,id):
    db = Mysql.getDbInstance(testEnv)
    cursor = db.cursor()
    cid = '\''+id+'\''
    in_para_sql = """SELECT b.in_param,b.id FROM underwriter.t_flow_point_execute_param b 
where execute_point_id = (select a.execute_point_id from 
underwriter.t_flow_point_execute a WHERE reality_execute_user_id = 
%s and a.point_id = '00000001' order by 
operate_time DESC LIMIT 1 )"""%cid
    cursor.execute(in_para_sql)
    # print(type(cursor.fetchone()))
    a = cursor.fetchone().get('in_param')
    # b = str(a,'utf-8')
    # print(a)
    in_param = json.loads(a)

    # print(type(in_param))
    # print(in_param)
    # print('>>>>>>>>>>>>>>>>>>>')
    appchannel = in_param.get('appInfo').get('appchannel')
    census_address = in_param.get('census_address')
    gpsAddress = in_param.get('gpsInfo').get('gpsAddress')
    idenNum = in_param.get('idenNum')
    name = in_param.get('name')
    device_info = in_param.get('deviceInfo')
    info = {'cid':id,'idenNum':idenNum,'name':name,'appchannel':appchannel,
            'census_address':census_address,
            'gpsAddress':gpsAddress,'device_info':device_info}
    # print(device_info)
    # print(">>>>>>>>>>>>>>>>>>>",(in_param))
    # i = json.dumps(info).encode("unicode_escape")
    cursor.close()
    # print(type(in_param))
    # # print(type(i))
    # print(info)
    return in_param,info
def get_new_info(testEnv,cid,appchannel,census_address,gpsAddress,idenNum,
                 name,device_info):
    _info = get_credential_point(testEnv,cid)[0]
    # print(_info)
    # print('~~~~~~~~',type(_info))
    # info = json.loads(_info)
    _info['appInfo']['appchannel'] = appchannel
    _info['census_address'] = census_address
    _info['gpsAddress'] = gpsAddress
    _info['idenNum'] = idenNum
    _info['name'] = name
    _info['deviceInfo'] = device_info
    new_in_param = json.dumps(_info)
    # print("--------------",new_in_param)
    # print(">>>>>>>>>>>>1",type(new_in_param))
    return new_in_param
    # return _info

def update_info(testEnv,id,dict):
    db = Mysql.getDbInstance(testEnv)
    cursor = db.cursor()
    # new_in_param = get_new_info(testEnv,cid)
    # in_param = json.dumps(new_in_param).encode('utf-8').decode("unicode_escape")
    # print("这是新的数据入参阿~~~~~\n",new_in_param)
    # print(">>>>>>>>>>>>>>>>2",type(dict))
    param = '\''+dict+'\''
    cid = '\''+id+'\''
    update_sql = """update underwriter.t_flow_point_execute_param set
    in_param = {}
 where execute_point_id = (select a.execute_point_id from
underwriter.t_flow_point_execute a WHERE reality_execute_user_id =
{} and a.point_id = '00000001' order by
operate_time DESC LIMIT 1 )""".format(param,cid)
    cursor.execute(update_sql)
    db.commit()
    cursor.close()
    print("执行结束")




#获取身份证节点
def get_idcard_point(testEnv,id):
    db = Mysql.getDbInstance(testEnv)
    cursor = db.cursor()
    cid = '\''+id+'\''
    in_para_sql = """SELECT b.in_param,b.id FROM underwriter.t_flow_point_execute_param b 
where execute_point_id = (select a.execute_point_id from 
underwriter.t_flow_point_execute a WHERE reality_execute_user_id = 
%s and a.point_id = '00000007' order by 
operate_time DESC LIMIT 1 )"""%cid
    cursor.execute(in_para_sql)
    # print(type(cursor.fetchone()))
    a = cursor.fetchone().get('in_param')
    # b = str(a,'utf-8')
    in_param = json.loads(a)

    print(type(in_param))
    print(in_param)
    print('>>>>>>>>>>>>>>>>>>>')
    appchannel = in_param.get('appInfo').get('appchannel')
    census_address = in_param.get('census_address')
    gpsAddress = in_param.get('gpsInfo').get('gpsAddress')
    idenNum = in_param.get('idenNum')
    name = in_param.get('name')
    info = {'cid':cid,'idenNum':idenNum,'name':name,'appchannel':appchannel,
            'census_address':census_address,
            'gpsAddress':gpsAddress}
    # print(">>>>>>>>>>>>>>>>>>>",(in_param))
    # i = json.dumps(info).encode("unicode_escape")
    cursor.close()
    print(type(in_param))
    # print(type(i))
    print(info)
    return in_param,info
def get_new_info_1(testEnv,cid,appchannel,census_address,gpsAddress,idenNum,
                  name):
    _info = get_credential_point(testEnv,cid)[0]
    # print(_info)
    # print('~~~~~~~~',type(_info))
    # info = json.loads(_info)
    _info['appInfo']['appchannel'] = appchannel
    _info['census_address'] = census_address
    _info['gpsAddress'] = gpsAddress
    _info['idenNum'] = idenNum
    _info['name'] = name
    new_in_param = json.dumps(_info)
    print("--------------",new_in_param)
    # print(">>>>>>>>>>>>1",type(new_in_param))
    return new_in_param
    # return _info

def update_idcard_info(testEnv,id,dict):
    db = Mysql.getDbInstance(testEnv)
    cursor = db.cursor()
    # new_in_param = get_new_info(testEnv,cid)
    # in_param = json.dumps(new_in_param).encode('utf-8').decode("unicode_escape")
    # print("这是新的数据入参阿~~~~~\n",new_in_param)
    print(">>>>>>>>>>>>>>>>2",type(dict))
    param = '\''+dict+'\''
    cid = '\''+id+'\''
    update_sql = """update underwriter.t_flow_point_execute_param set
    in_param = {}
 where execute_point_id = (select a.execute_point_id from
underwriter.t_flow_point_execute a WHERE reality_execute_user_id =
{} and a.point_id = '00000007' order by
operate_time DESC LIMIT 1 )""".format(param,cid)
    cursor.execute(update_sql)
    db.commit()
    cursor.close()
    print("执行结束")

def update_cif_info(testEnv,id,dic):
    db = Mysql.getDbInstance(testEnv)
    cursor = db.cursor()
    cid = '\'' + id + '\''
    name = '\''+dic.get('name')+'\''
    idenNum = '\''+dic.get('idenNum')+'\''
    sql1 = """update cifdb.t_customer_base set identity_no = %s,customer_name = %s where id = %s"""%(idenNum,name,cid)
    sql2 = """update cifdb.t_customer_credentials set idcard_no = %s where cid = %s"""%(idenNum,cid)
    # sql3 = """update maincifdb.t_customer_info set identity_no ='${idNumber}' where mobile_phone ='${phone}'"""
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
    cursor.close()
    print("执行结束")