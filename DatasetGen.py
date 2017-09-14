from faker import Factory
import random
import datetime
import re


f = open('Customer_Orders', 'w')
#f.write('hi there\n')  # python will convert \n to os.linesep
#f.close()  # you can omit in most cases as the destructor will call it
 
#----------------------------------------------------------------------
def create_names2(fake):
    """"""
    payment_mode = ['Credit Card','Paypal','COD','DEBIT CARD','INTERNET BANKING','CASHIERS CHEQUE']
    for i in range(10000000):

        incr = 00012 + i
        order_id = "B0X" + str(incr).zfill(20)
        #print order_id
        cust_id = "CUS" + str(random.randint(0,10000)).zfill(10)
        #print cust_id
        cust_paymnt_mthd_id = "PAYMTHD" + str(random.randint(0,7)).zfill(5)
        #print cust_paymnt_mthd_id
        order_status_cd = str(random.randint(0,9)).zfill(3)
        date_order_plcd = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None)
#        date_order_paid = datetime.datetime.strptime(str(date_order_plcd), "%Y-%m-%d %H:%M:%S")
        date_order_paid = date_order_plcd.strftime("%Y-%m-%d")
        #print date_order_plcd
        #print date_order_paid
        order_pr = "$" + str(random.randint(0,1500))
        out = order_id, cust_id, cust_paymnt_mthd_id, order_status_cd, str(date_order_plcd), date_order_paid, order_pr
        out_new = re.sub('[(){}<>]', '', str(out))
        #print out_new
        f.write(str(out_new))
        f.write('\n')
 
if __name__ == "__main__":
    fake = Factory.create()
    create_names2(fake)


