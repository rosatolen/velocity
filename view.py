import web
import view

def main():
  urls = (
    '/', 'view.Home'
  )
  app = web.application(urls, globals())
  app.run()

if __name__ == "__main__":
  main()
