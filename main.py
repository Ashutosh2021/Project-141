from email import header
from flask import Flask ,jsonify,request
from storage import all_articles,liked_articles,not_liked_articles

app=Flask(__name__)


@app.route("/get-article")
def get_article():
    return jsonify({
        "article": all_articles[0],
        "message":"success"
    },200)

@app.route("/liked-article",methods=["POST"])
def liked_article():
    article=all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message":"success"
    },200)

app.route("/not-liked-article",methods=["POST"])
def not_liked_article():
    article=all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message":"success"
    },200)

if __name__ == "__main__":
    app.run()