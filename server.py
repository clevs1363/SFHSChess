from flask import Flask, request, render_template, url_for
SFHSChess = Flask(__name__)


@SFHSChess.route("/")
@SFHSChess.route("/index.html")
def runIndex():
    return render_template('/html/index.html')

@SFHSChess.route("/index.css")
def runIndexCSS():
    return url_for('static', filename='/css/index.css')

@SFHSChess.route("/info.html")
def runInfo():
    return render_template('html/info.html')

@SFHSChess.route("/info.css")
def runInfoCSS():
    return url_for('static', filename='/css/info.css')

@SFHSChess.route("/challenges.html")
def runChallenges():
    return render_template('/html/challenges.html')

@SFHSChess.route("/challenges.css")
def runCHallengesCSS():
    return url_for('static', filename='/css/challenges.css')

@SFHSChess.route("/strategy.html")
def runStrategy():
    return render_template('/html/strategy.html')

@SFHSChess.route("/strategy.css")
def runStrategyCSS():
    return url_for('static', filename='/css/strategy.css')

if __name__ == '__main__':
    SFHSChess.debug = True
    SFHSChess.run(host = '0.0.0.0', port = 5000)