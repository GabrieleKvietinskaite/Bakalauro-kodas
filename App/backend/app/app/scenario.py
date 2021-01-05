from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, string, random
from random import randint, sample, randrange

class Automatization:
    DRIVER_PATH = 'C:\\Users\\gabkv\\Desktop\\Bakalauras\\chromedriver.exe'
    driver = webdriver.Chrome(DRIVER_PATH)
    username = ''
    email = ''
    password = ''

    def generate_random_symbols(self, types, size):
        return ( ''.join(random.choice(types) for i in range(size)))

    def generate_user_details(self):
        self.username = 'TEST' + self.generate_random_symbols(string.ascii_letters, 4) + self.generate_random_symbols(string.digits, 4)
        self.email = self.username + '@test.test'
        self.password = self.username + 'pass'

    def register(self):
        self.generate_user_details()
        self.driver.get('http://localhost:4200/register')

        username_input = self.driver.find_element_by_xpath('//input[@formcontrolname="username"]')
        email_input = self.driver.find_element_by_xpath('//input[@formcontrolname="email"]')
        password_input = self.driver.find_element_by_xpath('//input[@formcontrolname="password"]')
        confirm_password_input = self.driver.find_element_by_xpath('//input[@formcontrolname="confirmPassword"]')
        register_button = self.driver.find_element_by_class_name('register')

        username_input.send_keys(self.username)
        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        confirm_password_input.send_keys(self.password)
        register_button.click()
        time.sleep(3)

    def login(self):
        username_input = self.driver.find_element_by_xpath('//input[@formcontrolname="username"]')
        password_input = self.driver.find_element_by_xpath('//input[@formcontrolname="password"]')
        login_button = self.driver.find_element_by_class_name('login')

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button.click()
        time.sleep(3)

    def choose_role(self):
        self.driver.get('http://localhost:4200/roles')

        roles_dropdown = self.driver.find_element_by_xpath('//ng-select[@bindLabel="role"]')
        roles_dropdown.click()

        roles = self.driver.find_elements_by_class_name('ng-option')
        roles[0].click()

        save_role_button = self.driver.find_element_by_class_name('save-role')
        save_role_button.click()

        time.sleep(3)

    def choose_competences(self):
        competences_dropdown = self.driver.find_element_by_xpath('//ng-select[@bindLabel="competence"]')
        competences_dropdown.click()

        competences = self.driver.find_elements_by_class_name('ng-option')
        competences_quantity = randint(1, len(competences))
        competences_to_choose = sample(range(0, len(competences)), competences_quantity)

        for competence in competences_to_choose:
            competences = self.driver.find_elements_by_class_name('ng-option')
            competences[competence].click()
            competences_dropdown.click()

        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        
        save_competences_button = self.driver.find_element_by_class_name('save-competence')
        save_competences_button.click()

    def choose_game(self):
        time.sleep(1)
        play_button = self.driver.find_element_by_class_name('play')

        play_button.click()
        time.sleep(2)
    
    def game(self):
        while True:
            time.sleep(1)  
            answers_buttons = self.driver.find_elements_by_class_name('answer')
            answers_buttons_length = len(answers_buttons)
            if answers_buttons_length > 0:
                answers_buttons[randrange(answers_buttons_length)].click()
            else:
                self.driver.find_element_by_class_name('results').click()
                break

    def download_report(self):
        time.sleep(3)
        download_button = self.driver.find_element_by_class_name('download')
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        download_button.click()

        time.sleep(2)

aut = Automatization()
aut.register()
aut.login()
aut.choose_role()
aut.choose_competences()
aut.choose_game()
aut.game()
#aut.download_report()
#aut.driver.quit()