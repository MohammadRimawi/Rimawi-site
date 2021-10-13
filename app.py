from flask import Flask,flash, render_template, request, session, jsonify,url_for,redirect,make_response
from flask_assets import Environment, Bundle
from flask_scss import Scss


app = Flask(__name__)
Scss(app)



bundles = {
    "flex.css": Bundle('css/flex.css', output = "gen/flex.css"),
    "general.css": Bundle('assets/scss/general.scss', filters='pyscss', output='gen/general.css'),
    "slider.js": Bundle("javascript/slider.js", output = "gen/slider.js"),
}

assets = Environment(app)
assets.register(bundles)



@app.route('/')
def index():

    sections = [
        {
            "title":"Objective",
            "description":"A highly disciplined and hard-working individual looking for an internship in backend or other related areas of software development in a well established organization.",
            "items":{}
        },

        {
            "title":"Education",
            "description":"",
            "items":[   
            {
                "left":[
                        {
                            "text":"Princess Sumaya University for Technology",
                            "url":"https://www.psut.edu.jo",
                            "classes":["bold","big"],
                        },
                        {
                            "text":"Bachelor in Computer Science",
                        }
                     ],
                "right":[
                    {
                        "text":"2018 August - Expected 2023 January"
                    },
                                {
                        "text":"GPA: Very good with 82.2"
                    },
                
                    {
                        "text":"Sixth on batch"
                    },
                    {
                        "text":"Project 1",
                        "url":"https://www.psut.edu.jo",
                        "classes":["bold" ,"bullet-point-title"],
                    },
                    {
                        "text":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aspernatur iure optio fuga eveniet explica.",
                    }
                  ],
            },
           
            {
                "left":[
                {
                    "text":"Jubilee High School",
                    "url":"http://www.jubilee.edu.jo",
                    "classes":["bold","big"],
                },
                {
                    "text":"Tawjihi",
                }
            ],
            "right":[
                {
                    "text":"2014 August - 2018 July"
                },       
            ],
        },
            
            ]

        },

         {
            "title":"Experinces",
            "description":"",
            "items":[
                
            {
                "left":[
                        {
                            "text":"Princess Sumaya University for Technology",
                            "url":"https://www.psut.edu.jo",
                            "classes":["bold","big"],
                        },
                        {
                            "text":"Bachelor in Computer Science",
                        }
                     ],
                "right":[
                    {
                        "text":"2018 August - Expected 2023 January"
                    },
                                {
                        "text":"GPA: Very good with 82.2"
                    },
                
                    {
                        "text":"Sixth on batch"
                    },
                    {
                        "text":"Project 1",
                        "url":"https://www.psut.edu.jo",
                        "classes":["bold" ,"bullet-point-title"],
                    },
                    {
                        "text":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aspernatur iure optio fuga eveniet explica.",
                    }
                  ],
            },
           
            {
                "left":[
                {
                    "text":"Princess Sumaya University for Technology",
                    "url":"https://www.psut.edu.jo",
                    "classes":["bold","big"],
                },
                {
                    "text":"Bachelor in Computer Science",
                }
            ],
            "right":[
                {
                    "text":"2018 August - Expected 2023 January"
                },
                             {
                    "text":"GPA: Very good with 82.2"
                },
            
                {
                    "text":"Sixth on batch"
                },
                {
                    "text":"Project 1",
                    "url":"https://www.psut.edu.jo",
                    "classes":["bold" ,"bullet-point-title"],
                },
                {
                    "text":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aspernatur iure optio fuga eveniet explica.",
                }
            ],
            },
            
            ]

        },
                  {
            "title":"Projects",
            "description":"",
            "items":{},

        },
 {
            "title":"Experinces",
            "description":"",
            "items":[
                
            {
                "left":[
                        {
                            "text":"Princess Sumaya University for Technology",
                            "url":"https://www.psut.edu.jo",
                            "classes":["bold","big"],
                        },
                        {
                            "text":"Bachelor in Computer Science",
                        }
                     ],
                "right":[
                    {
                        "text":"2018 August - Expected 2023 January"
                    },
                                {
                        "text":"GPA: Very good with 82.2"
                    },
                
                    {
                        "text":"Sixth on batch"
                    },
                    {
                        "text":"Project 1",
                        "url":"https://www.psut.edu.jo",
                        "classes":["bold" ,"bullet-point-title"],
                    },
                    {
                        "text":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aspernatur iure optio fuga eveniet explica.",
                    }
                  ],
            },
           
            {
                "left":[
                {
                    "text":"Princess Sumaya University for Technology",
                    "url":"https://www.psut.edu.jo",
                    "classes":["bold","big"],
                },
                {
                    "text":"Bachelor in Computer Science",
                }
            ],
            "right":[
                {
                    "text":"2018 August - Expected 2023 January"
                },
                             {
                    "text":"GPA: Very good with 82.2"
                },
            
                {
                    "text":"Sixth on batch"
                },
                {
                    "text":"Project 1",
                    "url":"https://www.psut.edu.jo",
                    "classes":["bold" ,"bullet-point-title"],
                },
                {
                    "text":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aspernatur iure optio fuga eveniet explica.",
                }
            ],
            },
            
            ]

        },

    ]
    cards = [
        {"title": "Alsaqifa","description":"A platform for Arabian poets to gather and share poems and stuff.","image_url":"marguerite-729510__340.jpg" ,"type":"personal project","languages":["Flask", "Flutter", "MySQL"]},
        {"title": "Varla","description":"A personal voice assistant with alot of pesonal talered features.","image_url":"marguerite-729510__340.jpg","type":"personal project", "languages":["Flask", "Flutter", "MySQL"]},
        {"title": "Grade Tracker","description":"Website that calculates my GPA and offer tools and insights for performance.","image_url":"marguerite-729510__340.jpg","type":"personal project", "languages":["Flask", "HTML", "CSS","Chart.js"]},
        {"title": "AI Garbage Classification","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Univesity project","languages":["Flask", "Flutter", "MySQL"]},
        {"title": "RimawiBank","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Univesity project","languages":["C#", "SQLite"]},
        {"title": "Apollo","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Personal project","languages":["Flutter"]},
        {"title": "Squad","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Personal project","languages":["Angular"]},
        {"title": "Aghradi","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Univesity project","languages":["PHP", "MySQL","HTML","CSS","Javascipt"]},
        {"title": "Graph Editor","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Univesity project","languages":["HTML","CSS","Javascipt"]},
        {"title": "ACM PSUT Student chapter website","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Personal project","languages":["PHP", "MySQL","HTML","CSS","Javascipt","Bootstrap"]},
        {"title": "Adobe After effects video automation","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Work project","languages":["Javascipt"]},
        {"title": "Classical Encryption site","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"University project","languages":["Python","Flask","HTML","CSS","Javascript","Bootstrap"]},
        {"title": "Bing Daily wallpaper","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Personal project","languages":["Python","Bash"]},
        {"title": "This website :P","description":"A platform for Arabian poets A platform for Arabian poets","image_url":"marguerite-729510__340.jpg","type":"Personal project","languages":["Flask","HTML","CSS","Javascript"]},
    ]

    programming_skills = [
        {"name":"Python"},
        {"name":"C++"},
        {"name":"SQL"},
        {"name":"HTML"},
        {"name":"CSS"},
        {"name":"JavaScript"},
        {"name":"Bash"},
        {"name":"Flask"},
        {"name":"Flutter"},
        {"name":"PHP"},
        {"name":"C#"},
    ]
    return render_template("home.html",cards=cards,programming_skills=programming_skills,sections=sections)



if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)


    