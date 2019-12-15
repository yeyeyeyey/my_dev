# 面向对象：
# 1.封装
# 即把客观事物封装成抽象的类，并且类可以把自己的数据和方法让可信的类进行操作，对不可信的进行隐藏
# 2.继承
# 3.多态
#领域模型
#发掘重要的业务领域概念，建立业务领域概念之间的关系
#找名词，加属性，连关系
class Role(object):
    def __init__(self,name,role,weapon,attack,life_value = 100,money = 10000):
        self.name = name
        self.role =role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.attack = attack
    def shot(self,other):
        print('%s 在射击' %self.name)
        print('%s跟%s在中路拼枪' %(self.name,other.name))
        self.life_value = int(self.life_value)-int(other.attack)
        if self.life_value > 0:
            print('%s活下来了，还剩下%s血'%(self.name,self.life_value))
        else:
            print('%s挂了,充点钱吧，充钱才能更强'%self.name)
    def get_shot(self,attract):
        # self.life_value -= int(attract)
        print('%s 被射中了,还剩下%s 血' %(self.name,self.life_value))

    def arm(self,gun):
        self.attack =int(self.attack)+int(gun.attack)
        self.weapon = gun.name
        self.money =int(self.money)-int(gun.money)
        print('%s %s 装备了%s,攻击力提升啦，竟然达到了惊人的%s 点' %(self.role,self.name,
                                                  self.weapon,self.attack))
        print('%s 买了%s，还剩下 %s元钱' %(self.name,gun.name,self.money))

class Gun(object):
    def __init__(self,name,attack,money):
        self.name=name
        self.attack = attack
        self.money = money
ak47 = Gun('AK47','89','3000')
an94 = Gun('AN94','90','5000')
lsj  = Role('lsj','police','knief',10)
wyz  = Role('wyz','bandit','knief',10)

lsj.arm(ak47)
wyz.arm(an94)
lsj.shot(wyz)
wyz.shot(lsj)