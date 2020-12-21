from flask import Blueprint, jsonify
from engine.trie import result

tags = Blueprint('tags', __name__)


@tags.route('/', methods=['GET'])
# @token_verification
def get_tags():
	"""tags list view.
	---
	get:
		summary: 'A group of strings group base on their prefixes'
		description: 'Returns all the tags and words'
		operationId: 'ListTags'
		responses:
			401:
				description: 'UnAuthorized'
			500:
				description: 'Server error'
			'200':
				description: 'List Tags'
	"""
	return jsonify(result), 200
