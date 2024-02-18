from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def close_cookies_popup(self):
      try:
        cookies_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "wt-cli-accept-all-btn")))
        cookies_popup.click()

      except:
        pass  # Uyarı yoksa geç
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"


    def go_to_company_menu(self):
        company_menu = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Company')]")
        company_menu.click()

class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/careers/"

class CareersQAPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url ="https://useinsider.com/careers/quality-assurance/"



    def click_see_all_qa_jobs(self):
        self.close_cookies_popup()
        see_all_qa_jobs_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")))
        self.driver.execute_script("arguments[0].click();", see_all_qa_jobs_button)

    def filter_jobs(self, location, department):
        self.close_cookies_popup()  # Çerez uyarısını kapat
        location_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-filter-by-location-container']")))
        location_dropdown.click()

        location_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[text()='{location}']")))
        location_option.click()

        department_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='select2-filter-by-department-container']")))
        department_dropdown.click()

        department_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[text()='{department}']")))
        department_option.click()


    def are_jobs_displayed(self):
         try:
             WebDriverWait(self.driver, 10).until(
                 EC.visibility_of_element_located((By.XPATH, "//*[@id='jobs-list']/div[1]/div/a")))
             return True
         except:
             return False


driver = webdriver.Chrome()

home_page = HomePage(driver)
home_page.driver.get(home_page.url)
home_page.go_to_company_menu()

careers_page = CareersPage(driver)
careers_page.driver.get(careers_page.url)

careers_pageQA = CareersQAPage(driver)
careers_pageQA.driver.get(careers_pageQA.url)
careers_pageQA.click_see_all_qa_jobs()
careers_pageQA.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")
careers_pageQA.are_jobs_displayed()


assert careers_pageQA.are_jobs_displayed(), "Job list is not displayed"

driver.quit()

