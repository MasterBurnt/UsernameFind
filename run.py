try:
    from concurrent.futures import ThreadPoolExecutor 
    import requests 
    import threading
    import time
    import os
except ImportError as e:
    print(e)
    exit(0)

os.system('clear')
    
#Colors
c1 = '\033[0m'  #white
c2 = '\033[92m' #green
c3 = '\033[96m' #cyan
c4 = '\033[91m' #red
c5 = '\033[93m' #yellow 
c6 = '\033[94m' #blue
c7 = '\033[90m'


    
def banner():
    print(f"""
{c2}_  _ ____ ____ ____  ___  _  _ ____ _  _ ___
{c1}|  | [__  |___ |__/  |__] |  | |__/ |\ |  |
{c4}|__| ___] |___ |  \  |__] |__| |  \ | \|  |
    
""") 

banner()


#Internet connection
try:
    requests.get('https://www.github.com/MasterBurnt', timeout = 5)
except (requests. ConnectionError, requests. Timeout):
    print(c7+f'Please check your {c4}internet{c7} connection!')
    exit(0)

def banner1():
    print(f"""
{c2}                 ___
{c3} / /  _   _   _  )_  o  _   _ )
{c1}(_/  (   )_) )  (    ( ) ) (_( {c7}MᵃˢᵗᵉʳBᵘʳⁿᵗ
{c4}     _) (_
    
      """) 
     
while 1:
    user = input(c7+f'[?] {c2}Please Enter The Target{c5} Username {c2}:{c1}').strip()
    if user == "":
        print('Please Enter A Valid Username! ')
        time.sleep(2)
        os.system('clear')
        banner()
    else:
        break
        
save = []

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session
    
    
def go_site(url):
    session = get_session()   
    with session.get(url = url+user, timeout = 10) as response:
        if response.status_code == 200:
            print(c7+f"[+]{c2}Find : {url}{user}")
            save.append(url+user)
        else:
            print(c7+f'[-]{c4} Not Find! ')
            pass
        sys.exit()
def all_sites(sites):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(go_site, sites)


