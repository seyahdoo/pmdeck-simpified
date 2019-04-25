import threading

from action.Action import Action

if __name__ == "__main__":
    ac = Action("action/example_actions/py3.com.seyahdoo.micmute.zip")

    try:
        while threading.active_count() > 0:
            for t in threading.enumerate():
                if t is not threading.current_thread():
                    t.join()
    except (KeyboardInterrupt, SystemExit):
        exit(0)

    exit(0)
