from flask import Flask, render_template, url_for

app = Flask(__name__)

projects= [
    {
        "id":"proj1",
        "title": "Proj 1 title",

        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil doloremque laudantium reiciendis. Harum assumenda, fuga cupiditate aperiam animi, debitis voluptatem consequuntur ipsum tenetur saepe necessitatibus et omnis aliquid aspernatur inventore ut recusandae deleniti illo ex.",

        "closing": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe, veniam debitis possimus vitae temporibus est tenetur blanditiis, odit nihil nam ex sint adipisci obcaecati quaerat? Accusantium repudiandae accusamus fuga soluta.",

        "img": "../static/images/temp_graph.png",

        "icon":"../static/images/python.png",

        "category":"Python Developer",

        "date": "12/03/2022"
    },
    {
        "id":"proj2",
        "title": "Proj 2 title",
        "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Repudiandae vero illo, sit veniam anim  autem exercitationem voluptatum at illum odit corporis obcaecati",
        "closing":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea consequatur molestias saepe mollitia aperiam exercitationem!",
        "img": "../static/images/temp_graph2.png",
        "date": "11/05/2022"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home", projects=projects)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title="Portfolio", projects=projects)

@app.route("/data_science")
def data_science():
    return render_template('data_science.html', title="Data Science")

@app.route("/infographics")
def infographics():
    return render_template('infographics.html', title="Animals")

@app.route("/python_developer")
def python_developer():
    return render_template('python_developer.html', title="Python Developer")