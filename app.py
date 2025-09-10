from flask import Flask, request, render_template, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = "supersecret123"   # Needed for session
name_store = {}

def track_page(path):
    """Add a visited page into session, safely marking session modified."""
    visited = session.get('visited', [])
    if path not in visited:
        visited.append(path)
        session['visited'] = visited  # reassign so Flask persists it

def render_chapter(template_name, route):
    """Render any chapter with visited + all_visited context."""
    track_page(route)
    Username_value = name_store.get('username', None)

    required_routes = [
        '/', '/welcome', '/AI', '/web-design', '/cyber-security',
        '/ui-ux', '/computer-programming', '/information-and-digital-literacy',
        '/animation', '/graphic-design', '/digital-marketing', '/sound-video-editing'
    ]

    visited = set(session.get('visited', []))
    all_visited = set(required_routes).issubset(visited)

    return render_template(
        template_name,
        username=Username_value,
        visited=list(visited),
        all_visited=all_visited
    )

@app.route('/')
def intro():
    return render_chapter("intro.html", "/")

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    name_store['username'] = name
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    return render_chapter("welcome.html", "/welcome")

@app.route('/AI')
def AI():
    return render_chapter("AI.html", "/AI")

@app.route('/web-design')
def webdesign():
    return render_chapter("web-design.html", "/web-design")

@app.route('/cyber-security')
def cybersecurity():
    return render_chapter("cybersecurity.html", "/cyber-security")

@app.route('/ui-ux')
def ui_ux():
    return render_chapter("ui-ux.html", "/ui-ux")

@app.route('/computer-programming')
def computer_programming():
    return render_chapter("computer-programming.html", "/computer-programming")

@app.route('/information-and-digital-literacy')
def idl():
    return render_chapter("information-and-digital-literacy.html", "/information-and-digital-literacy")

@app.route('/animation')
def anime():
    return render_chapter("animation.html", "/animation")

@app.route('/graphic-design')
def graphic_design():
    return render_chapter("graphic-design.html", "/graphic-design")

@app.route('/digital-marketing')
def digital_marketing():
    return render_chapter("digital-marketing.html", "/digital-marketing")

@app.route('/sound-video-editing')
def sv():
    return render_chapter("sound-video-editing.html", "/sound-video-editing")

@app.route('/ending')
def end():
    return render_chapter("end.html", "/ending")

@app.route('/debug-visited')
def debug_visited():
    return jsonify(
        visited=session.get('visited', []),
        required=[
            '/', '/welcome', '/AI', '/web-design', '/cyber-security',
            '/ui-ux', '/computer-programming', '/information-and-digital-literacy',
            '/animation', '/graphic-design', '/digital-marketing', '/sound-video-editing'
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)
