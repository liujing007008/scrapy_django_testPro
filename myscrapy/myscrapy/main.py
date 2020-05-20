import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "myspider_haha"])  # 这句代码会执行爬虫类中 name = "myspider_haha"的类