from flask import jsonify, request
from app import app, db
from app.models import Like

@app.route('/likes/store', methods=['POST'])
def store_like():
    data = request.get_json()
    user_id = data.get('user_id')
    content_id = data.get('content_id')

    like = Like(user_id=user_id, content_id=content_id)
    db.session.add(like)
    db.session.commit()
    return jsonify({'message': 'Like stored successfully'}), 201

@app.route('/likes/check', methods=['GET'])
def check_like():
    user_id = request.args.get('user_id')
    content_id = request.args.get('content_id')

    like = Like.query.filter_by(user_id=user_id, content_id=content_id).first()
    return jsonify({'liked': bool(like)})

@app.route('/likes/total', methods=['GET'])
def total_likes():
    content_id = request.args.get('content_id')

    total_likes = Like.query.filter_by(content_id=content_id).count()
    return jsonify({'total_likes': total_likes})
