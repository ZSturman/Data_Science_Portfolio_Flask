import datetime
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5ae3536d2465afe1fe3bc35138172d1'

app.config['DEBUG'] = True
app.config['TESTING'] = False

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True

app.config['MAIL_USERNAME'] = "zacharysturman@zsdynamics.com"
app.config['MAIL_PASSWORD'] = "mgjecqtdwqdngatd"

app.config['MAIL_DEFAULT_SENDER'] = ("Zachary from ZSDynamics.com", "ZS@ZSDynamics.com")
app.config['MAIL_MAX_EMAILS'] = "None"
#app.config['MAIL_SUPRESS_SEND'] = True
app.config['MAIL_ASCII_ATTACHMENTS'] = "False"

mail = Mail()
mail.init_app(app)


def redirect_url(default='home'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

def add_subscriber(name, email):
    print("New Subscriber!")
    print("name:", name)
    print("email:", email)
    msg = Message(
        subject = 'New Subscriber: '+name,
        recipients= ["zasturman@gmail.com", "zacharysturman@zsdynamics.com"],
        body = "name: "+name+"\n email: "+email
    )
    mail.send(msg)



@app.route('/send_mail', methods=["GET", "POST"])
def send_mail():
    name = request.form.get("name")
    email = request.form.get("email")
    input_message = request.form.get("message")

    msg = Message(
        subject = 'Does the Test work?!',
        recipients= [email],
        html = """<h5>Hello, """+name+""". Thank you for reaching out</h5><br><br> <p><em>Here's what you said: </em></p> <br> <p>"""+ input_message +"""  <button>Click Me!</button>"""
    )
    mail.send(msg)
    return redirect(redirect_url())



@app.route('/subscribe', methods=["GET", "POST"])
def subscribe():
    name = request.form.get("new-subscribers-name")
    email = request.form.get("new-subscribers-email")

    msg = Message(
        subject = 'Welcome '+name+"!",
        recipients= [email],
        html = """<h5>Hello, """+name+""". Thank you for subscribing</h5><br> <p>Would you like to see the coolest stuff ZSDynamics has made?</p><br> <a href="youtube.com">Yes, of course</a>"""
    )

    add_subscriber(name, email)

    mail.send(msg)

    flash(f'Check your email for your welcome basket', 'success')


    return redirect(redirect_url())


projects_list = [
    {
        "id":"tempProj", 
        "category":"data analysis",
        "title": "Temp Project",
        "date": "01/01/2023",
        "goal": "Which logo is best?",
        "strategy": "Use multiple logos among multiple participants to find the most eye-catching logo",
        "result": "Logo v2 with animation v3 most appealing",
        "brief_description": "brief desciption Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quas nulla maiores, magnam natus vitae dolorem ex tempore eius voluptates fuga.",
        "description": "description Lorem ipsum dolor sit amet consectetur, adipisicing elit. Deserunt necessitatibus porro aliquid sapiente dolorum voluptas voluptatibus, perspiciatis voluptate voluptatum provident. Quos, neque pariatur itaque dolor reprehenderit labore molestias est culpa eos, ex error enim. Est, voluptatum libero in beatae magnam similique, provident, adipisci quaerat quas nihil a at laborum consectetur expedita minima laboriosam vitae quos eaque illum et. Eos, soluta odio laboriosam recusandae inventore corporis dignissimos suscipit quos unde sunt quia sed delectus explicabo aperiam?",
        "closing": "closing Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus voluptatem, error nam inventore quisquam commodi non exercitationem velit sit doloremque minima recusandae dolore assumenda temporibus nobis blanditiis modi culpa vero sint. Tempore rerum pariatur corrupti.",
        "thumbnail": "thumbnail",
        "banner": "banner",
        "images": ["img one", "img two", "and three"],
        "image_explaination": ["111Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deserunt dolor consectetur ducimus. Eos nesciunt dolor enim vitae eveniet placeat tenetur?", "222Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deserunt dolor consectetur ducimus. Eos nesciunt dolor enim vitae eveniet placeat tenetur?", "333Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deserunt dolor consectetur ducimus. Eos nesciunt dolor enim vitae eveniet placeat tenetur?"],
        "links":["link one", "link two"]
    }
]

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
    return render_template('home.html', title="Home", projects=projects, projects_list=projects_list)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title="Portfolio", projects=projects)

@app.route("/data_analytics")
def data_analytics():
    return render_template('data_analytics.html', title="Data Analytics")

@app.route("/back_end")
def back_end():
    return render_template('back_end.html', title="Back-end Developer")
    
@app.route("/front_end")
def front_end():
    return render_template('front_end.html', title="Front-end Developer")

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact Page")

@app.route("/services")
def services():
    return render_template('services.html', title="Services Page")
