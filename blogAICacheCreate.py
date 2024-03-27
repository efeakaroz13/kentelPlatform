import redis
import time
from flask import Flask,request
import json
app = Flask(__name__)
red = redis.Redis()

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        try:
            pendingBlog = json.loads(red.get("blogPending"))
        except:
            pendingBlog = []
        content = request.form.get("content").strip().replace("\n\n","\n").split("\n")
        for c in content:
            if len(c)>4:
                data = {
                    "title":c,
                    "timeAdded":time.time(),
                    "status":"pending"
                }
                pendingBlog.append(data)
        red.set("blogPending",json.dumps(pendingBlog))
        return "Upload Complete!"
    return """
        <form action="" method="POST">

            <textarea name="content" placeholder="Enter titles(for AI Blog)" style="width:100%;height:80vh;"></textarea>

            <button type="submit" style="width:100%;height:20vh">Submit</button>
        </form>
    """

if __name__ == "__main__":
    app.run(debug=True,port=1313)
