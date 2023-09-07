from django.shortcuts import render

# Create your views here.
#
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# # A dictionary to store user information
# # Example: { "Ankit": { "owes": {...}, "owed_by": {...}, "balance": ... }, ... }
# users = {}
#
#
# @app.route('/users', methods=['GET'])
# def get_users():
#     user_list = request.args.getlist('users')
#     if not user_list:
#         return jsonify(users)
#     else:
#         user_objects = []
#         for user in sorted(user_list):
#             if user in users:
#                 user_objects.append({user: users[user]})
#         return jsonify({'users': user_objects})
#
#
# @app.route('/add', methods=['POST'])
# def create_user():
#     user_name = request.json.get('user')
#     if not user_name:
#         return jsonify({'error': 'Invalid user name'})
#     if user_name in users:
#         return jsonify({'error': 'User already exists'})
#     users[user_name] = {'owes': {}, 'owed_by': {}, 'balance': 0.0}
#     return jsonify({user_name: users[user_name]})
#
#
# @app.route('/iou', methods=['POST'])
# def create_iou():
#     lender = request.json.get('lender')
#     borrower = request.json.get('borrower')
#     amount = request.json.get('amount')
#     if not (lender and borrower and amount):
#         return jsonify({'error': 'Invalid request body'})
#     if lender not in users:
#         return jsonify({'error': 'Lender does not exist'})
#     if borrower not in users:
#         return jsonify({'error': 'Borrower does not exist'})
#     users[lender]['owed_by'][borrower] = users[lender]['owed_by'].get(borrower, 0.0) + amount
#     users[borrower]['owes'][lender] = users[borrower]['owes'].get(lender, 0.0) + amount
#     users[lender]['balance'] -= amount
#     users[borrower]['balance'] += amount
#     return jsonify({'users': {lender: users[lender], borrower: users[borrower]}})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
