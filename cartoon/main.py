from scrapy import cmdline
import os
from cartoon import settings






#
# def jpg2pdf():
#
#     width, height = Image.open(episode_path + '/' + pic_list[0]).size
#     pdf = FPDF(unit='pt', format=[width, height])
#
#     for i in pic_list:
#         pdf.add_page()
#         pdf.image(episode_path + '/' + i, 0, 0)
#     pdf.output(path + '/output.pdf', 'F')

os.system('rm -rf %s/*' % settings.IMAGES_STORE)
cmdline.execute('scrapy crawl comic'.split())

