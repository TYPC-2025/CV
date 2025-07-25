from icrawler.builtin import BingImageCrawler

# 下载目录
hotdog_dir = 'dataset/train/hot_dog'
not_hotdog_dir = 'dataset/train/not_hot_dog'

# 创建爬虫并爬取热狗图像
hotdog_crawler = BingImageCrawler(storage={'root_dir': hotdog_dir})
hotdog_crawler.crawl(keyword='hot dog food', max_num=100)

# 创建爬虫并爬取非热狗图像（排除 hotdog 关键词）
not_hotdog_crawler = BingImageCrawler(storage={'root_dir': not_hotdog_dir})
not_hotdog_crawler.crawl(keyword='salad sandwich pizza sushi -hotdog -hot dog', max_num=100)
