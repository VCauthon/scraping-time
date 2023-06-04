# Scrapy settings for fotocasa project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "fotocasa"

SPIDER_MODULES = ["fotocasa.spiders"]
NEWSPIDER_MODULE = "fotocasa.spiders"


# Crawl responsibly by identifying yourself on the user-agent
# USER_AGENT = [  # I look like a google bot
#     "Mozilla/5.0 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)",
#     "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +https://www.google.com/bot.html) Safari/537.36"
#     ]

USER_AGENT = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.1.2;FBSS/2;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0]",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/3;FBCR/TELIA;FBID/phone;FBLC/sv_SE;FBOP/5;FBRV/0]",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G950F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/157.0.0.21.89;]",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B670460233A118780T1390849P1) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B674046446A102175T1297416P2) like Gecko",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; HPDTDFJS; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/170.1.0.80.91;FBBV/106613464;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0;FBIA/FBIOS]",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; Touch; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; Tablet PC 2.0; McAfee; wbx 1.0.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B668757220A77460T1390849P1) like Gecko",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-P605 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-J701F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/166.0.0.26.91;]",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/CCC080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/FBIOS;FBAV/163.0.0.54.96;FBBV/96876057;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/O2;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/96876057]",
    "Mozilla/5.0 (Linux; Android 7.0; F3212 Build/36.1.A.1.86; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36",    "Mozilla/5.0 (Linux; Android 7.1.2; HP Pavilion Notebook Build/NJH47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 [FBAN/FBIOS;FBAV/180.0.0.37.85;FBBV/116915501;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3.1;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/117772964]",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; GWX:DOWNLOADED; GTB7.5)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; BCP 1.2 GPO; Microsoft Outlook 16.0.9029; Microsoft Outlook 16.0.9029; ms-office; MSOffice 16)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2146.80 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0]",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G9650 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G570F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B674128930A90240T1297416P2) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B669643702A102175T1297416P2) like Gecko",
    "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G950N/KSU1AQL3 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/101718514]",
    "Mozilla/5.0 (Linux; Android 5.1; STARTRAIL7 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/163.0.0.43.91;]",
    "Mozilla/5.0 (Linux; Android 7.1.1; Moto G Play Build/NPI26.48-36; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/162.0.0.45.94;]",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2781.45 Safari/537.36",
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'User-Agent': "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) '
#                  'Chrome/58.0.3029.110 Safari/537.3'"
# }

# LOG_STDOUT = False
# LOG_ENABLED = True
# LOG_LEVEL = 'DEBUG'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "fotocasa.middlewares.FotocasaSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# Enable splash to render javascript
# SPLASH_URL = 'http://localhost:8050' 
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# Enable user agents set manually from settings
DOWNLOADER_MIDDLEWARES = {
    "fotocasa.middlewares.FotocasaDownloaderMiddleware": 543,
    # "scrapy_splash.SplashCookiesMiddleware": 723,  # Splash
    # "scrapy_splash.SplashMiddleware": 725,  # Splash
    # "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,  # Splash
}

# Enable or disable user agents set by scrapy-user-agents
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "fotocasa.pipelines.FotocasaPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#          #httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
