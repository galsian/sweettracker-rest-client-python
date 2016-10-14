# -*- coding: utf-8 -*-
import requests

API_URL = 'http://tracking.sweettracker.net/'

TEST_API_KEY = '7QCO3iQBOy8ZcfxqyezWEQ'

class SweetTracker(object):
	def __init__(self, api_key, api_url = API_URL):
		self.api_key = api_key
		self.api_url = API_URL
		requests_session = requests.Session()
		requests_adapters = requests.adapters.HTTPAdapter(max_retries=3)
		requests_session.mount('http://', requests_adapters)
		self.requests_session = requests_session

	def get_response(self, response):
		if response.status_code != requests.codes.ok:
			return {}
		result = response.json()
		return result

	def _get(self, url, payload=None):
		response = self.requests_session.get(url, headers=None, params=payload)
		return self.get_response(response)

	def get_company_info(self):
		url = '{}companylist?t_key={}'.format(self.api_url, self.api_key)
		return self._get(url)

	def get_tracking_info(self, company, tracking_id):
		url = '{}tracking?t_key={}&t_code={}&t_invoice={}'.format(self.api_url, self.api_key, company, tracking_id)
		return self._get(url)


	COMPANY_LIST = [{'Name': 'CJ대한통운', 'Code': '04'},
					{'Name': '한진택배', 'Code': '05'}, 
					{'Name': '현대택배', 'Code': '08'},
					{'Name': '우체국택배', 'Code': '01'},
					{'Name': '로젠택배', 'Code': '06'}, 
					{'Name': 'KG로지스택배(동부택배)', 'Code': '07'}, 
					{'Name': 'KG로지스택배(KG옐로우캡)', 'Code': '09'}, 
					{'Name': 'KGB택배', 'Code': '10'}, 
					{'Name': '일양로지스', 'Code': '11'}, 
					{'Name': 'EMS', 'Code': '12'}, 
					{'Name': 'DHL', 'Code': '13'}, 
					{'Name': 'FedEx', 'Code': '21'}, 
					{'Name': 'UPS', 'Code': '14'}, 
					{'Name': 'USPS', 'Code': '26'}, 
					{'Name': '대신택배', 'Code': '22'}, 
					{'Name': '경동택배', 'Code': '23'}, 
					{'Name': '합동택배', 'Code': '32'}, 
					{'Name': 'CVSnet 편의점택배', 'Code': '24'}, 
					{'Name': 'TNT Express', 'Code': '25'}, 
					{'Name': '한의사랑택배', 'Code': '16'}, 
					{'Name': 'GTX로지스', 'Code': '15'}, 
					{'Name': '천일택배', 'Code': '17'}, 
					{'Name': '건영택배', 'Code': '18'}, 
					{'Name': 'GSMNtoN(인로스)', 'Code': '28'}, 
					{'Name': '에어보이익스프레스', 'Code': '29'}, 
					{'Name': 'DHL Global Mail', 'Code': '33'}, 
					{'Name': 'i-Parcel', 'Code': '34'}, {
					'Name': '쿠팡 로켓배송', 'Code': '36'}, 
					{'Name': '범한판토스', 'Code': '37'}, 
					{'Name': 'KG로지스', 'Code': '39'}, 
					{'Name': '굿투럭', 'Code': '40'}]



