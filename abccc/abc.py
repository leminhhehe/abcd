from flask import Flask, request
import json
from webex_api import get_message, post_message, bot_id

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # app flask chạy với 2 method là get và post
def index():
    if request.method == 'GET':   # Trường hợp nhận được get
        return "Run on port 5005"
    elif request.method == 'POST':  # Trường hợp nhận được post (vd: gửi tin nhắn)
        data = request.get_json()
        
        if bot_id == data['data']['personId']:  # Kiểm tra nếu id của bot trùng với id của người gửi thì bỏ qua
            print("ignore message from botself")
        else: 
            room_id = data['data']['roomId']  
            message_id = data['data']['id']
            print(json.dumps(data, indent=4))
            
            msg_text = f"Bot da nhan duoc tin nhan la '{get_message(message_id)}'"

            post_message(room_id, msg_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=False)