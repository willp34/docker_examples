import time

##import redis
from flask import Flask
from fask_restful import Resourse, Api


app = Flask(__name__)

api = Api(app)

class Product(Resourse):
	def get(self);
	
	return {
			'products' : ['Ice Cream' , 'Chocolate']
	}
##cache = redis.Redis(host='redis', port=6379)


# def get_hit_count():
    # retries = 5
    # while True:
        # try:
            # return cache.incr('hits')
        # except redis.exceptions.ConnectionError as exc:
            # if retries == 0:
                # raise exc
            # retries -= 1
            # time.sleep(0.5)


# @app.route('/')
# def hello():
    # count = get_hit_count()
    # return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True)