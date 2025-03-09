from email.mime import image
from enum import Enum
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import base64
import time

class ArtStyles(Enum):
    NO_STYLE ='(No style)'
    CINEMATIC ='Cinematic'
    PHOTOGRAPHIC ='Photographic'
    ANIME ='Anime'
    MANGA ='Manga'
    DIGITAL_ART ='Digital Art'
    PIXEL_ART ='Pixel art'
    FANTASY_ART ='Fantasy art'
    NEOPUNK ='Neonpunk'
    
class ImageScraper:
    def __init__(self):
        """
        Initialize the ImageScraper with Selenium WebDriver.
        """
        # Initialize the Chrome WebDriver (headless)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--window-size=%s" % "100, 100")
        options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems in Docker environments
        options.add_argument('--disable-infobars')  # Disable infobars, "Chrome is being controlled by automated software"

        self.driver = webdriver.Chrome(options=options)

    def wait_for_element(self, by_method, selector, timeout=20):
        """
        Helper function to wait for an element to appear.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by_method, selector))
            )
            return element
        except TimeoutException:
            print(f"Error: Element with selector '{selector}' not found within {timeout} seconds.")
            return None

    def get_shadow_root(self, element):
        """
        Helper function to access the shadow root of a web component.
        """
        return self.driver.execute_script('return arguments[0].shadowRoot', element)

    def wait_for_elements(self, by, value, timeout=10):
        """
        Wait for multiple elements to be present in the DOM.
        
        :param by: The method to locate elements (e.g., By.CSS_SELECTOR).
        :param value: The selector to use for locating elements.
        :param timeout: How long to wait before timing out (default is 10 seconds).
        :return: A list of WebElements if found, otherwise an empty list.
        """
        end_time = time.time() + timeout
        elements = []

        while time.time() < end_time:
            try:
                elements = self.driver.find_elements(by, value)
                if elements:  # Check if any elements are found
                    return elements
            except Exception as e:
                print(f"Waiting for elements... {str(e)}")
                time.sleep(0.5)  # Wait a bit before trying again

        print(f"Timeout: Could not find elements with {by}='{value}' after {timeout} seconds.")
        return elements  # Return an empty list if no elements found


    def get_images(self,prompt, url="https://stable-diffusion-web.com/sdxl", neg_prompt='deformed, low resolution', artStyle:ArtStyles=ArtStyles.NO_STYLE, guidance = 7):
        """
        Scrape images from the given URL after interacting with a form by
        entering input_value into an input field and submitting the form.
        """
         # Navigate to the provided URL
        self.driver.get(url)

        iframe = self.wait_for_element(By.TAG_NAME, "iframe", 50)  # You might need a more specific element       
        self.driver.switch_to.frame(iframe)


        input_field = self.wait_for_element(By.CSS_SELECTOR, "#prompt-text-input input")
        
        # if neg_prompt:
        #     input_neg_prompt = self.wait_for_element(By.CSS_SELECTOR, "#negative-prompt-text-input input")
        #     if input_neg_prompt:
        #         input_neg_prompt.send_keys(neg_prompt)

        if artStyle:
            radio_buttons = self.wait_for_elements(By.CSS_SELECTOR, '#component-12 input[type="radio"]')
            for radio_button in radio_buttons:
                # Check the value of the radio button
                if radio_button.get_attribute("value") == artStyle:  # Replace "desired_value" with the actual value
                    radio_button.click()  # Click to select the radio button
                break  # Stop a

        # if guidance and guidance >=0 and guidance <=50:
        #     guidanceSlider = self.wait_for_element(By.CSS_SELECTOR, "#range_id_0")
        #     if guidanceSlider:
        #         guidanceSlider.send_keys(guidance)

        

        submit_button = self.wait_for_element(By.ID, "gen-button")
        

        if not submit_button or not input_field:
            print("Error: Could not find the input or btn element.")
            return []


        # Send the desired input value to the input field
        input_field.send_keys(prompt)
        # Find the submit button (adjust the selector if necessary)
        submit_button.click()

        # Wait for the images to load or images to appear
        thumbnail_buttons = self.wait_for_elements(By.CSS_SELECTOR, "button.thumbnail-item", timeout=60)

        if not thumbnail_buttons:
            print("Error: No thumbnail buttons were found.")
            return []

        # Scrape the images
        # thumbnail_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.thumbnail-item")
        images = []
        
        for button in thumbnail_buttons:
            img_tag = button.find_element(By.TAG_NAME, "img")
            img_src = img_tag.get_attribute("src") or img_tag.get_attribute("data-src")
            
            if img_src and img_src.startswith("data:image/jpeg;base64,"):
                # Extract the base64 part from the src
                base64_data = img_src.split(",")[1]
                # Decode the base64 data
                image_bytes = base64.b64decode(base64_data)
                # Append image bytes for later display
                images.append(image_bytes)
        
        self.driver.switch_to.default_content()

        return images
    
    def close(self):
        """
        Close the Selenium WebDriver.
        """
        self.driver.quit()
