import flask

import spotify

app = flask.Flask(__name__)

@app.route('/spotify')
def spotify_overlay():
    current_song = spotify.get_current_song()
    return flask.render_template('index.html', song=current_song)

@app.route('/chat')
def chat_overlay():
    for message in 
    
    return flask.render_template('chat.html', messages=[])

app.run(port=1177, debug=True)
