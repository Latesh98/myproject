from flask import Flask, request, jsonify

app = Flask(__name__)

blogs = []

@app.route('/create', methods=['POST'])
def create_blog():
    data = request.get_json()
    blog = {"id": len(blogs)+1, "title": data['title'], "content": data['content']}
    blogs.append(blog)
    return jsonify(blog), 201

@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs), 200

@app.route('/blog/<int:id>', methods=['GET'])
def get_blog(id):
    blog = next((blog for blog in blogs if blog["id"] == id), None)
    if blog:
        return jsonify(blog), 200
    return jsonify({"message": "Blog not found"}), 404

@app.route('/update/<int:id>', methods=['PUT'])
def update_blog(id):
    blog = next((blog for blog in blogs if blog["id"] == id), None)
    if blog:
        data = request.get_json()
        blog['title'] = data.get('title', blog['title'])
        blog['content'] = data.get('content', blog['content'])
        return jsonify(blog), 200
    return jsonify({"message": "Blog not found"}), 404

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_blog(id):
    blog = next((blog for blog in blogs if blog["id"] == id), None)
    if blog:
        blogs.remove(blog)
        return jsonify({"message": "Blog deleted"}), 200
    return jsonify({"message": "Blog not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
