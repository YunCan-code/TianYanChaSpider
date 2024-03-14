# @Time    : 2024/2/28 15:32
# @Author  : Sxl
# @File    : 天眼查重构.py
# 加入地区及行业自动选择 2024 03 11

import time
import re
import csv
# from 天眼登录 import login, logInfo

# 相关模块导入
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import random

# 文件名
file_name = '剩余区县开发区软件行业.csv'
# 爬虫起始页，爬虫失败重启后更改起始页
start_page = 1
# 用户名
user_name = '123456'
# 密码
pass_word = '123456'
# 地区选择

# 行业选择



# 日志文件
# logInfo()

# selenium 4版本必须要设置浏览器选项，否则会闪退
option = webdriver.EdgeOptions()
# option.add_argument("--headless")
option.add_experimental_option("detach", True)
# 实例化浏览器驱动对象，并将配置浏览器选项
driver = webdriver.Edge(options=option)

# 打开https://www.tianyancha.com/首页
driver.get("https://www.tianyancha.com/")
time.sleep(1)
# 点击登录、注册按钮
driver.find_element(By.XPATH, '//*[@id="page-header"]/div/div[2]/div/div[5]/span').click()
time.sleep(2)
# 选择非扫码登录
driver.find_element(By.XPATH, '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[2]').click()
time.sleep(1)
# 密码登录
driver.find_element(By.XPATH,
                    '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]').click()
# 输入账号密码
driver.find_element(By.XPATH,
                    '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[1]/input').send_keys(
    user_name)  # 16651002812
time.sleep(random.uniform(0.1, 3))
driver.find_element(By.XPATH,
                    '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/input').send_keys(
    pass_word)  # cc123456
time.sleep(random.uniform(0.1, 3))
# 同意条款
driver.find_element(By.XPATH,
                    '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[3]/input').click()
# 登录按钮
driver.find_element(By.XPATH,
                    '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/button').click()

time.sleep(15)
# 验证码识别，暂时使用手工

# 高级筛选
diff_choice = driver.find_element(By.XPATH, '//*[@id="page-container"]/div[2]/div[1]')
driver.execute_script("arguments[0].click();", diff_choice)
time.sleep(10)
# 选择最新的选项卡
# 1. 获取当前所有的标签页的句柄构成的列表
current_windows = driver.window_handles

# 2. 根据标签页句柄列表索引下标进行切换
driver.switch_to.window(current_windows[1])

# 新版本行业地区选择
# 行业及代码
print("请提前确定好行业与地区的搭配，确保其搭配的数据量小于5000条")
# hangye_1 = input('建筑业是否全选（N/Y）：')

# 点击行业
hy_choice = driver.find_element(By.XPATH, '//*[@id="cascader_category"]/span/span[1]')
driver.execute_script("arguments[0].click();", hy_choice)
# time.sleep(random.uniform(0.1, 3.2))
a = driver.find_elements(By.XPATH, '//*[@id="cascader_category"]/div/div[1]/div[1]/ul/li')
for i, k in enumerate(a):
    print(i + 1, k.text)
b = input("行业选择(1/3)：")
c = input("是否全选(y/n)：")
print("------------------")
if c == 'n':
    driver.find_element(By.XPATH,'//*[@id="cascader_category"]/div/div[1]/div[1]/ul/li'+'['+str(b)+']/span').click()

    f = driver.find_elements(By.XPATH, '//*[@id="cascader_category"]/div/div[1]/div[2]/ul/li/span')
    val = True
    while val:
        for i, k in enumerate(f):
            print(i + 1, k.text)
        d = input("行业选择(2/3)：")
        e = input("是否全选(y/n)：")
        print("------------------")
        if e == 'n':
            driver.find_element(By.XPATH, '//*[@id="cascader_category"]/div/div[1]/div[2]/ul/li[' + str(d) + ']/span').click()

            g = driver.find_elements(By.XPATH,'//*[@id="cascader_category"]/div/div[1]/div[3]/ul/li/span')

            val_2 = True
            while val_2:
                for o,p in enumerate(g):
                    print(o+1,p.text)
                h = input("行业选择(3/3)：")
                print("------------------")
                # j = input("是否全选(y/n)：")
                driver.find_element(By.XPATH,
                                    '//*[@id="cascader_category"]/div/div[1]/div[3]/ul/li[' + str(h) + ']/label/span').click()
                val_s = input('第三列是否继续选择(y/n)：')
                if val_s == 'n':
                    val_2 = False
            val_s = input('第二列是否继续选择(y/n)：')
            if val_s == 'n':
                val = False
        else:
            driver.find_element(By.XPATH, '//*[@id="cascader_category"]/div/div[1]/div[2]/ul/li[' + str(d) + ']/label/span').click()
            val_s = input('第二列是否继续选择(y/n)：')
            if val_s == 'n':
                val = False
