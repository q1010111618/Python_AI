#访问电影表单数据
import requests
from lxml import html
import csv
import re
from typing import cast

#常量
MOVIE_LIST_FILE="csv_data/movie_top250.csv"
TMDB_BASE_URL="https://www.themoviedb.org"
TMDB_TOP_URL="https://www.themoviedb.org/movie/top-rated/" # 默认查询的是第一页的数据
TMDB_MORE_URL="https://www.themoviedb.org/discover/movie/items" #查询更多电影数据


#保存数据到csv文件
def save_to_csv(data):
    with open(MOVIE_LIST_FILE,'w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=["电影名","电影发布年份","电影上映时间","电影类型","电影时长","电影评分","电影语言","电影导演","电影作者","电影宣传语","电影简介"])
        writer.writeheader()
        writer.writerows(data)

# 
def get_movie_year(movie_years):
    movie_year=movie_years[0].strip() if movie_years else ''
    return movie_year.replace("(","").replace(")","")
   
def get_movie_publish_date(release_time):
    movie_date=release_time[0].strip() if release_time else ""
    # 匹配失败时 re.search 返回 None，需先判断再取 group()
    match=re.search(r"\d{4}-\d{2}-\d{2}",movie_date)
    return match.group() if match else ""

def get_movie_cost_time(runtime):
    movie_cost_time=runtime[0].strip() if runtime else ""
    h_res=re.search(r"(\d+)h",movie_cost_time)
    m_res=re.search(r"(\d+)m",movie_cost_time)
    h= int(h_res.group(1)) if h_res else 0
    m= int(m_res.group(1)) if m_res else 0
    return f"{h*60+m}分钟"

#获取电影详情
def get_movie_detail(url):
    response = requests.get(url, timeout=60)
    document = html.fromstring(response.text)
    # 获取电影名称
    title = document.xpath('//*[@id="original_header"]//section//h2/a/text()')
    # 获取电影发布年份
    release_date = document.xpath('//*[@id="original_header"]//section//h2/span/text()')
    # 获取电影上映时间
    release_time=document.xpath('//*[@id="original_header"]//section//span[@class="release"]/text()')
    # 获取电影时长
    runtime=document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()')
    # 获取电影类型
    # lxml 缺少类型存根，xpath 返回类型未知，这里显式转换为字符串列表
    genres=cast(list[str],document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="genres"]/a/text()'))
    # 获取电影评分
    rating=document.xpath('//*[@id="original_header"]//div[@id="consensus_pill"]//div[@class="user_score_chart"]/@data-percent')
    # 获取电影语言
    language=document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    # 获取电影导演
    director=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    # 获取电影作者
    authors=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    # 获取电影宣传语
    solgon=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[@class="tagline"]/text()')
    # 获取电影简介
    overview=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')
    
    #3.返回电影详情 - 字典
    movie_info={
        "电影名":title[0].strip() if title else "",
        "电影发布年份":get_movie_year(release_date),
        "电影上映时间":get_movie_publish_date(release_time),
        "电影类型":",".join(genres) if genres else "",
        "电影时长":get_movie_cost_time(runtime),
        "电影评分":rating[0].strip() if rating else "",
        "电影语言":language[0].strip() if language else "",
        "电影导演":director[0].strip() if director else "",
        "电影作者":authors[0].strip() if authors else "",
        "电影宣传语":solgon[0].strip() if solgon else "",
        "电影简介":overview[0].strip() if overview else ""
    }
    #print(movie_info)
    return movie_info


# 主函数，定义核心逻辑
def main():
    all_movies=[]

    # 循环获取第1页到第5页
    for page_num in range(1,12):
        if page_num==1:
            #1.发送请求，获取高分电影榜单
            response = requests.get(TMDB_TOP_URL,timeout=60)
        else:
            #1.发送请求，获取高分电影榜单
            response = requests.post(TMDB_MORE_URL,f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-03-14&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",timeout=60)
        print(f"发送请求，获取高分电影榜单第{page_num}页")
        #2. 解析回调信息
        document=html.fromstring(response.text)
        # 遍历获取电影的超链接
        movie_list=document.xpath(f'//div[@id="page_{page_num}"]//div[@data-object-id]//a[@data-media-type="movie"]/@href')
        print(movie_list)
        #3. 访问电影详情页面
        for movie_url in movie_list:
            full_url = TMDB_BASE_URL + movie_url
            print(f"电影详情页面: {full_url}")
            #发送请求，获取电影详情
            movie_info=get_movie_detail(full_url)
            all_movies.append(movie_info)
        #print(all_movies)

    #4. 保存数据到csv文件
    save_to_csv(all_movies)

if __name__ == '__main__':
    main()