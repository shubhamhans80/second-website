from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# 1. होम पेज रूट (Home Page Route)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pchapter2')
def chapter2():
    return render_template('index2.html')

# 2. अबाउट पेज रूट (About Page Route)
@app.route('/pabout')
def about():
    return render_template('about.html')

# 3. Robots.txt रूट (गूगल सर्च के लिए)
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt')



# git status
# git add . / git add e:\main\seekhocoding  
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
    # debug=True रखने से कोड बदलते ही सर्वर अपने आप रीस्टार्ट हो जाता है
    app.run(debug=True)