else:
    driver.find_element(By.XPATH,'//*[@id="cascader_category"]/div/div[1]/div[1]/ul/li'+'['+str(b)+']/label/span').click()

# 行业确定
driver.find_element(By.XPATH, '//*[@id="cascader_category"]/div/div[2]/div/div[2]').click()

# 地区选择
driver.find_element(By.XPATH, '//*[@id="cascader_area"]/span/span[1]').click()
# time.sleep(random.uniform(0.1, 3.2))

fir = driver.find_elements(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[1]/ul/li')
for i,k in enumerate(fir):
    print(i+1,k.text)
fir_1 = input("请选择要爬取的地区(1/3)：")
fir_v = input("是否全选(y/n)：")
print("------------------")
if fir_v == 'n':
    driver.find_element(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[1]/ul/li['+str(fir_1)+']/span').click()

    se = driver.find_elements(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[2]/ul/li')
    val = True
    while val:
        for se_i,se_k in enumerate(se):
            print(se_i+1,se_k.text)
        se_1 = input("请选择要爬取的地区(2/3)：")
        se_2 = input("是否全选(y/n)：")
        print("------------------")

        if se_2 == 'n':
            driver.find_element(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[2]/ul/li['+str(se_1)+']/span').click()
            th_1 = driver.find_elements(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[3]/ul/li')

            val_2 = True
            while val_2:
                for th_i,th_k in enumerate(th_1):
                    print(th_i+1,th_k.text)
                th_2 = input("请选择要爬取的地区(3/3)：")
                print("------------------")
                # th_3 = input("是否全选(y/n)：")
                driver.find_element(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[3]/ul/li['+str(th_2)+']/label/span').click()
                val_s = input('第三列是否继续选择(y/n)：')
                if val_s == 'n':
                    val_2 = False
            val_s = input('第二列是否继续选择(y/n)：')
            if val_s == 'n':
                val = False
        else:
            driver.find_element(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[2]/ul/li['+str(se_1)+']/label/span').click()
            val_s = input('第二列是否继续选择(y/n)：')
            if val_s == 'n':
                val = False
else:
    driver.find_element(By.XPATH,'//*[@id="cascader_area"]/div/div[1]/div[1]/ul/li['+str(fir_1)+']/label/span').click()

# 地区确定
driver.find_element(By.XPATH, '//*[@id="cascader_area"]/div/div[2]/div/div[2]').click()
time.sleep(random.uniform(0.1, 3.2))

# 存续 在业
driver.find_element(By.XPATH, '//*[@id="web-content"]/div/div/div[2]/div[7]/div[2]/div[1]/div').click()
time.sleep(random.uniform(0.1, 3.2))
# 查看筛选结果
driver.find_element(By.XPATH, '//*[@id="web-content"]/div/div/div[3]/div/div[2]/div[4]').click()
time.sleep(random.uniform(10, 18))

# 遍历所有业
# 获取一共多少页
ye_nums_str = driver.find_element(By.XPATH, '//div[@class=" search-pager"]/ul/li[last()-1]').text
ye_nums_int = int(re.findall(r'\d+', ye_nums_str)[0])

print("本次爬取一共:" + str(ye_nums_int) + "页")

# 记录正在爬取的公司数量
com_nums = 1
for i in range(start_page, ye_nums_int + 1):  # 哪里报错就从那一页重新抓  29 - 230--197
    # 刷新一下网页，查看账号登录状态，如果未登录，休息五分钟后登录
    driver.refresh()
    # 证书翻页以前判断右上角登录状态，如果是未登录，休息十分钟后登录
    # isLogin = driver.find_element(By.XPATH, '//*[@id="page-header"]/div/div[3]/div/div[5]').text
    # if isLogin.strip() == '登录/注册':
    #     time.sleep(random.uniform(500, 1000))
    #     login()

    # 获取当前时间
    print("当前系统时间为：" + str(time.asctime()))
    print("正在爬取第" + str(i) + "页")

    # 页码输入
    ye_input = driver.find_element(By.XPATH, '//div[@id="customize"]/input[1]')
    ye_input.clear()
    ye_input.send_keys(i)
    driver.find_element(By.XPATH, '//div[@class="customize"]/div').click()
    time.sleep(1)

    # 遍历该页的所有公司
    for i in range(1, 21):
        # 存放每个公司的信息
        item = []
        time.sleep(random.uniform(2, 3))
        try:
            com_name_link = driver.find_element(By.XPATH, '//div[@class="search-item sv-search-company"]' + '[' + str(
                i) + ']' + '/div/div[3]/div/a')
            # com_name_link = driver.find_element(By.XPATH, '//div[@class="search-item sv-search-company"]' + '[' + str(
            #     3) + ']' + '/div/div[3]/div/a')
        except:
            print("遍历完毕或者其它错误")
        # time.sleep(random.uniform(1, 2))

        # com_name_link.click()
        driver.execute_script("arguments[0].click();", com_name_link)
        # 滑动至该元素位置
        driver.execute_script("arguments[0].scrollIntoView();", com_name_link)
        ## 1. 获取当前所有的标签页的句柄构成的列表
        current_windows = driver.window_handles
        ## 2. 根据标签页句柄列表索引下标进行切换
        driver.switch_to.window(current_windows[-1])
        time.sleep(random.uniform(1, 2))

        # 1，公司名称
        # print(driver.page_source)
        try:
            com_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/h1').text
            print(com_name)
        except:
            com_name = "无"
        item.append(com_name)
        time.sleep(random.uniform(1, 2))

        # 2. 法定代表人
        try:
            com_boss = driver.find_element(By.XPATH,
                                           '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/span[2]/a[1]').text
            print(com_boss)
        except:
            com_boss = "无"
        item.append(com_boss)
        # time.sleep(random.uniform(1, 2))

        # 3，经营状态
        try:
            com_state = driver.find_element(By.XPATH,
                                            '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]').text
            print(com_state)
        except:
            com_state = "无"
        item.append(com_state)
        # time.sleep(random.uniform(1, 2))

        # 4. 成立日期
        try:
            com_est_date = driver.find_element(By.XPATH,
                                               '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[3]/td[2]').text
            print(com_est_date)
        except:
            com_est_date = "无"
        item.append(com_est_date)
        # time.sleep(random.uniform(1, 2))

        # 5.统一社会信用代码
        try:
            com_code = driver.find_element(By.XPATH,
                                           '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/span').text
            print(com_code)
        except:
            com_code = "无"
        item.append(com_code)
        # time.sleep(random.uniform(1, 2))

        # 6.注册资本
        try:
            com_reg_cap = driver.find_element(By.XPATH,
                                              '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/span[2]').text
            print(com_reg_cap)
        except:
            com_reg_cap = "无"
        item.append(com_reg_cap)
        # time.sleep(random.uniform(1, 2))

        # 7.实缴资本
        try:
            com_paid_cap = driver.find_element(By.XPATH,
                                               '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[4]/td[6]').text
            print(com_paid_cap)
        except:
            com_paid_cap = "无"
        item.append(com_paid_cap)
        # time.sleep(random.uniform(1, 2))

        # 8.工商注册号
        try:
            reg_code = driver.find_element(By.XPATH,
                                           '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[5]/td[2]/div/span').text
            print(reg_code)
        except:
            reg_code = "无"
        item.append(reg_code)
        # time.sleep(random.uniform(1, 3))

        # 9.纳税人识别号 # 同社会信用代码
        try:
            com_code_2 = driver.find_element(By.XPATH,
                                             '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[5]/td[4]/div/span').text
            print(com_code_2)
        except:
            com_code_2 = "无"
        item.append(com_code_2)
        # time.sleep(random.uniform(1, 2))

        # 10.组织结构代码
        try:
            zuzhi_code = driver.find_element(By.XPATH,
                                             '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[5]/td[6]/div/span').text
            print(zuzhi_code)
        except:
            zuzhi_code = "无"
        item.append(zuzhi_code)
        # time.sleep(random.uniform(1, 2))

        # 11.营业期限
        try:
            com_per = driver.find_element(By.XPATH,
                                          '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[6]/td[2]/span').text
            print(com_per)
        except:
            com_per = "无"
        item.append(com_per)
        # time.sleep(random.uniform(1, 2))

        # 12.纳税人资质
        try:
            tax_qua = driver.find_element(By.XPATH,
                                          '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[6]/td[4]').text
            print(tax_qua)
        except:
            tax_qua = "无"
        item.append(tax_qua)

        # 13.核准日期
        try:
            app_date = driver.find_element(By.XPATH,
                                           '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[6]/td[6]').text
            print(app_date)
        except:
            app_date = "无"

        item.append(app_date)

        # 14. 企业类型
        try:
            com_type = driver.find_element(By.XPATH,
                                           '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[7]/td[2]').text
            print(com_type)
        except:
            com_type = "无"

        item.append(com_type)

        # 15.行业
        try:
            com_ind = driver.find_element(By.XPATH,
                                          '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[7]/td[4]').text
            print(com_ind)
        except:
            com_ind = "无"

        item.append(com_ind)

        # 16. 人员规模
        try:
            com_per_nums = driver.find_element(By.XPATH,
                                               '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[7]/td[6]').text
            print(com_per_nums)
        except:
            com_per_nums = "无"

        item.append(com_per_nums)

        # 17. 参保人数
        try:
            canbao_num = driver.find_element(By.XPATH,
                                             '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[8]/td[2]').text
            print(canbao_num)
        except:
            canbao_num = "无"

        item.append(canbao_num)

        # 18. 分支结构参保人数
        try:
            bra_canbao_nums = driver.find_element(By.XPATH,
                                                  '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[9]/td[2]').text
            pattern = r'\d'
            if re.search(pattern, bra_canbao_nums):
                print(bra_canbao_nums)
            else:
                bra_canbao_nums = "无"
        except:
            bra_canbao_nums = "无"

        item.append(bra_canbao_nums)

        # 19. 登记机关
        try:
            reg_aut = driver.find_element(By.XPATH,
                                          '//*[@id="page-root"]/div[3]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[last()-1]/td[2]/div/span[1]').text
            print(reg_aut)
        except:
            reg_aut = "无"

        item.append(reg_aut)

        # 20.注册地址
        try:
            com_addr = driver.find_element(By.XPATH,
                                           '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div/span[1]').text
            print('注册地址:', com_addr)
        except:
            com_addr = "无"

        item.append([com_addr])

        # 21.电话
        try:
            phone_1 = driver.find_element(By.XPATH,
                                          '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/span[2]/span[2]').text
            print(phone_1)
        except:
            phone_1 = "无"

        item.append(phone_1)

        # 点击电话更多
        try:
            # time.sleep(random.uniform(2, 3))
            phone_more = driver.find_element(By.XPATH,
                                             '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/span[last()]')
            # 存放更多电话
            phones = []
            # 没有更多电话，则跳过
            if phone_more.text.strip()[0:2] == '更多':
                # print('**********************************')
                driver.execute_script("arguments[0].click();", phone_more)
                time.sleep(random.uniform(2, 3.5))
                # phone_2 = driver.find_element(By.XPATH,
                #                               '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div[2]').text

                # element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(
                #     (By.XPATH, '//div[@class="tyc-modal-body"]/div[1]/div[1]')))

                phone_2 = driver.find_elements(By.XPATH,
                                               '//div[@class="tyc-modal-body"]/div/div[1]')
                for i in phone_2:
                    phones.append(i.text)
                # 关闭更多电话框
                driver.find_element(By.XPATH,
                                    '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/button/span/i').click()
                print(phones)
            else:
                phones = '无'
        except:
            phones = "无"

        item.append(phones)

        # # 22. 邮箱
        # try:
        #     email_1 = driver.find_element(By.XPATH,
        #                                   '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/a').text
        #     print(email_1)
        # except:
        #     email_1 = "无"
        #
        # item.append(email_1)
        #
        # time.sleep(random.uniform(1, 3))
        #
        # try:
        #     driver.find_element(By.XPATH,
        #                         '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/span[2]').click()
        #     time.sleep(random.uniform(1, 3))
        #     email_2 = driver.find_element(By.XPATH,
        #                                   '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div[2]').text
        #     driver.find_element(By.XPATH,
        #                         '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/button/span/i').click()
        #     email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', [email_2][0])
        #     print(email_addresses)
        # except:
        #     email_addresses = "无"
        #
        # item.append(email_addresses)

        # # 23. 网址
        # try:
        #     web_link = driver.find_element(By.XPATH,
        #                                    '//*[@id="page-root"]/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/a').text
        #     print(web_link)
        # except:
        #     web_link = "无"
        #
        # item.append(web_link)

        # 经营状况
        jy_state = driver.find_element(By.XPATH, '//*[@id="JS_Layout_Nav"]/div/div/div/div/div[1]/div[5]/a')
        driver.execute_script("arguments[0].click();", jy_state)
        time.sleep(random.uniform(1, 2))

        # 有的公司没有证书，捕捉异常
        try:
            is_fanye = driver.find_element(By.XPATH, '//div[@data-dim="certificate"]/div[2]/div/div').text
            if is_fanye.strip() != '':  # 有不止一页
                print("有不止一页证书")
                all_yema = driver.find_elements(By.XPATH,
                                                '//div[@data-dim="certificate"]/div[2]/div/div/div/div/div/div[position()<last()]')
                for i in all_yema:
                    # 翻页之后必须等待出现证书名
                    element = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(
                        (By.XPATH, '//div[@data-dim="certificate"]/div[2]/div/table/tbody/tr[1]')))

                    # 证书翻页以前判断右上角登录状态，如果是未登录，休息十分钟后登录
                    # isLogin = driver.find_element(By.XPATH, '//*[@id="page-header"]/div/div[3]/div/div[5]').text
                    # if isLogin.strip() == '登录/注册':
                    #     time.sleep(random.uniform(500, 1000))
                    #     login()

                    # 第一页也会被点击，可能报错
                    i.click()
                    # 翻页前加入睡觉
                    time.sleep(random.uniform(1, 2))

                    # 24.证书类型/名称
                    cer_names = driver.find_elements(By.XPATH,
                                                     '//div[@data-dim="certificate"]/div[2]/div/table/tbody/tr/td[3]')

                    # 使用enumerate进行循环，index+1替换下面的XXX
                    for index, i in enumerate(cer_names):
                        # 存放各个证书的信息
                        zs_item = []

                        # 24.证书类型/名称（清洗后）
                        cer_name = i.text.strip()
                        print(str(index + 1), cer_name)

                        if cer_name in ['安全生产许可证', '建筑业资质证书']:
                            # 详情按钮
                            xiangqing_button = driver.find_element(By.XPATH,
                                                                   '//div[@data-dim="certificate"]/div[2]/div/table/tbody/tr[' + str(
                                                                       index + 1) + ']/td[7]/span')
                            driver.execute_script("arguments[0].click();", xiangqing_button)

                            time.sleep(random.uniform(2, 3.3))
                            # 使用等待条件替代睡觉
                            # element = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="tyc-modal-content"]/div[2]/table/tr/td[1]')))

                            # 详情页内容 遍历
                            try:
                                # 第一列
                                zs_contents = driver.find_elements(By.XPATH,
                                                                   '//div[@class="tyc-modal-content"]/div[2]/table/tr/td[1]')
                                for index, i in enumerate(zs_contents):
                                    if i.text.strip() in ['发证日期', '有效期自']:
                                        cer_date = driver.find_element(By.XPATH,
                                                                       '//div[@class="tyc-modal-content"]/div[2]/table/tr[' + str(
                                                                           index + 1) + ']/td[2]').text
                                        print(cer_date)
                                        zs_item.append(cer_name)
                                        zs_item.append(cer_date)
                                    elif i.text.strip() in ['发证有效期', '有效期至']:
                                        cer_lastdate = driver.find_element(By.XPATH,
                                                                           '//div[@class="tyc-modal-content"]/div[2]/table/tr[' + str(
                                                                               index + 1) + ']/td[2]').text
                                        print(cer_lastdate)
                                        zs_item.append(cer_lastdate)
                                    elif i.text.strip() == '资质范围':
                                        cer_service = driver.find_element(By.XPATH,
                                                                          '//div[@class="tyc-modal-content"]/div[2]/table/tr[' + str(
                                                                              index + 1) + ']/td[2]').text
                                        print(cer_service)
                                        zs_item.append(cer_service)

                            except:
                                print("详情页无内容")
                            # 遍历了一个详情页后输出内容
                            print('-', zs_item)
                            item.append(zs_item)

                            # 关闭该证书详情页
                            driver.find_element(By.XPATH,
                                                '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/button/span/i').click()
                            time.sleep(random.uniform(1, 2))

                    print("----翻页----")
            else:
                print('只有一页或者没有证书')
                # 24.证书类型/名称
                cer_names = driver.find_elements(By.XPATH,
                                                 '//div[@data-dim="certificate"]/div[2]/div/table/tbody/tr/td[3]')
                for index, i in enumerate(cer_names):
                    # 存放各个证书的信息
                    zs_item = []

                    # 24.证书类型/名称（清洗后）
                    cer_name = i.text.strip()
                    print(str(index + 1), cer_name)

                    if cer_name in ['安全生产许可证', '建筑业资质证书']:
                        # 详情按钮
                        # 详情页定位（替换XXXX）：//div[@data-dim="certificate"]/div[2]/div/table/tbody/tr[XXXXXX]/td[7]/span
                        xiangqing_button = driver.find_element(By.XPATH,
                                                               '//div[@data-dim="certificate"]/div[2]/div/table/tbody/tr[' + str(
                                                                   index + 1) + ']/td[7]/span')
                        driver.execute_script("arguments[0].click();", xiangqing_button)
                        time.sleep(random.uniform(2, 3.5))
                        # element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(
                        #     (By.XPATH, '//div[@class="tyc-modal-content"]/div[2]/table/tr/td[1]')))

                        try:
                            # 第一列
                            zs_contents = driver.find_elements(By.XPATH,
                                                               '//div[@class="tyc-modal-content"]/div[2]/table/tr/td[1]')
                            for index, i in enumerate(zs_contents):
                                if i.text.strip() in ['发证日期', '有效期自']:
                                    cer_date = driver.find_element(By.XPATH,
                                                                   '//div[@class="tyc-modal-content"]/div[2]/table/tr[' + str(
                                                                       index + 1) + ']/td[2]').text
                                    print(cer_date)
                                    zs_item.append(cer_name)
                                    zs_item.append(cer_date)
                                elif i.text.strip() in ['发证有效期', '有效期至']:
                                    cer_lastdate = driver.find_element(By.XPATH,
                                                                       '//div[@class="tyc-modal-content"]/div[2]/table/tr[' + str(
                                                                           index + 1) + ']/td[2]').text
                                    print(cer_lastdate)
                                    zs_item.append(cer_lastdate)

                                elif i.text.strip() == '资质范围':
                                    cer_service = driver.find_element(By.XPATH,
                                                                      '//div[@class="tyc-modal-content"]/div[2]/table/tr[' + str(
                                                                          index + 1) + ']/td[2]').text
                                    print(cer_service)
                                    zs_item.append(cer_service)
                        except:
                            print("详情页无内容")
                        # 遍历了一个详情页后输出内容
                        print('-', zs_item)
                        item.append(zs_item)

                        # 关闭该证书详情页
                        driver.find_element(By.XPATH,
                                            '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/button/span/i').click()
                        time.sleep(random.uniform(1, 2))

        except:
            print("证书遍历报错或者无证书")
        print('item:', item)
        # print(len(item))

        a = item[0:22]
        b = item[22:]
        if len(item) > 22:
            for i in b:
                for t in i:
                    c = item[0:22]
                    a.append(t)
                # 指定要将数据写入的 CSV 文件路径
                csv_file = file_name
                # 打开 CSV 文件，将数据写入
                with open(csv_file, mode='a+', newline='', encoding='utf-8-sig') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow(a)
                a = c
        else:
            # 指定要将数据写入的 CSV 文件路径
            csv_file = file_name
            # 打开 CSV 文件，将数据写入
            with open(csv_file, mode='a+', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(item)
        print("*****第：" + str(com_nums) + " 个公司爬取完毕*****")
        com_nums += 1

        # 最终都要关闭该公司的页面
        driver.close()
        ## 1. 获取当前所有的标签页的句柄构成的列表
        current_windows = driver.window_handles
        ## 2. 根据标签页句柄列表索引下标进行切换
        driver.switch_to.window(current_windows[-1])
