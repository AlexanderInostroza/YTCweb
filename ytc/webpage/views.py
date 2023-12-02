from django.shortcuts import render
import os
import time
import instaloader

# Create your views here.

from django.http import HttpResponse

LAST_CHECKED_TIME = None

def instagram_scraper():
    dict = {'sessionid': '62745039570%3AtwL2Me68sI66z1%3A15%3AAYeQgkkJVxyWF8tq3AXKX0xxEFq35LbIvJlarvF1uQ', 'mid': 'ZUpoxQALAAH-9WvRdwb-adoF9oAf', 'ig_pr': '1', 'ig_vw': '1920', 'csrftoken': 'UMyZCywozLFaSwhDS8mRQDPzl9z5NbkB', 's_network': '', 'ds_user_id': '62745039570', 'ig_nrcb': '1', 'datr': 'xWhKZZuewX3Rsy_FRIaEI41O', 'ig_did': 'B05C36F4-34BF-41DE-8F6D-462B50F86303', 'shbid': '"6098\\0546924456958\\0541730911781:01f7aeffccdcdc20eaaef83b737b5fa71887ac143e78bfe652f0b8e3de39b6f442b7307f"', 'shbts': '"1699375781\\0546924456958\\0541730911781:01f77704d8e5f5b8b6e29324fd922d88a54fc2584f5039080813791c3a78ab6d009b25ec"'}
    loader = instaloader.Instaloader()
    loader.load_session("cuentinha9", dict)
    perfil_objetivo = 'yotecuidousm'
    profile = instaloader.Profile.from_username(loader.context, perfil_objetivo)
    post_list = []
    c=0
    for post in profile.get_posts():
        if c >= 6: break
        c+=1
        img_url = post.url
        caption = post.caption
        shortcode = post.shortcode
        isVideo = post.is_video
        if isVideo:
            img_url = "/static/resources/kapuholder.png"
            # img placeholder
        post_list.append((img_url, caption, shortcode))
    file = open("ytc/webpage/static/resources/posts.txt","w",encoding="utf-8")
    for img_url, caption, shortcode in post_list:
        file.write("::{}||{}||{}\n".format(img_url, caption, shortcode))
    file.close()
    
def home(request):
    global LAST_CHECKED_TIME
    if LAST_CHECKED_TIME == None:
        LAST_CHECKED_TIME = time.gmtime(0)
    current_time = time.gmtime(time.time())
    if LAST_CHECKED_TIME.tm_mday != current_time.tm_mday or LAST_CHECKED_TIME.tm_mon != current_time.tm_mon:
        LAST_CHECKED_TIME = current_time
        instagram_scraper()
    posts = []
    file = open("ytc/webpage/static/resources/posts.txt","r",encoding="utf-8")
    r_posts = "\n".join([ln.strip() for ln in file]).split("::")[1:]
    file.close()
    for r_post in r_posts:
        img_url, caption, shortcode = r_post.split("||")
        posts.append({
            "img_url": img_url,
            "caption": caption,
            "shortcode": shortcode
        })
    context = {"posts": posts}
    return render(request, "home.html", context)

def pets(request):
    i = 0
    dir = "ytc/webpage/static/content/adopcion"
    files = os.listdir(dir)
    pets = []
    for file in files:
        name, extension = file.split(".")
        if extension != "txt":
            info_file = open(dir+"/"+name+".txt", "r", encoding="utf-8")
            text = "".join([line.strip() for line in info_file])
            info_file.close()
            info = text.split("*")[1:]
            for i in range(len(info)):
                info[i] = {
                    "index": str(i+1),
                    "info_index": info[i].strip(),
                    }
            pets.append({
                "name": name,
                "img": file,
                "info": info,
            })
    context = {"pets": pets}
    return render(request, "pets.html", context)


def donate(request):
    file = open("ytc/webpage/static/content/donaciones/info.txt","r",encoding="utf-8")
    info = list(file)
    file.close()
    context = {"info": info}
    return render(request, "donate.html", context)

def aboutUs(request):
    dir = "ytc/webpage/static/content/administracion"
    files = os.listdir(dir)
    members = []
    for file in files:
        name, extension = file.split(".")
        if extension != "txt":
            info_file = open(dir+"/"+name+".txt", "r", encoding="utf-8")
            file_as_list = list(info_file)
            info_file.close()
            members.append({
                "name": file_as_list[0],
                "position": file_as_list[2],
                "img": file,
            })
    context = {"members": members}
    return render(request, "aboutUs.html", context)