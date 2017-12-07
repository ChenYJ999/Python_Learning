#containing the exceptions raised by urllib.request 处理requests 提供的错误
import urllib.error
#用来解析URLs
import urllib.parse
#for opening and reading URLs
import urllib.request
#正则表达式
import re
#处理文件和目录
import os



#获得页面的专题信息
def Page_Info(myPage):
	mypage_Info = re.findall('<div class="titleBar" id=.*?><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
	return mypage_Info

#将信息保存在本地
def StringListSave(save_path,filename,slist):
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	path = save_path + '/' + filename + '.txt'
#这样写后，能省去 fp.close() 
	with open(path,'w+') as fp:
		for s in slist:
			fp.write('%s\t\t%s\n\n'%(s[0],s[1]))
#		fp.write(slist)			


def New_Page_Info(new_page):
	new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)\.html".*?>(.*?)</a></td>', new_page, re.S)
	results = []
	for url,item in new_page_Info:
		results.append((item,url+'.html'))
	return results

def Spider(url):
	print("downloading"+url+'\n')

	response = urllib.request.urlopen(url,timeout=10)

	My_page = response.read().decode("gbk")	

	myPageResults = Page_Info(My_page)

	save_path = '网易新闻抓取'
	i = 0
	filename = str(i)+'_'+'新闻排行榜'

#	StringListSave(save_path,filename,myPageResults)

	i = 1
	for item,url in myPageResults:
		print(str(i)+"  downloading..."+url+'\n')
		response = urllib.request.urlopen(url,timeout=10)
		new_page = response.read().decode('gbk')
		new_page_result = New_Page_Info(new_page)
		print(type(new_page_result))
		filename = str(i)+'_'+item+ '_新闻排行榜'		
		StringListSave(save_path,filename,new_page_result)
		i += 1







if __name__ == '__main__':
	print("start...")
	start_url = "http://news.163.com/rank/"
	Spider(start_url)
	print("End...")