if __name__ == "__main__":
    os.system('clear')
    banner1()
    sites ={
    'https://www.championat.com/',
    'https://angel.co/u/',
    'https://www.7cups.com/',
    'https://www.chess.com/',
    'https://www.flickr.com/',
    'https://www.npmjs.com/',
    'https://www.bazar.cz/',
    'https://pokemonshowdown.com/',
    'https://freesound.org/',
    'https://www.memrise.com/',
    'https://tellonym.me/',
    'https://www.opennet.ru/',
    'https://chatujme.cz/',
    'https://www.munzee.com/',
    'https://ello.co/',
    'https://ask.fm/',
    'https://gunsandammo.com/',
    'https://hubski.com/',
    'https://pastebin.com/',
    'https://quizlet.com/',
    'https://community.signalusers.org/',
    'https://lolchess.gg/',
    'http://www.jeuxvideo.com/',
    'https://launchpad.net/',
    'https://letterboxd.com/',
    'https://www.academia.edu/',
    'https://imgup.cz/',
    'https://www.baby.ru/',
    'https://www.patreon.com/',
    'https://unsplash.com/',
    'https://www.goodreads.com/',
    'https://rubygems.org/',
    'https://www.aparat.com/',
    'https://www.smule.com/',
    'https://eintracht.de/',
    'https://houzz.com/',
    'https://raidforums.com/',
    'https://www.wattpad.com/',
    'https://www.sbazar.cz/',
    'https://www.kongregate.com/',
    'https://packagist.org/',
    'https://www.periscope.tv/',
    'https://tetr.io/',
    'https://youpic.com/',
    'https://lobste.rs/',
    'https://www.reverbnation.com/',
    'https://chaos.social/',
    'https://deviantart.com/',
    'https://www.freelancer.com/',
    'https://play.google.com/store/',
    'https://imgsrc.ru/',
    'https://opensource.com/',
    'https://vero.co/',
    'https://uid.me/',
    'https://www.pinterest.com/',
    'https://discussions.apple.com/',
    'https://ourdjtalk.com/',
    'https://slideshare.net/',
    'https://gfycat.com/',
    'https://www.sports.ru/',
    'https://forums.whonix.org/',
    'https://audiojungle.net/',
    'https://www.fixya.com/',
    'https://www.drive2.ru/',
    'https://www.behance.net/',
    'https://gab.com/',
    'https://www.pinkbike.com/',
    'https://www.shitpostbot.com/',
    'https://community.cloudflare.com/',
    'https://www.quora.com/profile/',
    'https://pcpartpicker.com/',
    'https://xboxgamertag.com/',
    'https://habr.com/',
    'https://www.nairaland.com/',
    'https://flipboard.com/',
    'https://www.kaggle.com/',
    'https://icq.com/',
    'https://www.redbubble.com/',
    'https://www.forumhouse.ru/',
    'https://newgrounds.com/',
    'https://contently.com/',
    'https://mastodon.cloud/',
    'https://www.mercadolivre.com.br/',
    'https://trashbox.ru/',
    'https://hubpages.com/',
    'https://soylentnews.org/',
    'http://www.wikidot.com/',
    'https://pcgamer.com/',
    'https://forum.guns.ru/',
    'https://irecommend.ru/',
    'https://prog.hu/',
    'https://codepen.io/',
    'https://www.native-instruments.com/forum/',
    'https://pypi.org/',
    'https://scratch.mit.edu/',
    'https://ok.ru/',
    'https://speedrun.com/',
    'https://virgool.io/',
    'https://lichess.org/',
    'https://www.dailykos.com/',
    'https://www.toster.ru/',
    'https://forum.hackthebox.eu/',
    'https://naver.com/',
    'https://www.codechef.com/',
    'https://wordpress.com/',
    'https://www.virustotal.com/',
    'https://www.countable.us/',
    'https://typeracer.com/',
    'https://fortnitetracker.com/challenges/',
    'https://www.colourlovers.com/',
    'https://sourceforge.net/',
    'https://forum.leasehackr.com/',
    'https://www.openstreetmap.org/',
    'https://soundcloud.com/',
    'https://www.zhihu.com/',
    'https://www.webnode.cz/',
    'https://otzovik.com/',
    'https://www.hackster.io/',
    'https://aminoapps.com/',
    'https://freelance.habr.com/',
    'https://social.tchncs.de/',
    'https://github.community/',
    'https://www.9gag.com/',
    'https://www.cnet.com/',
    'https://www.etsy.com/',
    'https://slack.com/',
    'https://splits.io/',
    'https://2Dimensions.com/',
    'https://linux.org.ru/',
    'https://php.ru/forum/',
    'https://www.cracked.com/',
    'https://ask.fedoraproject.org/',
    'https://crevado.com/',
    'https://www.metacritic.com/',
    'https://note.com/',
    'https://devrant.com/',
    'https://www.fotolog.com/author/',
    'https://mastodon.xyz/',
    'https://www.dailymotion.com/',
    'https://vk.com/',
    'https://www.hunting.ru/forum/',
    'https://www.fandom.com/',
    'https://vsco.co/',
    'https://buzzfeed.com/',
    'https://open.spotify.com/',
    'https://www.clozemaster.com/',
    'https://forum.sublimetext.com/',
    'https://hackerone.com/',
    'https://www.myminifactory.com/',
    'https://www.gumroad.com/',
    'https://www.pornhub.com/users/',
    'https://moikrug.ru/',
    'https://about.me/',
    'https://coroflot.com/',
    'https://giphy.com/',
    'https://gitee.com/',
    'https://www.rajce.idnes.cz/',
    'https://notabug.org/',
    'https://d3.ru/',
    'https://www.blogger.com/',
    'https://venmo.com/',
    'https://vimeo.com/',
    'https://www.buymeacoffee.com/',
    'https://idpay.ir/',
    'https://mstdn.io/',
    'https://tryhackme.com/',
    'https://myspace.com/',
    'https://blip.fm/',
    'https://weheartit.com/',
    'https://www.ifttt.com/',
    'https://keybase.io/',
    'https://www.flickr.com/photos/',
    'https://www.gamespot.com/',
    'https://disqus.com/',
    'https://akniga.org/profile/blue/',
    'https://www.producthunt.com/@',
    'https://members.fotki.com/',
    'https://www.svidbook.ru/',
    'https://www.github.com/',
    'https://www.babyblog.ru/',
    'https://news.ycombinator.com/',
    'https://dev.to/',
    'https://last.fm/',
    'https://www.designspiration.net/',
    'https://www.girlsaskguys.com/user/',
    'https://gitlab.com/',
    'https://spletnik.ru/',
    'https://career.habr.com/',
    'http://forum.3dnews.ru/',
    'https://www.strava.com/',
    'https://hackaday.io/',
    'https://repl.it/',
    'https://www.sporcle.com/',
    'https://www.researchgate.net/',
    'https://www.discogs.com/',
    'https://osu.ppy.sh/',
    'https://story.snapchat.com/@',
    'https://www.wikipedia.org/',
    'https://www.warriorforum.com/',
    'https://www.tradingview.com/',
    'https://f3.cool/',
    'https://getmyuni.com/',
    'https://leetcode.com/',
    'https://echo.msk.ru/',
    'https://www.livejournal.com/',
    'https://asciinema.org/',
    'https://robertsspaceindustries.com/',
    'https://egpu.io/',
    'https://www.trakt.tv/',
    'https://hackerrank.com/',
    'https://dribbble.com/',
    'https://wordpress.org/',
    'https://www.flightradar24.com/',
    'https://ultimate-guitar.com/',
    'http://en.gravatar.com/',
    'https://www.bandcamp.com/',
    'https://gurushots.com/',
    'https://imgur.com/',
    'https://issuu.com/',
    'http://forum.igromania.ru/',
    'https://www.instructables.com/',
    'https://rateyourmusic.com/',
    'https://www.codewars.com/',
    'https://www.roblox.com/',
    'https://www.fl.ru/',
    'https://archive.org/',
    'http://promodj.com/',
    'https://www.couchsurfing.com/',
    'https://ko-fi.com/',
    'https://www.kwork.ru/',
    'https://wix.com/',
    'https://www.geocaching.com/',
    'https://booth.pm/',
    'https://itch.io/',
    'https://www.livelib.ru/',
    'https://medium.com/',
    'https://www.alik.cz/',
    'https://www.polygon.com/',
    'https://www.producthunt.com/',
    'https://bitbucket.org/',
    'https://www.capfriendly.com/',
    'https://www.youtube.com/',
    'https://www.codecademy.com/',
    'https://www.scribd.com/',
    'http://www.authorstream.com/',
    'http://dating.ru/',
    'https://jbzd.com.pl/',
    'https://www.bookcrossing.com/',
    'https://discuss.elastic.co/',
    'https://virgool.io/@',
    }
    start_time = time.time()
    all_sites(sites)
    if save == []:
        print(c6+f'\nNothing was{c4} found!')       
    else:        
        duration = time.time() - start_time
        print(c6+f"\nUsername Found On {c1}{len(save)}{c6} Sites!\nThe file was saved in a history called {c1}{user}.txt{c5}\n\nSeconds {c1}{int(duration)}")
#SAVE
if save == []:
    exit(0)
else:        
    try:
        os.mkdir('history')
    except:
        pass
    os.chdir('history')
    file = open(user+".txt", "a") 
    for i in save:
        file.write(f'{i} \n')
    file.close()
    
    
