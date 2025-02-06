from flask import Flask, request, jsonify

app = Flask(__name__)

blogs = []

@app.route('/create', methods=['POST'])
def create_blog():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    blog = {"title": title, "content": content}
    blogs.append(blog)
    return jsonify({"message": "Blog created successfully!", "blog": blog})

@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
