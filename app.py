from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ninja_info_form.html')

@app.route('/result', methods = ['POST', 'GET'])
def ninja_info_card():
    if request.method == 'POST':
        result = request.form
        village = result.get('village')
        country = result.get('country')
        playerName = result.get('playerName')
        clan = result.get('clan')
        gender = result.get('gender')
        age = result.get('age')
        dob = result.get('dob')
        skill = result.get('skill')
        rank = result.get('rank')
        playerHeadshot = result.get('playerHeadshot')
        teamAvatar1 = result.get('teamAvatar1')
        teamName1 = result.get('teamName1')
        teamAvatar2 = result.get('teamAvatar2')
        teamName2 = result.get('teamName2')
        teamAvatar3 = result.get('teamAvatar3')
        teamName3 = result.get('teamName3')
        specializations = result.get('specializations')
        elements = result.get('elements')
        traits = result.get('traits')
        tai = result.get('tai')
        nin = result.get('nin')
        tools = result.get('tools')
        blood = result.get('blood')
        gen = result.get('gen')
        speed = result.get('speed')
        energy = result.get('energy')
        power = result.get('power')
        iq = result.get('iq')
        missionS = result.get('missionS')
        missionA = result.get('missionA')
        missionB = result.get('missionB')
        missionC = result.get('missionC')
        missionD = result.get('missionD')
        speedColor = "rgba(140, 194, 171, 1)" if speed != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'
        energyColor = "rgba(140, 194, 171, 1)" if energy != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'
        powerColor = "rgba(140, 194, 171, 1)" if power != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'
        iqColor = "rgba(140, 194, 171, 1)" if iq != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'

        if not teamAvatar1:
            teamAvatar1 = "via.placeholder.com/90x56"
        if not teamAvatar2:
            teamAvatar2 = "via.placeholder.com/90x56"
        if not teamAvatar3:
            teamAvatar3 = "via.placeholder.com/90x56"

        return render_template("ninja_info_card.html", village=village,
                               country=country,
                               playerName=playerName,
                               clan=clan,
                               gender=gender,
                               age=age,
                               dob=dob,
                               skill=skill,
                               rank=rank,
                               playerHeadshot=playerHeadshot,
                               teamAvatar1=teamAvatar1,
                               teamName1=teamName1,
                               teamAvatar2=teamAvatar2,
                               teamName2=teamName2,
                               teamAvatar3=teamAvatar3,
                               teamName3=teamName3,
                               specializations=specializations,
                               elements=elements,
                               traits=traits,
                               tai=tai,
                               nin=nin,
                               tools=tools,
                               blood=blood,
                               gen=gen,
                               speed=speed,
                               energy=energy,
                               power=power,
                               iq=iq,
                               speedColor=speedColor,
                               energyColor=energyColor,
                               powerColor=powerColor,
                               iqColor=iqColor,
                               missionS=missionS,
                               missionA=missionA,
                               missionB=missionB,
                               missionC=missionC,
                               missionD=missionD)

