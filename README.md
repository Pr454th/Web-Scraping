scrapy startproject project_name

scrapy genspider ietf pythonscraping.com

scrapy runspider ietf

scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10

scrapy runspider wikipedia.py -s FEED_URI=articles.csv -s FEED_FORMAT=csv
