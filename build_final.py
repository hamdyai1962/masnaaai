import base64,zlib,os,subprocess,sys
base=r"C:\HamdyAI-Factory"
dist=base+"\\dist"
dat=base+"\\factory.dat"
print("  Reading compressed data...")
with open(dat,"r") as f:
    data=f.read()
print("  Data size: "+str(len(data))+" chars")
print("  Decompressing...")
html=zlib.decompress(base64.b64decode(data)).decode("utf-8")
print("  HTML size: "+str(len(html))+" bytes")
out=dist+"\\index.html"
with open(out,"w",encoding="utf-8") as f:
    f.write(html)
print("  Saved: "+out)
print("  Verifying...")
with open(out,"r",encoding="utf-8") as f:
    c=f.read()
ok=True
if not c.startswith("<!DOCTYPE"):
    print("  ERROR: Missing DOCTYPE");ok=False
if not c.rstrip().endswith("</html>"):
    print("  ERROR: Missing </html>");ok=False
ob=c.count("{");cb=c.count("}")
if ob!=cb:
    print("  ERROR: Braces "+str(ob)+"!="+str(cb));ok=False
if ok:
    print("  ===================================")
    print("  FACTORY BUILT SUCCESSFULLY!")
    print("  ===================================")
    print("  Size: "+str(len(c))+" bytes")
    print("  Braces: "+str(ob)+"="+str(cb)+" OK")
    print("  File: "+out)
    print()
    # Ask about GitHub
    ans=input("  Deploy to GitHub? (y/n): ").strip().lower()
    if ans=="y":
        token=input("  GitHub Token: ").strip()
        if token:
            os.chdir(base)
            subprocess.run(["git","remote","remove","origin"],capture_output=True)
            subprocess.run(["git","remote","add","origin","https://"+token+"@github.com/hamdyai1962/masnaaai.git"],capture_output=True)
            subprocess.run(["git","add","."],capture_output=True)
            r=subprocess.run(["git","commit","-m","Factory v16.0"],capture_output=True,text=True)
            print("  "+r.stdout.strip()[:80])
            r2=subprocess.run(["git","push","-u","origin","main","--force"],capture_output=True,text=True)
            if r2.returncode==0:
                print("  Pushed to main!")
            else:
                print("  Push error: "+r2.stderr.strip()[:80])
            r3=subprocess.run(["git","subtree","push","--prefix","dist","origin","gh-pages"],capture_output=True,text=True)
            if r3.returncode==0:
                print("  Published to gh-pages!")
            else:
                subprocess.run(["git","subtree","split","--prefix","dist","-b","tmp-gh"],capture_output=True)
                subprocess.run(["git","push","origin","tmp-gh:gh-pages","--force"],capture_output=True)
                subprocess.run(["git","branch","-D","tmp-gh"],capture_output=True)
                print("  Published (force)!")
            print("  URL: https://hamdyai1962.github.io/masnaaai/")
    print()
    ans2=input("  Start local server? (y/n): ").strip().lower()
    if ans2=="y":
        os.chdir(dist)
        print("  Server: http://localhost:3000")
        print("  Press Ctrl+C to stop")
        import http.server,socketserver
        try:
            with socketserver.TCPServer(("",3000),http.server.SimpleHTTPRequestHandler) as h:
                h.serve_forever()
        except OSError:
            with socketserver.TCPServer(("",8080),http.server.SimpleHTTPRequestHandler) as h:
                print("  Port 3000 busy, using 8080")
                h.serve_forever()
        except KeyboardInterrupt:
            print("  Stopped")
else:
    print("  BUILD FAILED - check errors above")
