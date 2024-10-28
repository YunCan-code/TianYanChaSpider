# TianYanChaSpider

代码已经失效，推荐使用接口进行爬取

> 利用 Python selenium 对天眼查进行爬虫
> 帮同事写的，要求不高，出数据就行

### 1.目标数据

- 详情页的公司数据
- 公司的资质证书(安全生产和建筑建筑业资质证书)的证书有效期其范围

### 2.运行环境

- Python 3.8
- Selenium 4.17.2

### 3.待完成

- 代码重构
- 效率提升(目前一天一万条左右)
- 极验证码自动识别
- 自动对筛选条件数据量进行切割

### 4.其它说明

- 使用时填写账号密码(淘宝)，数据保存的文件名
- 登录时手动点验证码
- 由于天眼查数据最多显示 250 页，即 5000 条公司信息，所以需要提前做好条件切割。eg：
  - 爬取南京建筑业的所有公司信息，共 10W+条数据
  - 选择建筑业-房屋建筑业；选择江苏-南京-玄武区和秦淮区
  - 此时数据为 3677 条
  - 通过分批次爬取即可获得所有数据
