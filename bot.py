import config

import vk

session = vk.AuthSession(config.APP_ID, config.LOGIN, config.PASSWORD, scope="messages")
vk_api = vk.API(session)


def init_long_poll_server():
    r = vk_api.messages.getLongPollServer(v="5.95")
    server = r["server"]
    key = r["key"]
    ts = r["ts"]
    return server, key, ts


def main():
    print(init_long_poll_server())


if __name__ == '__main__':
    main()
