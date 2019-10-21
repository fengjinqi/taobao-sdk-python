'''
Created by auto_sdk on 2019.07.03
'''
from top.api.base import RestApi
class TbkActivitylinkGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.platform = None
		self.promotion_scene_id = None
		self.relation_id = None
		self.sub_pid = None
		self.union_id = None

	def getapiname(self):
		return 'taobao.tbk.activitylink.get'
