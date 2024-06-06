#!/usr/bin/env python3


from uvicorn import Config as UvicornConfig, Server


# Запуск Uvicorn
config = UvicornConfig("src.main:app", host="127.0.5.9", port=52608, reload=True)
server = Server(config)

if __name__ == "__main__":
    server.run()
