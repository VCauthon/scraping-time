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
USER_AGENT = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 RuxitSynthetic/1.0 v5206104941427224227 t8464983649698732870 ath5ee645e0 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (Linux; Android 9; JAT-L41) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.63 Mobile Safari/537.36 ABB/3.2.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 RuxitSynthetic/1.0 v5850539865125209984 t7031922189477711439 athe94ac249 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36 RuxitSynthetic/1.0 v7504646058 t1650172424564047786 athfa3c3975 altpub cvcv=2 smf=0",
    "Mozilla/5.0 (Linux; arm_64; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaApp_Android/22.78.1 YaSearchBrowser/22.78.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36 RuxitSynthetic/1.0 v6106289593499753356 t7978617126683910420 ath259cea6f altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (Linux; Android 10; SM-A205FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 RuxitSynthetic/1.0 v2880630017468159540 t8883952605554344371 ath93eb305d altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 RuxitSynthetic/1.0 v21927890020 t3426260252853334511 athfa3c3975 altpub cvcv=2 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 RuxitSynthetic/1.0 v4279856980818293836 t2537736810932639330 ath5ee645e0 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 RuxitSynthetic/1.0 v7897331601289658854 t7629398982635883461 ath2653ab72 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36 RuxitSynthetic/1.0 v9016504694830673184 t8379550823119750660 ath5ee645e0 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (Linux; Android 7.0; TGW102L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 RuxitSynthetic/1.0 v2460860465118689570 t7978617126683910420 ath259cea6f altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 RuxitSynthetic/1.0 v1826633695271199249 t3933913501096950183 ath4b3726d5 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (Linux; Android 10; M2006C3MNG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36 RuxitSynthetic/1.0 v7504672081 t1650172424564047786 athfa3c3975 altpub cvcv=2 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 RuxitSynthetic/1.0 v1461335191726294374 t7843338426965001067 ath2653ab72 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 RuxitSynthetic/1.0 v6710484315693613566 t851036140292854579 ath2653ab72 altpriv cvcv=2 cexpw=1 smf=0",
    "Mozilla/5.0 (Linux; Android 8.1.0; Neffos_C7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'User-Agent': "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) '
#                  'Chrome/58.0.3029.110 Safari/537.3'"
# }

# LOG_STDOUT = True
# LOG_ENABLED = False
# LOG_LEVEL = 'INFO'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "fotocasa.middlewares.FotocasaSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "fotocasa.middlewares.FotocasaDownloaderMiddleware": 543,
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
