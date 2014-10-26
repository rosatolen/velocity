import web
import view


def main():
    urls = (
        '/', 'view.Home',
        '/create/reward', 'view.CreateReward',
        '/create/task/snail', 'view.CreateSnailTask',
        '/create/task/quail', 'view.CreateQuailTask',
    )
    app = web.application(urls, globals())
    app.run()


if __name__ == "__main__":
    main()
