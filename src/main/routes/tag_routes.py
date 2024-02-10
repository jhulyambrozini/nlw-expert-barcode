from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def createtags():
    print(request.json)
    return jsonify({"res": "ok"})