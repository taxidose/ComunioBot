from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import SecretKeys
import csv
from datetime import date

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)


def comunio_login():
    driver.get("https://www.comunio.de")
    try:
        cookie_accept_btn = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, """/html/body/div[1]/div/div/div/div[2]/div/button[2]""")))
        time.sleep(1.5)
        cookie_accept_btn.click()

        login_btn = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, """/html/body/grid/level[1]/div/login-page/div/level/rail[2]/lore[4]/div[2]/a[1]""")))
        time.sleep(1.72)
        login_btn.click()

        time.sleep(1.23)

        login_field_name = driver.find_element_by_xpath(
            """/html/body/grid/level[1]/div/login-page/div/login-modal/div/div[1]/form/div[1]/input""")
        login_field_name.send_keys(SecretKeys.COMUNIO_ACC_NAME)

        login_field_pw = driver.find_element_by_xpath(
            """/html/body/grid/level[1]/div/login-page/div/login-modal/div/div[1]/form/div[2]/input""")
        login_field_pw.send_keys(SecretKeys.COMUNIO_PASSWORD)
        time.sleep(0.5)

        login_field_pw.send_keys(Keys.RETURN)
        time.sleep(0.666)

    except:
        driver.quit()


# returns list of dictionaries with keys: rank, name, points, plus, networth for each player
def receive_data() -> list:
    driver.get("https://www.comunio.de/standings/total")
    # try:
    standings_tabelle = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, """//*[@id="standings"]/div/div/div[1]/div[3]/div[3]""")))
    standings_tabelle_list = standings_tabelle.text.split()
    standings_tabelle_list.insert(0, "1.")
    standings_tabelle_list.insert(5, "2.")
    standings_tabelle_list.insert(10, "3.")

    player_amt = int(len(standings_tabelle_list) / 5)

    player_data = []
    attribute_counter = 0
    for i in range(player_amt):
        player_data.append({"rank": standings_tabelle_list[attribute_counter],
                            "name": standings_tabelle_list[attribute_counter + 1],
                            "points": int(standings_tabelle_list[attribute_counter + 4]),
                            "plus": int(standings_tabelle_list[attribute_counter + 3]),
                            "networth": standings_tabelle_list[attribute_counter + 2]})
        attribute_counter += 5
    driver.quit()
    return player_data

# latest.csv for reading in data and <date>.csv for history
def write_csv(input_data):
    file_name = date.today().strftime("%d_%m_%Y") + ".csv"
    latest_file = "latest.csv"
    csv_columns = ["rank", "name", "points", "plus", "networth"]
    try:
        with open(file_name, "w") as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for data in input_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    try:
        with open(latest_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for data in input_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")





