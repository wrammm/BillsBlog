import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


class Blog_ATS(unittest.TestCase):

    #use Chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome()

    #preform test
    def test_blog(self):
        #get csv data
        with open('blogPosts.csv') as file:
            reader = csv.reader(file)
            line = 0
            titles = []
            authors = []
            bodies = []
            statuses = []
            for row in reader:
                if(line > 0):
                    titles.append(row[0])
                    authors.append(row[1])
                    bodies.append(row[2])
                    statuses.append(row[3])
                line = line + 1
        #log in credentials
        user = "wramm@unomaha.edu"
        pwd = "forSecurityPurposesThisIsNotTheRealPassword"
        driver = self.driver
        #maximize window
        driver.maximize_window()
        #go to admin site
        driver.get("https://billsblogg.herokuapp.com/admin/")
        #enter log in credentials
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Logged In"
        #for every post, add post to blog
        for i in range(len(titles)):
            driver.get("https://billsblogg.herokuapp.com/admin/")
            # pause screen for 1 second
            time.sleep(1)
            #click posts link
            elem = driver.find_element_by_xpath("""//*[@id="content-main"]/div[2]/table/tbody/tr/th/a""").click()
            time.sleep(1)
            #click add post button
            elem = driver.find_element_by_xpath("""//*[@id="content-main"]/ul/li/a""").click()
            time.sleep(1)
            # enter title
            elem = driver.find_element_by_id("id_title")
            elem.send_keys(titles[i])
            time.sleep(1)
            # enter author
            elem = driver.find_element_by_id("id_author")
            elem.send_keys(authors[i])
            time.sleep(1)
            #enter body
            elem = driver.find_element_by_id("id_body")
            elem.send_keys(bodies[i])
            time.sleep(1)
            #choose 'published'status from select box
            elem = driver.find_element_by_id('id_status')
            for option in elem.find_elements_by_tag_name('option'):
                if option.text == statuses[i]:
                    option.click()  # select() in earlier versions of webdriver
                    break
            #click save button
            elem = driver.find_element_by_xpath("""//*[@id="post_form"]/div/div/input[1]""").click()
            time.sleep(1)
            assert "Posted Blog Entry"
            #go to blog to see new post
            driver.get("https://billsblogg.herokuapp.com/")
            time.sleep(2)

    #close test
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()