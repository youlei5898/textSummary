# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PyWebdriver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://textsummary.herokuapp.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_py_webdriver(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(u"10月20日，国家主席习近平在伦敦白金汉宫出席英国女王伊利莎白二世举行的欢迎晚宴。新华社记者 鞠鹏 摄")
        driver.find_element_by_xpath("//textarea[2]").clear()
        driver.find_element_by_xpath("//textarea[2]").send_keys(u"国际在线专稿：中国国家主席习近平携夫人彭丽媛正在英国进行国事访问，由于这是中国国家元首十年来首次对英国进行国事访问，英国媒体对习近平夫妇的关注和讨论热度不断升温。不少媒体都在试图还原二人的生平，而他们的个人魅力也给英国媒体留下了深刻印象。\n\n　　英国广播公司：习近平是中国人民的领导人，经常深入基层，体察民情。他用平实的话语告诫大学生，青年时期树立价值观非常重要，这就像穿衣服扣扣子一样，如果第一粒扣子扣错了，剩余的扣子都会扣错。所以，人生的扣子从一开始就要扣好。他曾在小餐馆排队买饭，不仅自己支付饭费，还跟民众一起用餐。他曾经不戴口罩深入棚户区视察，这让外界觉得普通人能够忍受的环境他也能忍受。总之，他不想让民众觉得自己遥不可及。\n\n　　《每日快报》：习近平夫妇二人早期的成长历程都充满了艰辛。习近平早在青少年时代就离开在北京的父母，前往偏远的山区接受贫下中农的“再教育”。他推小车，建大坝，每天的粮食配给量很低，还要睡在“稻草铺成的床上”，但“逆境中的一切都有助于他日后性格的形成”。而彭丽媛年少时也经历过波折，但她最后却成为一名解放军少将。\n\n　　文章进一步指出，习近平夫妇打破了西方对中国领导人夫妇的刻板印象。首先，二者非常亲民，因此更为人们所了解。习近平经常深入基层，走到人民群众中间，甚至到普通的小吃店享用简单的午餐。在爱尔兰，习近平曾一展球技，足球在他的脚上上下翻飞。彭丽媛则一改以往中国领导人夫人默默无闻的形象，大方地在各种外交场合“助夫君一臂之力”。她已成为国际舞台上的一位明星：她是世界卫生组织“抗击结核病和艾滋病”亲善大使，是联合国教科文组织“促进女童和妇女教育特使”，还是中国控烟形象大使。\n\n　　其次，习近平夫妇在形象上非常现代、与时俱进。习近平在公开场合总是穿着笔挺的西装，而她的夫人彭丽媛仪态举止典雅端庄，两人给中国赋予了崭新的形象。这或许意味着“在中国的政治层面上，二人也会带来全新的变化”。\n\n　　《每日邮报》：中国“第一夫人”彭丽媛访问英国首日连换三套服装，“惊艳全场”。在参加女王的欢迎仪式时，彭丽媛身穿白色裙子套装，搭配叶子形状的胸针，简洁大方，高贵典雅。20日下午，当习近平在英国议会发表演讲时，彭丽媛身穿深灰印花长衣外套，并搭配了一条浅灰丝巾。而当晚上的国宴开始时，彭丽媛换上了中长袖的深蓝色长裙晚礼服，腰间配了一条白色的腰带，再搭配白色珍珠耳钉和白色手包，气场十足。\n\n　　报道还介绍了彭丽媛的背景，称她由于是歌唱家出身，所以习惯于暴露在镁光灯下，并时常“为过于严肃的政治舞台带来一抹亮色”。由于出生于盛产牡丹的中国山东菏泽市，彭丽媛出道时曾被称为“牡丹仙子”。凭借出色的嗓音与刻苦的努力，在23岁时，她就成为了中国家喻户晓的歌唱明星。\n\n　　《每日电讯报》：作为中国的“第一夫人”，彭丽媛以她的迷人气质和优雅魅力征服了海内外。她致力于在各种场合推广中国文化，也积极投身于抗击艾滋病等公益事业。上个月习近平对美国进行国事访问期间，彭丽媛访问了茱莉亚学院，并亲自向学生们示范了民族唱法。去年3月，她陪同美国第一夫人米歇尔·奥巴马及其母亲和两个女儿参观了故宫。当年夏天，她又邀请前来参加南京青奥会的外国首脑夫人体验苏州刺绣。她在用自身的行动传播中国文化，人们从她的着装和思想上也能感受到中国文化的魅力。\n\n　　《镜报》：在国际舞台上，彭丽媛所享有的声望绝不逊于英国的凯特王妃，但是很多英国人并不熟悉彭丽媛的生平。这位中国的“第一夫人”是一位在逆境中冉冉升起的明星。虽然年少时经历过一些波折，但由于在歌唱方面天资聪颖，加上勤奋刻苦，她在艺术之路上取得了巨大的成功。1983年，彭丽媛凭借在春晚上演唱的歌曲一炮走红，开始为广大观众所熟知。1986年，她经朋友介绍与习近平相识。一年后，二人便结了婚。\n\n　　2013年习近平当选国家主席，彭丽媛的角色发生了变化。她开始淡出舞台，转而将重心放在公益活动上。她是多个国际组织的“大使”、“公使”，还成为了中国女性的“时尚代表”。她在2015年《福布斯》杂志评选的“全球最")
        driver.find_element_by_id("getSummary").click()

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
