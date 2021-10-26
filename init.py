from flask import Flask,flash, render_template, request, session, jsonify,url_for,redirect,make_response
from flask_assets import Environment, Bundle
from flask_scss import Scss


app = Flask(__name__)
Scss(app)



bundles = {
    "font-awesome.css": Bundle('css/font-awesome.css', output = "gen/font-awesome.css"),
    "flex.css": Bundle('css/flex.css', output = "gen/flex.css"),

    "general.css": Bundle('assets/scss/general.scss', filters='pyscss', output='gen/general.css'),
    "slider.js": Bundle("javascript/slider.js", output = "gen/slider.js"),
}

assets = Environment(app)
assets.register(bundles)



@app.route('/')
def index():
    sections = [{
            "title": "Objective",
            "description": "A highly disciplined and hard-working individual looking for an internship in backend or other related areas of software development in a well established organization.",
            "items": {}
        },

        {
            "title": "Education",
            "description": "",
            "items": [{
                    "left": [{
                            "text": "Princess Sumaya University for Technology",
                            "url": "https://www.psut.edu.jo",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Bachelor in Computer Science",
                        }
                    ],
                    "right": [{
                            "text": "August 2018 - Expected January 2023",
                            "classes": ["italic"],
                        },
                        {
                            "text": "GPA: Very good with 82.2"
                        },

                        {
                            "text": "ranking 6<sup>th</sup> in cohort of 59 students."
                        },

                    ],
                },

                {
                    "left": [{
                            "text": "Jubilee High School",
                            "url": "http://www.jubilee.edu.jo",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Tawjihi",
                        }
                    ],
                    "right": [{
                        "text": "August 2014 - August 2018",
                        "classes": ["italic"],
                    }, ],
                },

            ]

        },

        {
            "title": "Experiences",
            "description": "",
            "items": [


                {
                    "left": [{
                            "text": "PSUT ACM Student Chapter",
                            "url": "https://psutsc.acm.org",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Problem solving beginner level insturctor",
                        },
                        {
                            "text":'''ACM Student Chapter in Princess Sumaya
                                        University for Technology''',
                            "classes": ["italic","small","grey"],

                        },
                    ],
                    "right": [{
                            "text": "September 2020  - Onging",
                            "classes": ["italic"],
                        },
                        {
                            "text": "Beginner level instuctor",
                            "classes": ["bold", "bullet-point-title", "sub-item"],
                        },
                        {
                            "text": "Teaching problem solving, algorithms and data stuctures for beginners in C++.",
                            "classes": ["sub-item"]
                        }
                    ],
                },
                {
                    "left": [{
                            "text": "PSUT ACM Student Chapter",
                            "url": "https://psutsc.acm.org",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Committee board member",
                        },
                         {
                            "text":'''ACM Student Chapter in Princess Sumaya
                                        University for Technology''',
                            "classes": ["italic","small","grey"],

                        },
                        
                    ],
                    "right": [{
                            "text": "Board member",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "September 2019  - September 2020",
                            "classes": ["italic"],

                        },
                        {
                            "text": "ACM new website",
                            "url": "https://psutsc.acm.org/",
                            "classes": ["bold", "bullet-point-title", "sub-item"],
                        },
                        {
                            "text": "Remaking the website using the new branding colors and themes, and making new features.",
                            "classes": ["sub-item"]
                        },
                        {
                            "text": "Treasurer",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "September 2021  - Onging",
                            "classes": ["italic"],
                        },
                        {
                            "text": "ACM leader board",
                            #"url": "https://psutsc.acm.org/",
                            "classes": ["bold", "bullet-point-title", "sub-item"],
                        },
                        {
                            "text": "Gamifying problem solving using Codeforces APIs.",
                            "classes": ["sub-item"]
                        },





                    ],
                },
                {
                    "left": [{
                            "text": "Codablity",
                            "url": "http://www.codability.net/",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Scratch level insturctor",
                        },
                        {
                            "text": '''
                            Codability is a non proﬁt Summer camp
                            that teaches school kids problem solving
                            through programming.
                            ''',
                            "classes": ["italic", "small","grey"],
                            #TODO add small
                        }
                    ],
                    "right": [{
                            "text": "Jun 2019  - August 2019",
                            "classes": ["italic"],
                        },
                        {
                            "text": "Scratch level instuctor",
                            "classes": ["bold", "bullet-point-title", "sub-item"],
                        },
                        {
                            "text": "Teaching kids from age 8 - 12 Computer Science, using <a target='_blank' href = 'https://scratch.mit.edu/' ><u>MIT Scratch</u></a>.",
                            "classes": ["sub-item"]
                        },

                    ],
                },

                {
                    "left": [{
                            "text": "Phi Science Institute",
                            "url": "https://phi.science/",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Visuals content creator",
                        },
                         {
                            "text":'''Phi Science aims to transform science and
                            deep tech education in the Arab region
                            through its precision education method.''',
                            "classes": ["italic","small","grey"],

                        },


                    ],
                    "right": [{
                            "text": "August 2018 - September 2019",
                            "classes": ["italic"],
                        },
                        {
                            "text": "Video editing automation",
                            #"url": "https://www.psut.edu.jo",
                            "classes": ["bold", "bullet-point-title", "sub-item"],
                        },
                        {
                            "text": "Worked on automating video editing in Adobe After effects.",
                            "classes": ["sub-item"]

                        },
                        {
                            "text": "Cutting down time for producing 1 video from 3 months to 3 hours.",
                            "classes": ["sub-item"]
                        },
                        {
                            "text": "Creating The Arabic Artiﬁcial Intelligence Summit branding",
                            "classes": ["sub-item"]
                        },

                    ],
                },

            ]

        }, {
            "title": "Projects",
            "description": "",
            "items": {},

        }, {
            "title": "Activities",
            "description": "",
            "items": [{
                    "left": [{
                        "text": "2021",
                        "classes": ["italic", "big"],
                    }, ],
                    "right": [{
                            "text": "Google Developer<br>Student Club - PSUT",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Member",
                            "classes": [""]
                        },

                    ],
                },
                {
                    "left": [
                        {
                        "text": "2020",
                        "classes": ["italic", "big"],
                          },
                    ],
                    "right": [
                        
                        {
                            "text": "Jordanian Collegiate Programming Contest - JCPC",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Seventh Place",
                            "classes": [""]
                        },

                    ],
                },

                {
                    "left": [
                    ],
                    "right": [
                        
                        {
                            "text": "Amazon Teckathon - Jordan",
                            #TODO add link here
                            "url":"https://www.amazonteckathon.com/",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Finalists, Best Presentation",
                            "classes": [""]
                        },

                    ],
                },
                
                {
                    "left": [
                    ],
                    "right": [
                        {
                            "text": "TEDx PSUT 2020",
                            "url": "https://www.tedxpsut.com/",
                            "classes": ["bold", "big"],
                        },
                        
                        {
                            "text": "Design Lead",
                            "classes": [""]
                        },

                    ],
                },
                {
                    "left": [{
                        "text": "2019",
                        "classes": ["italic", "big"],
                    }, ],
                    "right": [{
                            "text": "Startup Weekend Amman",
                            "classes": ["bold", "big"],
                        },
                        {
                            "text": "Third Place",
                            "classes": [""]
                        },

                    ],
                },
                {
                    "left": [

                    ],
                    "right": [
                        {
                            "text": "Amman Collegiate Programming Contest",
                            # "url": "https://www.tedxpsut.com/",
                            "classes": ["bold", "big"],
                        },
                        
                        {
                            "text": "Eighth place",
                            "classes": [""]
                        },

                    ],
                },
                {
                    "left": [{
                        "text": "2018",
                        "classes": ["italic", "big"],
                    }, ],
                    "right": [{
                            "text": "Startup Weekend Amman - SDG Version",
                            #"url": "https://www.tedxpsut.com/",
                            "classes": ["bold", "big"],
                        },

                        {
                            "text": "Third Place at the SDG Version",
                            "classes": [""]
                        },

                    ],
                },
                {
                    "left": [{
                        "text": "2017",
                        "classes": ["italic", "big"],
                    }, ],
                    "right": [{
                            "text": "Microsoft Imagine Cup 2017",
                            "url": "https://imaginecup.microsoft.com/en-us/Team/Index/cbbfc52e-0924-4dd6-8092-36fe3031e6ee",
                            "classes": ["bold", "big"],
                        },

                       {
                            "text": "First Place at The National Competition",
                        },
                        {
                            "text": "First Place at The Regional MEA Competition",
                        },
                        {
                            "text": "18th place world wide.",
                        }


                    ],
                },
               
            ]

        },

    ]
    cards = [{
        "title": "Alsaqifa",
        "description": "A platform for Arabian poets to gather and share poems and stuff.",
        "image_url": "Alsaqifa.png",
        "type": "personal project",
        "languages": ["Flask", "Flutter", "MySQL"],
        "github": [{
            "type": "Frontend",
            "url": "https://github.com/MohammadRimawi/Alsaqifa"
        }, {
            "type": "Backend",
            "url": "https://github.com/MohammadRimawi/Alsaqifa-API"
        }],
        "url": "",
        "youtube": ""
    }, {
        "title": "Varla",
        "description": "A personal voice assistant with alot of pesonal talered features.",
        "image_url": "Varla.jpg",
        "type": "personal project",
        "languages": ["Flask", "Flutter", "MySQL"],
        "github": [{
            "type": "Frontend",
            "url": "https://github.com/MohammadRimawi/Rimawification-Front-End"
        }, {
            "type": "Backend",
            "url": "https://github.com/MohammadRimawi/Rimawification-Backend"
        }],
        "url": "",
        "youtube": ""
    }, {
        "title": "Grade Tracker",
        "description": "Website that calculates my GPA and offer tools and insights for performance.",
        "image_url": "Grade tracker.png",
        "type": "personal project",
        "languages": ["Flask", "HTML", "CSS", "Chart.js"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/GradesTracker"
        }],
        "url": "",
        "youtube": ""

    }, {
        "title": "AI Garbage Classification",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "ai.jpg",
        "type": "Univesity project",
        "languages": ["Flask", "Flutter", "MySQL", "Python", "Tensorflow"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/Artificial-Intelligence"
        }],
        "url": "https://www.kaggle.com/rahafalabed/trash-classification",
        "youtube": ""
    }, {
        "title": "RimawiBank",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "",
        "type": "Univesity project",
        "languages": ["C#", "SQLite"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/RimawiBank"
        }],
        "url": "",
        "youtube": ""
    }, {
        "title": "Apollo",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "",
        "type": "Personal project",
        "languages": ["Flutter"],
        "github": [{
                "type": "Frontend",
                "url": "https://github.com/Apollo-LW/front-end"
            },
            {
                "type": "Project",
                "url": "https://github.com/Apollo-LW"
            }
        ],
        "url": "",
        "youtube": "https://youtu.be/CIEP0VCt-eU"
    }, {
        "title": "Squad",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "Squad.png",
        "type": "Personal project",
        "languages": ["Angular"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MrMoon/Squad"
        }],
        "url": "",
        "youtube": "https://youtu.be/q_rmZaASnZI"
    }, {
        "title": "Aghradi",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "Aghradi.png",
        "type": "Univesity project",
        "languages": ["PHP", "MySQL", "HTML", "CSS", "Javascipt"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/Aghradi"
        }],
        "url": "",
        "youtube": "https://youtu.be/UZPYmP-QJOg"
    }, {
        "title": "Graph Editor",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "",
        "type": "Univesity project",
        "languages": ["HTML", "CSS", "Javascipt"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/Graph-Editor"
        }],
        "url": "",
        "youtube": ""
    }, {
        "title": "ACM PSUT Student chapter website",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "ACM website.png",
        "type": "Personal project",
        "languages": ["PHP", "MySQL", "HTML", "CSS", "Javascipt", "Bootstrap"],
        "github": [],
        "url": "https://psutsc.acm.org",
        "youtube": ""
    }, {
        "title": "Adobe After effects video automation",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "",
        "type": "Work project",
        "languages": ["Javascipt"],
        "github": [],
        "url": "",
        "youtube": ""
    }, {
        "title": "Classical Encryption site",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "",
        "type": "University project",
        "languages": ["Python", "Flask", "HTML", "CSS", "Javascript", "Bootstrap"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/Information-Systems-Security"
        }],
        "url": "",
        "youtube": ""
    }, {
        "title": "Bing Daily wallpaper",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "bing.jpg",
        "type": "Personal project",
        "languages": ["Python", "Bash"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/Bing-Daily-Wallpaper"
        }],
        "url": "",
        "youtube": ""
    }, {
        "title": "This website :P",
        # "description": "A platform for Arabian poets A platform for Arabian poets",
        "image_url": "this website.png",
        "type": "Personal project",
        "languages": ["Flask", "HTML", "CSS", "Javascript"],
        "github": [{
            "type": "Project",
            "url": "https://github.com/MohammadRimawi/Rimawi-site"
        }],
        "url": "https://Mohammad.Rimawi.me",
        "youtube": ""
    }, ]

    programming_skills = [{
        "name": "Python",
        "type": "self-taught"
    }, {
        "name": "C++",
        "type": "University course"
    }, {
        "name": "SQL",
        "type": "University course"
    }, {
        "name": "HTML",
        "type": "University course"
    }, {
        "name": "CSS",
        "type": "University course"
    }, {
        "name": "JavaScript",
        "type": "University course"
    }, {
        "name": "Bash",
        "type": "self-taught"
    }, {
        "name": "Flask",
        "type": "self-taught"
    }, {
        "name": "Flutter",
        "type": "self-taught"
    }, {
        "name": "PHP",
        "type": "University course"
    }, {
        "name": "C#",
        "type": "University course"
    }, ]
    return render_template("home.html",cards=cards,programming_skills=programming_skills,sections=sections)



if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)


    
