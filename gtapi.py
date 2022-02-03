from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.support import expected_conditions as EC

import string

class Translator:

    # DO NOT CHANGE THEM - CONSTANTS
    AFRIKAANS = 'af'
    ALBANIAN = 'sq'
    AMHARIC = 'am'
    ARABIC = 'ar'
    ARMENIAN = 'hy'
    AZERBAIJANI = 'az'
    BASQUE = 'eu'
    BELARUSIAN = 'be'
    BENGALI = 'bn'
    BOSNIAN = 'bs'
    BULGARIAN = 'bg'
    CATALAN = 'ca'
    CEBUANO = 'ceb'
    CHICHEWA = 'ny'
    CHINESE = 'zh-CN'
    CORSICAN = 'co'
    CROATIAN = 'hr'
    CZECH = 'cs'
    DANISH = 'da'
    DUTCH = 'nl'
    ENGLISH = 'en'
    ESPERANTO = 'eo'
    ESTONIAN = 'et'
    FILIPINO = 'tl'
    FINNISH = 'fi'
    FRENCH = 'fr'
    FRISIAN = 'fy'
    GALICIAN = 'gl'
    GEORGIAN = 'ka'
    GERMAN = 'de'
    GREEK = 'el'
    GUJARATI = 'gu'
    HAITIAN_CREOLE = 'ht'
    HAUSA = 'ha'
    HAWAIIAN = 'haw'
    HEBREW = 'iw'
    HINDI = 'hi'
    HMONG = 'hmn'
    HUNGARIAN = 'hu'
    ICELANDIC = 'is'
    IGBO = 'ig'
    INDONESIAN = 'id'
    IRISH = 'ga'
    ITALIAN = 'it'
    JAPANESE = 'ja'
    KANNADA = 'kn'
    KAZAKH = 'kk'
    KHMER = 'km'
    KINYARWANDA = 'rw'
    KOREAN = 'ko'
    KURDISH = 'ku'
    KYRGYZ = 'ky'
    LAO = 'lo'
    LATIN = 'la'
    LATVIAN = 'lv'
    LITHUANIAN = 'lt'
    LUXEMBOURGISH = 'lb'
    MACEDONIAN = 'mk'
    MALAGASY = 'mg'
    MALAY = 'ms'
    MALAYALAM = 'ml'
    MALTESE = 'mt'
    MAORI = 'mi'
    MARATHI = 'mr'
    MONGOLIAN = 'mn'
    MYANMAR = 'my'
    NEPALI = 'ne'
    NORWEGIAN = 'no'
    ODIA = 'or'
    PASHTO = 'ps'
    PERSIAN = 'fa'
    POLISH = 'pl'
    PORTUGUESE = 'pt'
    PUNJABI = 'pa'
    ROMANIAN = 'ro'
    RUSSIAN = 'ru'
    SAMOAN = 'sm'
    SCOTS_GALICIAN = 'gl'
    SERBIAN = 'sr'
    SESOTHO = 'st'
    SHONA = 'so'
    SINDHI = 'sd'
    SINHALA = 'si'
    SLOVAK = 'sk'
    SLOVENIAN = 'sl'
    SOMALI = 'so'
    SPANISH = 'es'
    SUNDANESE = 'su'
    SWAHILI = 'sw'
    SWEDISH = 'sv'
    TAJIK = 'tg'
    TAMIL = 'ta'
    TATAR = 'tt'
    TELUGU = 'te'
    THAI = 'th'
    TURKISH = 'tr'
    TURKMEN = 'tk'
    UKRAINIAN = 'uk'
    URDU = 'ur'
    UYGHUR = 'ug'
    UZBEK = 'uz'
    VIETNAMESE = 'vi'
    WELSH = 'cy'
    XHOSA = 'xh'
    YIDDISH = 'yi'
    YORUBA = 'yo'
    ZULU = 'zu'
    AUTO = 'auto'

    def __init__(self):
        # Setting up a headless browser.
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    def __run_google_translate__(self, sentence, from_language, to_language):
        url = 'https://translate.google.com/?sl={0}&tl={1}&text={2}&op=translate'.format(from_language, to_language, sentence)

        # Wait for the browser to be ready
        self.browser.implicitly_wait(10)

        # Open up the URL
        self.browser.get(url)

    def translate(self, sentence, from_language = AUTO, to_language = ENGLISH):
        self.__run_google_translate__(sentence, from_language, to_language)

        response = None
        try:
            response = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span'))).text

        except JavascriptException:
            print('JavascriptException')

        except:
            print('Error')

        # self.browser.close()

        # Convert the result to string.        
        if response != None:
            return str(response)

        return None

    def detect_language(self, sentence):
        self.__run_google_translate__(sentence, 'auto', 'en')

        response = None
        try:
            response = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[2]/div/div[2]/div/div/span/button[1]/span[1]/span'))).text

            # The response will store something like 'ENGLISH - DETECTED', we want to get only the language.
            response = response.split('-')[0]
            response = response[0: -1] 

            # Only first character uppercased.
            response = string.capwords(response)

        except JavascriptException:
            print('JavascriptException')

        except:
            print('Error')

        # self.browser.close()

        if response != None:
            return str(response)

        return None
    
