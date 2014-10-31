import web
import view
from model.task import SnailTask


def main():
    urls = (
        '/', 'view.Home',
        '/create/reward', 'view.CreateReward',
        '/create/task/snail', 'view.CreateSnailTask',
        '/create/task/quail', 'view.CreateQuailTask',
        '/create/task/watermelon', 'view.CreateWatermelonTask',
        '/complete/task/(.+)', 'view.CompleteTask',
        '/purchase/(.+)', 'view.PurchaseReward',
    )
    app = web.application(urls, globals())
    app.run()

if __name__ == "__main__":
    main()
