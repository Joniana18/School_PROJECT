from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all_jobs_selenium(base_url, site_type, start_page=1):
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    all_jobs = []

    try:
        if site_type == "duapune":
            driver.get(base_url)
            time.sleep(5)  # Allow time for the page to load

            job_elements = driver.find_elements(By.CSS_SELECTOR, "div.job-listing.col-md-12.premiumBlockv2.simple-listing")
            print(f"Found {len(job_elements)} job listings")

            for job_element in job_elements:
                try:
                    title = job_element.find_element(By.CSS_SELECTOR, "h1.job-title a").text.strip()
                    company = job_element.find_element(By.CSS_SELECTOR, "small a").text.strip()
                    location = job_element.find_element(By.CSS_SELECTOR, "span.location").text.strip()
                    expire = job_element.find_element(By.CSS_SELECTOR, "span.expire").text.strip()

                    job_data = {
                        "Title": title,
                        "Company": company,
                        "Location": location,
                        "Expire": expire
                    }
                    all_jobs.append(job_data)

                except Exception as e:
                    print(f"Error extracting job: {e}")
                    continue

        elif site_type == "punajuaj":
            page = start_page
            while True:
                url = f"{base_url}/page/{page}/"
                driver.get(url)
                time.sleep(5)

                # Scroll to ensure JavaScript loads jobs
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)

                print(f"Loaded page: {url}")
                print(driver.page_source[:1000])  # Debugging: First 1000 characters of the page source

                job_elements = driver.find_elements(By.CSS_SELECTOR, "div.loop-item-content")
                print(f"Page {page}: Found {len(job_elements)} jobs") 

                if not job_elements:
                    print("No job elements found, stopping...")
                    break  

                for job_element in job_elements:
                    try:
                        title = job_element.find_element(By.CSS_SELECTOR, "h3.loop-item-title a").text.strip()
                        company = job_element.find_element(By.CSS_SELECTOR, "span.job-company").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-company") else "No company found"
                        job_type = job_element.find_element(By.CSS_SELECTOR, "span.job-type").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-type") else "No job type"
                        location = job_element.find_element(By.CSS_SELECTOR, "span.job-location").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-location") else "No location found"
                        category = job_element.find_element(By.CSS_SELECTOR, "span.job-category").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-category") else "No category"
                        language = job_element.find_element(By.CSS_SELECTOR, "span.job-language").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-language") else "No language"

                        job_data = {
                            "Title": title,
                            "Company": company,
                            "Job Type": job_type,
                            "Location": location,
                            "Category": category,
                            "Language": language
                        }

                        all_jobs.append(job_data)
                    except Exception as e:
                        print(f"Error extracting job: {e}")
                        continue

                # Check for "Next" button
                next_button = driver.find_elements(By.CSS_SELECTOR, "a.next.page-numbers")
                if not next_button:
                    print("No next button found, stopping...")
                    break  

                page += 1
    
    finally:
        driver.quit()

    return pd.DataFrame(all_jobs)

# Example Usage
base_url = "https://duapune.com/search/advanced/filter?page=1"
df = scrape_all_jobs_selenium(base_url, "duapune")
print(df)from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all_jobs_selenium(base_url, site_type, start_page=1):
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    all_jobs = []

    try:
        if site_type == "duapune":
            driver.get(base_url)
            time.sleep(5)  # Allow time for the page to load

            job_elements = driver.find_elements(By.CSS_SELECTOR, "div.job-listing.col-md-12.premiumBlockv2.simple-listing")
            print(f"Found {len(job_elements)} job listings")

            for job_element in job_elements:
                try:
                    title = job_element.find_element(By.CSS_SELECTOR, "h1.job-title a").text.strip()
                    company = job_element.find_element(By.CSS_SELECTOR, "small a").text.strip()
                    location = job_element.find_element(By.CSS_SELECTOR, "span.location").text.strip()
                    expire = job_element.find_element(By.CSS_SELECTOR, "span.expire").text.strip()

                    job_data = {
                        "Title": title,
                        "Company": company,
                        "Location": location,
                        "Expire": expire
                    }
                    all_jobs.append(job_data)

                except Exception as e:
                    print(f"Error extracting job: {e}")
                    continue

        elif site_type == "punajuaj":
            page = start_page
            while True:
                url = f"{base_url}/page/{page}/"
                driver.get(url)
                time.sleep(5)

                # Scroll to ensure JavaScript loads jobs
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)

                print(f"Loaded page: {url}")
                print(driver.page_source[:1000])  # Debugging: First 1000 characters of the page source

                job_elements = driver.find_elements(By.CSS_SELECTOR, "div.loop-item-content")
                print(f"Page {page}: Found {len(job_elements)} jobs") 

                if not job_elements:
                    print("No job elements found, stopping...")
                    break  

                for job_element in job_elements:
                    try:
                        title = job_element.find_element(By.CSS_SELECTOR, "h3.loop-item-title a").text.strip()
                        company = job_element.find_element(By.CSS_SELECTOR, "span.job-company").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-company") else "No company found"
                        job_type = job_element.find_element(By.CSS_SELECTOR, "span.job-type").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-type") else "No job type"
                        location = job_element.find_element(By.CSS_SELECTOR, "span.job-location").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-location") else "No location found"
                        category = job_element.find_element(By.CSS_SELECTOR, "span.job-category").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-category") else "No category"
                        language = job_element.find_element(By.CSS_SELECTOR, "span.job-language").text.strip() if job_element.find_elements(By.CSS_SELECTOR, "span.job-language") else "No language"

                        job_data = {
                            "Title": title,
                            "Company": company,
                            "Job Type": job_type,
                            "Location": location,
                            "Category": category,
                            "Language": language
                        }

                        all_jobs.append(job_data)
                    except Exception as e:
                        print(f"Error extracting job: {e}")
                        continue

                # Check for "Next" button
                next_button = driver.find_elements(By.CSS_SELECTOR, "a.next.page-numbers")
                if not next_button:
                    print("No next button found, stopping...")
                    break  

                page += 1
    
    finally:
        driver.quit()

    return pd.DataFrame(all_jobs)

# Example Usage
base_url = "https://duapune.com/search/advanced/filter?page=1"
df = scrape_all_jobs_selenium(base_url, "duapune")
print(df)
