from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# 1. होम पेज रूट (Home Page Route)
@app.route('/')
def home():
    return render_template('index.html')

# 2. अबाउट पेज रूट (About Page Route)
@app.route('/about')
def about():
    return render_template('about.html')

# 3. Robots.txt रूट (गूगल सर्च के लिए)
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt')

if __name__ == '__main__':
    # debug=True रखने से कोड बदलते ही सर्वर अपने आप रीस्टार्ट हो जाता है
    app.run(debug=True)
