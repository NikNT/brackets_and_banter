import time
import pyperclip  # Used to read copied text from clipboard
from playwright.sync_api import sync_playwright

# ---- CONFIGURATION ----
TEMP_MAIL_URL = "https://temp-mail.org/en/"

def get_temp_email(page):
    """Fetches a temporary email by clicking the 'Copy to Clipboard' button using its class."""
    page.goto(TEMP_MAIL_URL)
    time.sleep(10)  # Wait for the email to load

    # Click the "Copy to Clipboard" button using the class selector
    page.click(".copyIconGreenBtn")  # Selecting by class name
    time.sleep(2)  # Wait for clipboard update

    # Get the copied email from clipboard
    temp_email = pyperclip.paste()
    
    if temp_email:
        print(f"[+] Copied Temp Email: {temp_email}")
        return temp_email
    else:
        print("[!] Failed to copy email.")
        return None

# ---- RUN THE SCRIPT ----
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set to True for background execution
    page = browser.new_page()

    temp_email = get_temp_email(page)

    print("[*] Process completed. Press Enter to exit...")
    input()
    
    browser.close()
