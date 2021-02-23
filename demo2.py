# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:20:33 2021

@author: tejas
"""
import scrapy
from ..items import Demo2Item

class myntrademo(scrapy.Spider):
    name = 'myntra'
    page = 2
    start_urls = ['https://www.flipkart.com/clothing-and-accessories/clothing-accessories/caps/mens-caps/pr?sid=clo%2Cqd8%2Cy9u%2Cgy0&p%5B%5D=facets.ideal_for%255B%255D%3DMen&hpid=S9qY-VWGz05lnCbmrdC-Gqp7_Hsxr70nj65vMAAFKlc=&fm=neon%2Fmerchandising&iid=M_8ce2752c-0107-46c4-b0d2-cbb9d4f4cc93_20.4K8U2QXOYSCB&ppt=hp&ppn=homepage&ssid=bee799eqb40000001614017294055&otracker=hp_omu_Top%2BFashion%2BBrands_3_20.dealCard.OMU_4K8U2QXOYSCB_14&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Top%2BFashion%2BBrands_NA_dealCard_cc_3_NA_view-all_14&cid=4K8U2QXOYSCB']
    
    def parse(self, response):
        items =  Demo2Item()
        
        brand_name = response.css('._2WkVRV::text').extract()
        price = response.css('._30jeq3::text').extract()
        discount = response.css('._3Ay6Sb span::text').extract()
        
        for i in range (len(discount)):
            items['brand_name'] = brand_name[i]
            items['price'] = price[i]
            items['discount'] = discount[i]
            
            yield items
            
            next_page = "https://www.flipkart.com/clothing-and-accessories/clothing-accessories/caps/mens-caps/pr?sid=clo%2Cqd8%2Cy9u%2Cgy0&p%5B%5D=facets.ideal_for%255B%255D%3DMen&hpid=S9qY-VWGz05lnCbmrdC-Gqp7_Hsxr70nj65vMAAFKlc%3D&fm=neon%2Fmerchandising&iid=M_8ce2752c-0107-46c4-b0d2-cbb9d4f4cc93_20.4K8U2QXOYSCB&ppt=hp&ppn=homepage&ssid=bee799eqb40000001614017294055&otracker=hp_omu_Top%2BFashion%2BBrands_3_20.dealCard.OMU_4K8U2QXOYSCB_14&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Top%2BFashion%2BBrands_NA_dealCard_cc_3_NA_view-all_14&cid=4K8U2QXOYSCB&page="+str(myntrademo.page)
            if myntrademo.page <= 5:
                 yield response.follow(next_page,callback=self.parse)
                 myntrademo.page += 1
            
            
        