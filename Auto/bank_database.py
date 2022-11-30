import pymysql
import decimal


DB=None


class Account:
    def __init__(self, account_id, account_passwd):
        self.account_id = account_id
        self.account_passwd = account_passwd

    # 登录检查
    def check_account(self):
        cursor = DB.cursor()
        try:
            SQL = "select * from account where account_id=%s and account_passwd=%s" \
                  % (self.account_id, self.account_passwd)
            cursor.execute(SQL)
            if cursor.fetchall():
                return True
            else:
                return False
        except Exception as e:
            print("错误", e)
        finally:
            cursor.close()

    # 查询余额
    def query_money(self):
        cursor = DB.cursor()
        try:
            SQL = "select money from account where account_id=%s and account_passwd=%s" \
                %(self.account_id, self.account_passwd)
            cursor.execute(SQL)
            money = cursor.fetchone()[0]
            if money:
                return str(money.quantize(decimal.Decimal('0.00')))
            else:
                return 0.00
        except Exception as e:
            print("错误原因",e)
        finally:
            cursor.close()

    # 取钱
    def reduce_money(self, money):
        cursor = DB.cursor()
        try:
            has_money=self.query_money()
            if decimal.Decimal(money) <= decimal.Decimal(has_money):
                SQL = "update account set money=money-%s where account_id=%s and account_passwd=%s" \
                      % (money, self.account_id, self.account_passwd)
                cursor.execute(SQL)
                if cursor.rowcount == 1:
                    DB.commit()
                    return True
                else:
                    DB.rollback()
                    return False
            else:
                print("余额不足")
        except Exception as e:
            print("错误原因",e)
        finally:
            cursor.close()

    # 存钱
    def add_money(self, money):
        cursor = DB.cursor()
        try:
            SQL = "update account set money=money+%s where account_id=%s and account_passwd=%s" \
                  % (money, self.account_id, self.account_passwd)
            cursor.execute(SQL)
            if cursor.rowcount == 1:
                DB.commit()
                return True
            else:
                DB.rollback()
                return False
        except Exception as e:
            DB.rollback()
            print("错误原因", e)
        finally:
            cursor.close()


# MIAN
if __name__ == "__main__":
    global DB
    DB = pymysql.connect(host="localhost", user="root", passwd="1234", charset="utf8", database="bank")
    cursor = DB.cursor()
    from_account_id = input("请输入账号：")
    from_account_passwd = input("请输入密码：")
    account = Account(from_account_id, from_account_passwd)
    if account.check_account():
        choose = input("请输入操作：\n1、查询余额\n2、取钱\n3、存钱\n4、取卡\n")
        while choose != "4":
            # 查询
            if choose == "1":
                print("您的余额是%s元" % account.query_money())
            # 取钱
            elif choose == "2":
                money = input("您的余额是%s元,请输入取款金额" % account.query_money())
                if account.reduce_money(money):
                    print("取款成功，您的余额还有%s元" % account.query_money())
                else:
                    print("取款失败！")
            # 存钱
            elif choose == "3":
                money = input("请输入存款金额：")
                if account.add_money(money):
                    print("存款成功，您的余额还有%s元，按任意键继续\n" % (account.query_money()))
                else:
                    print("存款失败，按任意键继续")
            choose = input("请输入操作：\n1、查询余额\n2、取钱\n3、存钱\n4、取卡\n")
        else:
            print("谢谢使用！")
    else:
        print("账号或密码错误")
    DB.close()
