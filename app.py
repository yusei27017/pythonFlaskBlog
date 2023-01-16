from flask import Flask, request, make_response
from flask import render_template, redirect

from ctrl import mainApi

app = Flask(__name__)

##web page route
##chat GPT method
@app.route("/<page_name>")
def show_page(page_name):
    if page_name == "pixiv":
        return redirect("https://github.com/yusei27017/Pixiv")
    # elif page_name == "":
    #     return render_template("homePage.html")
    else:
        return render_template(f"{page_name}.html")

@app.route("/")
def homePage():
    return render_template("homePage.html")

# 原本
# @app.route("/aboutMe")
# def aboutMe():
#     return render_template("aboutMe.html")
# @app.route("/aboutSite")
# def aboutSite():
#     return render_template("aboutSite.html")
#

## web api
@app.route("/api", methods=['post'])
def mainPostRoute():
    try:
        json_param = request.data
        reslut_data = mainApi(json_param)
        # response = make_response(res,200)
        response = make_response(reslut_data, 200)
        return response
    except:
        response = make_response("error msg: Wrong format", 403)
        return response

## web site map
@app.route("/sitemap.xml")
def sitemap():
    return render_template("sitemap.xml")

