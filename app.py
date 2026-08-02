from flask import Flask, render_template, url_for, jsonify, redirect, request, send_from_directory, Response
import os
app = Flask(__name__)  

 
    
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt') 

@app.route('/sitemap.xml')
def sitemap():

    return Response('<?xml version="1.0" encoding="UTF-8"?>\n'
'''
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>https://second-website-ohwa.onrender.com/</loc>
        <loc>https://second-website-ohwa.onrender.com/chapter1</loc>
    </url>

 </urlset>
''', mimetype='application/xml')

 
@app.route('/')
def home(): 
    return render_template('/python/chapters/index1.html')

@app.route('/chapter2')
def chapter2(): 
    return render_template('/python/chapters/index2.html')
 
# git status
# git add .
# git commit -m "Project updated with new features"
# git push origin main
 

# fresh upload starting se 

# Remove-Item -Recurse -Force .git
# git init
# git add -A
# git commit -m "Fresh initial commit"
# git branch -M main
# git remote add origin https://github.com/shubhamhans80/mysite.git
# git push -u origin main --force

 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)    