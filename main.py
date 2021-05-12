from selenium import webdriver
import smtplib, ssl

port = 465  # For SSL

password = ""


driver = webdriver.Chrome()

def alert_user():


    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        send_email = "airsoftandminecraft5@gmail.com"
        recv_email = "kevin.rhoades128@gmail.com"
        server.login("airsoftandminecraft5@gmail.com", password)
        server.sendmail(send_email, recv_email, "hi:)")

def check_page():
    while True:
        try:
            driver.get ("https://www.patreon.com/bsjgaming")
            butt = driver.find_element_by_xpath("//*[@id=\"renderPageContentWrapper\"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/button")
            butt.click()

            content = driver.find_element_by_xpath("//*[@id=\"renderPageContentWrapper\"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[3]/div/div/div/div/div[3]/div/a")
            att = content.get_attribute("aria-label")
            print(att)
            if att != "Hard Carry Players Sold Out":
                alert_user()
        except:
            print("yup")
            alert_user()
            break


if __name__ == "__main__":
    password = input("Type your password and press enter: ")
    check_page()