@app.route('/debug')
def debug():
    village = "https://i.imgur.com/zJy6KGs.png"
    country = "https://i.imgur.com/4Quyg2c.png"
    playerName = "Senju, Natsuki"
    clan = "Senju"
    gender = "Female"
    age = "19"
    dob = "April 25th"
    skill = "B"
    rank = "Chunin"
    playerHeadshot = "https://i.imgur.com/Sy31t85.png"
    teamAvatar1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQuwAVgKaSdHC1uElTXDcpZ4fn-BnLqTfNUTA&usqp=CAU"
    teamName1 = "Tsukuyomi"
    teamAvatar2 = "https://i.pinimg.com/originals/0f/80/51/0f80516c7f2c6e9710b742fc5a766f07.gif"
    teamName2 = "Susanoo"
    teamAvatar3 = "https://i.imgur.com/lHECSDT.jpg"
    teamName3 = "Momo"
    specializations = "<img src='https://files.jcink.net/uploads2/narutosaga/Specialization_Images/Taijutsu.png'><img src='https://files.jcink.net/uploads2/narutosaga/Specialization_Images/Ninjutsu.png'><img src='https://files.jcink.net/uploads2/narutosaga/Specialization_Images/Summoning.png'>"
    elements = "<img src='https://files.jcink.net/uploads2/narutosaga/Element_Images/Water.png'><img src='https://files.jcink.net/uploads2/narutosaga/Element_Images/Earth.png'><img src='https://files.jcink.net/uploads2/narutosaga/Element_Images/Wood.png'>"
    traits = "Agile, Chakra Sea"
    tai = "7"
    nin = "8"
    tools = "4"
    blood = "6"
    gen = "2"
    speed = "6"
    energy = "8"
    power = "5"
    iq = "6"
    speedColor = "rgba(140, 194, 171, 1)" if speed != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'
    energyColor = "rgba(140, 194, 171, 1)" if speed != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'
    powerColor = "rgba(140, 194, 171, 1)" if speed != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'
    iqColor = "rgba(140, 194, 171, 1)" if speed != max(speed, energy, power, iq) else 'rgba(228, 126, 109, 1)'
    output = f"""[dohtml]
    <style>
        /* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
        .flip-card {{
            background-color: transparent;
            width: 560px;
            height: 800px;
            perspective: 1000px; /* Remove this if you don't want the 3D effect */
            margin: auto; /*horizontal center*/
        }}

        /* This container is needed to position the front and back side */
        .flip-card-inner {{
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.8s;
            transform-style: preserve-3d;
        }}

        /* Do an horizontal flip when you move the mouse over the flip box container */
        .flip-card:hover .flip-card-inner {{
            transform: rotateY(180deg);
        }}

        /* Position the front and back side */
        .flip-card-front, .ninja-flip-card-back {{
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden; /* Safari */
            backface-visibility: hidden;
        }}

        /* Style the front side (fallback if image is missing) */
        .flip-card-front {{
            background-color: #bbb;
            color: black;
            overflow: hidden;
        }}


        /* Hide text during animation */
        .flip-card-inner:hover .text {{
            opacity: 0;
        }}
        /* Style the back side */
        .ninja-flip-card-back {{
            transform: rotateY(180deg);
            opacity: 0;
        }}
        /* Reveal back */
        .flip-card-inner:hover .ninja-flip-card-back {{
            -webkit-backface-visibility: visible; /* Safari */
            backface-visibility: visible;
            opacity: 1;
            animation-name: fadeInOpacity;
            animation-iteration-count: 1;
            animation-timing-function: ease-in;
            animation-duration: 0.8s;
        }}
        @keyframes fadeInOpacity {{
            0% {{
                opacity: 0;
            }}
            100% {{
                opacity: 1;
            }}
        }}
        .ninja-flip-card-back p,
        .ninja-flip-card-back h1{{
            font-weight: bold;
            margin: 0 auto; /* Center the text container */
            padding: 10px;
        }}
        .card-grid-container {{
            display: grid;
            grid-template-columns: 20% 20% 20% 20% 20%;
            grid-template-rows: 12% 38% 20% 15% 15%;
            /*background-color: tan;*/
            background-image: url('https://i.imgur.com/8WT1dlD.png');
            background-repeat: no-repeat;
            background-size: cover;
            border: 15px darkgreen solid;
            padding: 5px;
            max-width: 560px;
            height: 760px;
        }}

        .card-grid-item {{
            /*background-color: rgba(255, 255, 255, 0.3);*/
            /*border: 1px solid rgba(0, 0, 0, 0.5);*/
            padding: 5px;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .flex-center {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .two-by-one {{
            grid-column-start: auto;
            grid-column-end: span 2;
        }}
        .one-by-two {{
            grid-row-start: auto;
            grid-row-end: span 2;
        }}
        .three-by-two{{
            grid-column-start: auto;
            grid-column-end: span 3;
            grid-row-start: auto;
            grid-row-end: span 2;
        }}
        .emboss {{
            border: 2px solid rgba(0,0,0,0.3);
            background-color: rgba(255,255,255,0.3);
            box-shadow: 2px 2px 6px 1px rgba(0,0,0,0.37);
            -webkit-box-shadow: 2px 2px 6px 1px rgba(0,0,0,0.37);
        }}
        .country {{
            height: 100px;
            width: 100px;
            margin-top: -60px;
        }}
        .name {{
            padding: 5px;
        }}
        .basic-info {{
            list-style-type: none;
            text-align: left;
            padding-left: 5px;
        }}
        .basic-info li {{
            margin: 10px 10px;
            padding: 7px;
            font-weight: bold;
        }}
        .headshot img{{
            margin-bottom: 10px;
        }}
        .teammate {{
            flex-direction: column;
            padding: 1px;
        }}
        .teammate img{{
            width: 90px;
            height: 56px;
        }}
        .teammate p{{
            margin: 10px;
            padding: 10px;
            font-size: 12px;
        }}
        .specials {{
            padding: 10px;
            width: 100%;
            height: 90%;
            margin-top: 20px;
        }}
        .specials ul {{
            margin: 0px;
            padding: 0px;
            list-style-type: none;
        }}
        .specials li {{
            height: 15%;
            margin-top: 4px;
            margin-bottom: 4px;
            padding: 2px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .specials h5{{
            font-weight: bold;
            margin-right: 3px;
        }}
        .stats {{
            padding: 10px;
        }}
        .missions{{
            margin-top: 30px;
            margin-left: 5px;
            text-align: left;
        }}
        .missions div {{
            padding: 5px;
        }}
        .missions p{{
            margin: 0px;
            padding: 2px;
        }}
        .missions p:not(:last-child) {{
            border-bottom: #000 2px solid;
        }}
        .barstats{{
            margin-bottom: 70px;
        }}
        .force-right {{
            float: right;
        }}
    </style>

    <div class='flip-card'>
        <div class='flip-card-inner'>
            <div class='flip-card-front'>
                <img src='https://i.imgur.com/WFyVtlg.jpg' style='width:560px;height:800px;'>
            </div>
            <div class='ninja-flip-card-back'>
                <div class='card-grid-container'>
                    <div class='card-grid-item'><img class='village' src='{village}' /></div>
                    <div class='card-grid-item'></div>
                    <div class='card-grid-item'><img class='country' src='{country}'/></div>
                    <div class='card-grid-item two-by-one'><h2 class='emboss name'>{playerName}</h2></div>
                    <div class='card-grid-item two-by-one'><ul class='basic-info'>
                        <li class='emboss'>Clan: {clan}</li>
                        <li class='emboss'>Gender: {gender}</li>
                        <li class='emboss'>Age: {age}</li>
                        <li class='emboss'>DOB: {dob}</li>
                        <li class='emboss'>Skill Rank: {skill}</li>
                        <li class='emboss'>Shinobi Rank: {rank}</li>
                    </ul></div>
                    <div class='card-grid-item'></div>
                    <div class='card-grid-item two-by-one headshot'><img class='emboss' src='{playerHeadshot}'></div>
                    <div class='card-grid-item teammate'>
                        <img class='emboss' src='{teamAvatar1}'>
                        <p class='emboss'>{teamName1}</p>
                    </div>
                    <div class='card-grid-item teammate'>
                        <img class='emboss' src='{teamAvatar2}'>
                        <p class='emboss'>{teamName2} </p>
                    </div>
                    <div class='card-grid-item teammate'>
                        <img class='emboss' src='{teamAvatar3}'>
                        <p class='emboss'>{teamName3}</p>
                    </div>
                    <div class='card-grid-item two-by-one '>
                        <div class='specials flex-center'>
                            <ul>
                                <li class='emboss'><h5>Specializations:</h5>{specializations}</li>
                                <li class='emboss'><h5>Elements:</h5>  {elements}</li>
                                <li class='emboss'><h5>Traits:</h5> {traits}</li>
                            </ul>
                        </div>
                    </div>
                    <div class='card-grid-item'></div>
                    <div class='card-grid-item three-by-two stats'>
                        <script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.js' integrity='sha512-QEiC894KVkN9Tsoi6+mKf8HaCLJvyA6QIRzY5KrfINXYuP9NxdIkRQhGq3BZi0J4I7V5SidGM3XUQ5wFiMDuWg==' crossorigin='anonymous'></script>
                        <canvas id='pentaChart' width='298' height='208'></canvas>
                        <script>
                            var ctx = document.getElementById('pentaChart');
                            var pentaChart = new Chart(ctx, {{
                                type: 'radar',
                                data: {{
                                    labels: ['Tai', 'Nin', 'Tools', 'Blood', 'Gen'],
                                    datasets: [{{
                                        data: [{tai}, {nin}, {tools}, {blood}, {gen}],
                                        backgroundColor: 'rgba(255,0,0,0.3)'
                                    }}]
                                }},
                                options: {{
                                    legend: {{
                                        display: false,
                                    }},
                                    tooltips: {{
                                        enable: true,
                                    }},
                                    responsive: false,
                                    scale: {{
                                        pointLabels: {{
                                            fontSize: 18
                                        }},
                                        angleLines: {{
                                            display: false
                                        }},
                                        ticks: {{
                                            beginAtZero: true,
                                            min: 0,
                                            max: 10
                                        }}
                                    }}
                                }}
                            }});
                        </script>
                    </div>
                    <div class='card-grid-item one-by-two missions'>
                        <div class='emboss'>
                            <p>Missions:</p>
                            <p>S: <span class='force-right'>0</span></p>
                            <p>A: <span class='force-right'>0</span></p>
                            <p>B: <span class='force-right'>0</span></p>
                            <p>C: <span class='force-right'>0</span></p>
                            <p>D: <span class='force-right'>0</span></p>
                        </div>

                    </div>
                    <div class='card-grid-item barstats'><canvas id='barChart' width='100' height='200'></canvas>
                        <script>
                            var ctx = document.getElementById('barChart');
                            var barChart = new Chart(ctx, {{
                                type: 'bar',
                                data: {{
                                    labels: ['Speed', 'Energy', 'Power', 'IQ'],
                                    datasets: [{{
                                        data: [{speed}, {energy}, {power}, {iq}],
                                        backgroundColor: [
                                            '{speedColor}',
                                            '{energyColor}',
                                            '{powerColor}',
                                            '{iqColor}'
                                        ],
                                        borderColor: [
                                            'rgba(0, 0, 0, 1)',
                                            'rgba(0, 0, 0, 1)',
                                            'rgba(0, 0, 0, 1)',
                                            'rgba(0, 0, 0, 1)'
                                        ],
                                        borderWidth: 1
                                    }}]
                                }},
                                options: {{
                                    legend: {{
                                        display: false
                                    }},
                                    responsive: false,
                                    scales: {{
                                        yAxes: [{{
                                            ticks: {{
                                                display: false,
                                                beginAtZero: true,
                                                min: 0,
                                                max: 10
                                            }}
                                        }}]
                                    }}
                                }}
                            }});
                        </script></div>
                </div>
            </div>
        </div>
    </div>
    [/dohtml]"""
    return output
