from scrapy import cmdline

__author__ = '01210367'


name = 'sfbestmain'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())