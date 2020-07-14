from selenium import webdriver


class Locators:
    def test(self):
        baseUrl = "https://www.irctc.co.in/nget/train-search"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        elementByclassname = driver.find_element_by_class_name("")
        if elementByclassname is not None:
            print("we found element by Class Name")
        else:
            print("not a valid Class Name and throws an Exception unable to locate element")

        elementBytagname = driver.find_element_by_tag_name("")
        if elementBytagname is not None:
            print("we found element by Tag Name")
        else:
            print("Not an valid Tag Name and throws an Exception unable to locate element")

        elementById = driver.find_element_by_id("userName")
        if elementById is not None:
            print("we found element by Id")
        else:
            print("not a valid Id and throws an Exception unable to locate element")

        elementByName = driver.find_element_by_name("userName")
        if elementByName is not None:
            print("we found element by Name")
        else:
            print("not a valid Name and throws an Exception unable to locate element")

        driver.quit()


locators = Locators()
locators.test()
