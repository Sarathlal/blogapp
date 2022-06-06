from flask import Blueprint, redirect, url_for, flash, render_template, jsonify, request
from flask_restful import Resource

from blogapp.blog import api

class Post(Resource):
    def get(self):
        return {'hello': 'world'}, 200

api.add_resource(Post, '/v1/')