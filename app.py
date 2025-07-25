import signal
import sys
import threading
from typing import List, Callable, Tuple

from flask import Flask

from controlers.base_controller import BaseController
from controlers.game_controller import GameController
from controlers.home_controller import HomeController
from controlers.map_controller import MapController
from controlers.summary_controller import SummaryController
from models.data_container import DataContainer
from models.ssh_keys import SshKeys
from utils.cookies.cookies_manager import CookiesManager
from utils.ssh_keys_reader import SshKeysReader


class App:
    DATA_CONTAINER_FILE_PATH = r'./data/data.json'
    HOST = '192.168.1.100'
    PORT_HTTP = 8080
    PORT_HTTPS = 8443

    CERTIFICATE = r'./security/192.168.1.100.pem'
    CERTIFICATE_KEY = r'./security/192.168.1.100-key.pem'
    KEYS_FILE_PATH = r'./security/flask_key.ppk'

    def __init__(self):
        self._app = Flask(__name__)
        self._app.secret_key = self._get_keys().private_key
        self._setup_signal_handlers()
        self._cookies_manager = CookiesManager()
        self._data = self._init_data()
        self._controllers = self._init_controllers()
        self._register_plugins()

    def _get_ssl_context(self) -> Tuple[str, str]:
        return self.CERTIFICATE, self.CERTIFICATE_KEY

    def _get_keys(self) -> SshKeys:
        return SshKeysReader.read_ssh_private_key(self.KEYS_FILE_PATH)

    def _setup_signal_handlers(self):
        def handle_exit(signum, frame):
            self.cleanup()
            sys.exit(0)

        signal.signal(signal.SIGINT, handle_exit)   # Ctrl+C
        signal.signal(signal.SIGTERM, handle_exit)  # Kill

    def _init_data(self) -> DataContainer:
        try:
            data_container = DataContainer.load_from_file(self.DATA_CONTAINER_FILE_PATH)
        except Exception as e:
            print(f'[!] Could not load previous games state.\n{str(e)}')
            data_container = DataContainer()
        return data_container

    def _init_controllers(self) -> List[BaseController]:
        return [
            HomeController(self._cookies_manager, self._data),
            GameController(self._cookies_manager, self._data),
            MapController(self._cookies_manager, self._data),
            SummaryController(self._cookies_manager, self._data)
        ]

    def _register_plugins(self):
        for controller in self._controllers:
            self._app.register_blueprint(controller.blueprint)

    def _start(self, host: str, port: int, debug: bool, secure: bool = False):
        ssl_context = self._get_ssl_context() if secure else None

        self._app.run(
            host=host,
            port=port,
            debug=debug,
            ssl_context=ssl_context
        )

    @staticmethod
    def _start_threaded(start_method: Callable, *args, **kwargs):
        threading.Thread(target=start_method, args=args, kwargs=kwargs).start()

    def start_http(self, debug: bool = False, multithreading: bool = False):
        if multithreading:
            self._start_threaded(self._start, self.HOST, self.PORT_HTTP, False, False)
        else:
            self._start(self.HOST, self.PORT_HTTP, debug, False)

    def start_https(self, debug: bool = False, multithreading: bool = False):
        if multithreading:
            self._start_threaded(self._start, self.HOST, self.PORT_HTTPS, False, True)
        else:
            self._start(self.HOST, self.PORT_HTTPS, debug, True)

    def cleanup(self):
        print('Closing the application. Saving data...')
        self._data.save_to_file(self.DATA_CONTAINER_FILE_PATH)

if __name__ == '__main__':
    app = App()

    try:
        app.start_https(debug=True, multithreading=False)
    except KeyboardInterrupt:
        app.cleanup()
    except Exception as e:
        print(f'An error occurred: {e}')
        # app.cleanup()
