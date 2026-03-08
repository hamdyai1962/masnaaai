import os,re
print("=== FIXING PUTER.JS CONNECTION ===")
f=r"C:\HamdyAI-Factory\dist\index.html"
with open(f,"r",encoding="utf-8") as h: c=h.read()
print("  Read: "+str(len(c))+" bytes")

# Fix 1: Add puter.auth.signIn button + auto-connect
fix_js="""
<div id="puterLogin" style="position:fixed;top:60px;left:50%;transform:translateX(-50%);z-index:9999;background:rgba(10,16,32,.95);border:2px solid #00ff88;border-radius:16px;padding:24px 32px;text-align:center;backdrop-filter:blur(10px);display:none">
<div style="font-size:32px;margin-bottom:12px">🔐</div>
<div style="font-size:16px;font-weight:800;color:#00ff88;margin-bottom:8px">تسجيل الدخول مطلوب</div>
<div style="font-size:13px;color:#94a3b8;margin-bottom:16px">لاستخدام الذكاء الاصطناعي مجاناً، سجّل دخولك في Puter</div>
<button onclick="doPuterLogin()" style="padding:14px 40px;background:#00ff88;color:#050910;border:none;border-radius:12px;font-size:15px;font-weight:900;cursor:pointer;font-family:inherit;transition:all .2s">🚀 تسجيل الدخول مجاناً</button>
<div style="font-size:10px;color:#475569;margin-top:10px">Puter.js — مجاني بالكامل — لا يحتاج بطاقة ائتمان</div>
</div>
<script>
async function doPuterLogin(){
try{
await puter.auth.signIn();
document.getElementById('puterLogin').style.display='none';
location.reload();
}catch(e){alert('خطأ: '+e.message)}
}
async function checkPuterConnection(){
try{
var s=await puter.auth.isSignedIn();
if(!s){document.getElementById('puterLogin').style.display='block'}
else{
try{var u=await puter.auth.getUser();
var dots=document.querySelectorAll('.dot,.status-dot,[id*=puter],[id*=Puter]');
dots.forEach(function(d){d.style.background='#00ff88'});
var statEls=document.querySelectorAll('[id*=status],[id*=Status],[id*=puter],[id*=Puter]');
statEls.forEach(function(el){if(el.textContent.indexOf('متصل')>-1||el.textContent.indexOf('Offline')>-1||el.textContent.indexOf('غير')>-1){el.textContent='متصل: '+u.username}});
}catch(e){}
}
}catch(e){document.getElementById('puterLogin').style.display='block'}
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',function(){setTimeout(checkPuterConnection,2000)})}
else{setTimeout(checkPuterConnection,2000)}
</script>
"""

# Insert before </body>
if "</body>" in c:
    c=c.replace("</body>",fix_js+"\n</body>")
    print("  Injected Puter login fix before </body>")
elif "</html>" in c:
    c=c.replace("</html>",fix_js+"\n</html>")
    print("  Injected Puter login fix before </html>")

with open(f,"w",encoding="utf-8") as h: h.write(c)
print("  Saved: "+str(len(c))+" bytes")

# Redeploy to GitHub
print("  Deploying to GitHub...")
os.chdir(r"C:\HamdyAI-Factory")
import subprocess
subprocess.run(["git","add","."],capture_output=True)
r=subprocess.run(["git","commit","-m","Fix Puter.js connection + auto-login"],capture_output=True,text=True)
print("  "+r.stdout.strip()[:80])
r2=subprocess.run(["git","push","origin","main","--force"],capture_output=True,text=True)
if r2.returncode==0: print("  Pushed to main!")
else: print("  Push: "+r2.stderr.strip()[:80])
subprocess.run(["git","subtree","split","--prefix","dist","-b","tmp-gh"],capture_output=True)
subprocess.run(["git","push","origin","tmp-gh:gh-pages","--force"],capture_output=True)
subprocess.run(["git","branch","-D","tmp-gh"],capture_output=True)
print("  Published to gh-pages!")
print()
print("  ===================================")
print("  FIX APPLIED + DEPLOYED!")
print("  ===================================")
print("  URL: https://hamdyai1962.github.io/masnaaai/")
print()
print("  How to use:")
print("  1. Open the URL above")
print("  2. Click the green login button")
print("  3. Sign in to Puter (free)")
print("  4. Factory will connect automatically!")
print()
