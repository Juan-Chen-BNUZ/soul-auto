from selenium import webdriver
import time
import random

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(executable_path="chromedriver.exe")
wd.get('https://chat.soulapp.cn/')

# 扫描二维码的时间
time.sleep(20)

# 点击第一个联系人
wd.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[3]/div/div[1]').click()

# 获取输入框
SendBox = wd.find_element_by_xpath('//*[@id="input"]')

# 循环输入，并发送
for i in range(0,150000):
    # 记录循环时间
    begin = time.time()
    SendBox.send_keys(random.choice(['我不能给你全世界，但是，我的全世界全都给你',
                              '春风十里不如你，愿有岁月可回首，且以深情共白头',
                              '我曾做过最好的事就是对你一如既往的坚持',
                              '有的人说不清哪里好，但就是谁都替代不了',
                              '不是我执着，而是你值得',
                              '其实你不喜欢我，我也不会死，但是如果你肯喜欢我，我一定会非常非常勇敢地活下去',
                              '每个人心中都有一团火， 路过的人只能看到烟。 但是总有一个人， 总有那么一个人能看到这火， 然后走过来陪我一起',
                              '没遇见你之前，我没想过结婚这事，遇见你之后，结婚这事我没想过别人',
                              '有人问我你究竟哪里好，这么多年我还忘不了，春风再美也比不上你的笑，没见过你的人不会明了',
                              '我还在努力，你先不要喜欢其他人',
                              '和你在一起的时刻都很美好，因为天气好，因为天气不好，因为天气刚刚好',
                              '当有人说到幸福二字时，我满脑子都是我们',
                              '一想到你，我对整个世界都很温柔',
                              '我爱你没变，变的是我更爱你了',
                              '你一声不离，换我余生不弃',
                              '我想要的很简单，时光还在，你还在',
                              '你永远也看不到我最寂寞时候的样子，因为只有你不在我身边的时候，我才最寂寞',
                              '有那么多事情我无能为力，比如生老病死，比如时光流逝，比如我爱你',
                              '林深时见鹿，海蓝时见鲸，梦醒时见你',
                              '未经允许，擅自喜欢你，特别不好意思']))
    wd.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[3]/div[3]/div').click()
    # 记录时间
    Tic = time.time()
    # 设置延迟时间防检测
    time.sleep(random.uniform(3,5))
    # 记录时间
    Toc = time.time()
    # 总时间
    Time = Toc - Tic

    # 循环结束
    end = time.time()

    print("成功发送第 %d 条消息，休眠时差%f秒，总时间%f秒"%(i+1,Time,end-begin))




