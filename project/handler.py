from flask import render_template, request


class Handler:

    @classmethod
    def index(cls):
        if request.method == 'POST':
            text = request.form['text']
            print(text)

        return render_template('index.html')
