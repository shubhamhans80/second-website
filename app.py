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
        <loc>https://seekhocoding.online/</loc>
        <loc>https://seekhocoding.online/python/chapter/1/</loc>
    </url>

 </urlset>
''', mimetype='application/xml')

 
@app.route('/')
def home(): 
    return render_template('/python/chapters/index2.html')

@app.route('/chapter1')
def chapter1(): 
    return render_template('/python/chapters/index1.html')


# erros

@app.errorhandler(404)
def page_not_found(error): 
    return render_template('errors/error.html', 
                           error_code="404", 
                           error_message="Sorry, the page you are looking for is not available at this time. Please check the URL or visit the main page."), 404
 
@app.errorhandler(Exception)
def handle_all_exceptions(error): 
    app.logger.error(f"Unhandled Exception Occurred: {error}")
      
    return render_template('errors/error.html', 
                           error_code="500", 
                           error_message="This page is unable to open due to a temporary system issue. Our team will fix it soon."), 500

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