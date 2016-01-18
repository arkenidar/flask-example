#!python
from flask import Flask, request, render_template
app = Flask(__name__)
app.logger.info('go to http://localhost:5000/?query=abc')

@app.route('/')
def search():
    query = request.args.get('query', '')
    title = 'Search page' if query=='' else 'Search result for '+query
    items = [
    {'url':'http://abc.com', 'title':'abc'},
    {'url':'http://xyz.com', 'title':'xyz'},
    {'url':'http://abcxyz.com', 'title':'abcxyz'},
    {'url':'http://123.com', 'title':'123'},
    {'url':'http://qwerty.com', 'title':'qwerty'}
    ]
    items = items if query=='' else [ item for item in items if query in item['url'] or query in item['title'] ]

    return render_template('form.html', title=title, query=query, items=items)

if __name__ == '__main__':
    app.run(debug=True)