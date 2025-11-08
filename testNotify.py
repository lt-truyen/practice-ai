from time import sleep
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # cần để dùng flash

@app.route('/')
def index():
    flash('Chào mừng bạn đến với Flask Notification1!', 'success')
    sleep(1500)
    flash('Chào mừng bạn đến với Flask Notification2!', 'success')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
