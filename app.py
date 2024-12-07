from flask import Flask, jsonify, request

app = Flask(__name__)

# 测试路由
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

# 创建 API 路由 - 获取用户信息
@app.route("/user/<username>", methods=["GET"])
def get_user(username):
    return jsonify({"username": username, "message": f"Hello, {username}!"})

# 创建 API 路由 - 接收 JSON 数据
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    return jsonify({"received_data": data, "message": "Data received successfully!"})

# 启动服务器
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
