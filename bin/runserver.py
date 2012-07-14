import os
import sys
import argparse

dir_name = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, dir_name)

from ml_api import create_app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the app using the dev server')
    parser.add_argument('host', default='127.0.0.1', nargs='?',
                        help='IP address or hostname to bind to (default 127.0.0.1)')
    parser.add_argument('port', default=5000, type=int, nargs='?',
                        help='Port number to listen on (default 5000)')
    parser.add_argument('--nodebug', action='store_true',
                        help='Run the app with debug set to false')

    args = parser.parse_args()

    app = create_app(debug=not args.nodebug)
    app.run(host=args.host, port=args.port)
