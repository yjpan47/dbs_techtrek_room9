import os
import datetime
from flask import request
from flask_restplus import Resource, Namespace
from api.main.config import IMAGE_DIR


API = Namespace(
    name='customer',
    description='Operations related to adding, retrieving, deleting, and updating data for the customer entity.'
)


@API.route('/srkhfaeoihgowsefaw', strict_slashes=False)
class RestaurantAuthTokenController(Resource):
    def get(self):
        return "HGellofwef", 200

# @API.route('/auth/refresh', strict_slashes=False)
# class RestaurantAuthTokenController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return RestaurantService.refresh_restaurant_auth_token(restaurant_id)
#
#
# @API.route('/auth/register', strict_slashes=False)
# class RestaurantRegisterController(Resource):
#     def post(self):
#         data = request.json
#         return RestaurantService.register_restaurant(
#             email=data.get('email'),
#             password=data.get('password'),
#             name=data.get('name'),
#             description=data.get('description'),
#             street_address=data.get('street_address'),
#             unit_number=data.get('unit_number'),
#             country=data.get('country'),
#             postal_code=data.get('postal_code')
#         )
#
#
# @API.route('/auth/login', strict_slashes=False)
# class RestaurantLoginController(Resource):
#     def post(self):
#         email = request.json.get('email')
#         password = request.json.get('password')
#         return RestaurantService.login_restaurant(email, password)
#
#
# @API.route('/auth/logout', strict_slashes=False)
# class RestaurantLogoutController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def post(self):
#         auth_token = RESTAURANT_TOKEN_AUTH.get_auth().get('token')
#         return RestaurantService.logout_restaurant(auth_token)
#
#
# @API.route('/', strict_slashes=False)
# class RestaurantController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return RestaurantService.get_restaurant(restaurant_id)
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def put(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         data = request.json
#         return RestaurantService.update(
#             restaurant_id,
#             email=data.get('email'),
#             password=data.get('password'),
#             name=data.get('name'),
#             description=data.get('description'),
#             street_address=data.get('street_address'),
#             unit_number=data.get('unit_number'),
#             country=data.get('country'),
#             postal_code=data.get('postal_code')
#
#         )
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def delete(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return RestaurantService.delete(restaurant_id)
#
#
# @API.route('/queue/<string:queue_id>', strict_slashes=False)
# class RestaurantQueueController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self, queue_id):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.get_queue_for_restaurant(restaurant_id, queue_id)
#
#
# @API.route('/queue/all', strict_slashes=False)
# class RestaurantQueueAllController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.get_queues_for_restaurant(restaurant_id)
#
#
# @API.route('/queue/create', strict_slashes=False)
# class RestaurantQueueCreatedController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.get_queues_for_restaurant(restaurant_id, states=(QueueState.CREATED,))
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def post(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.create_queue(restaurant_id)
#
#
# @API.route('/queue/pend', strict_slashes=False)
# class RestaurantQueuePendingController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.get_queues_for_restaurant(restaurant_id, states=(QueueState.PENDING,))
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def post(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         queue_id = request.json.get('queue_id')
#         start_time = datetime.datetime.utcnow()
#         return QueueService.to_pend(restaurant_id, queue_id, start_time)
#
#
# @API.route('/queue/wait', strict_slashes=False)
# class RestaurantQueueWaitingController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.get_queues_for_restaurant(restaurant_id, states=(QueueState.WAITING,))
#
#
# @API.route('/queue/buzz', strict_slashes=False)
# class RestaurantQueueBuzzingController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.get_queues_for_restaurant(restaurant_id, states=(QueueState.BUZZING,))
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def post(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         queue_id = request.json.get('queue_id')
#         return QueueService.to_buzz(restaurant_id, queue_id)
#
#
# @API.route('/queue/complete', strict_slashes=False)
# class RestaurantQueueCompletedController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return QueueService.get_queues_for_restaurant(restaurant_id, states=(QueueState.COMPLETED,))
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def post(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         queue_id = request.json.get('queue_id')
#         end_time = datetime.datetime.utcnow()
#         return QueueService.to_complete(restaurant_id, queue_id, end_time)
#
#
# @API.route('/deal', strict_slashes=False)
# class RestaurantDealController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def get(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return DealService.get_deals_for_restaurant(restaurant_id)
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def post(self):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         title = request.form.get('title')
#         description = request.form.get('description')
#         image_file = request.files.get('image')
#         if image_file:
#             filename = image_file.filename
#             filepath = os.path.join(IMAGE_DIR, filename)
#             image_file.save(filepath)
#             return DealService.new_deal(restaurant_id, title, description, filepath)
#         return DealService.new_deal(restaurant_id, title, description)
#
#
# @API.route('/deal/<string:deal_id>', strict_slashes=False)
# class RestaurantDealController(Resource):
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def delete(self, deal_id):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         return DealService.delete_deal(restaurant_id, deal_id)
#
#     @RESTAURANT_TOKEN_AUTH.login_required
#     def put(self, deal_id):
#         restaurant_id = RESTAURANT_TOKEN_AUTH.current_user()
#         title = request.form.get('title')
#         description = request.form.get('description')
#         image_file = request.files.get('image')
#         if image_file:
#             filename = image_file.filename
#             filepath = os.path.join(IMAGE_DIR, filename)
#             image_file.save(filepath)
#             return DealService.update_deal(
#                 restaurant_id,
#                 deal_id,
#                 title=title,
#                 description=description,
#                 image_path=filepath
#             )
#         return DealService.update_deal(
#             restaurant_id,
#             deal_id,
#             title=title,
#             description=description,
#         )
