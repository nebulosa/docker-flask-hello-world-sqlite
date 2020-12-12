from flask import redirect, url_for, request

from app import app, db
from app.models import Request

import uuid

@app.route('/index.html', methods=['GET', 'POST'])
def index_html():
    return redirect(url_for('index'))

@app.route('/',      methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    log = 'I just said hello to {}, n.n/'.format(request.remote_addr)
    app.logger.debug(log)
    r = Request(log=log)
    db.session.add(r)
    db.session.commit()
    return 'hello world from {}\n'.format(uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.getnode())))
