import threading

from action.Action import Action

if __name__ == "__main__":
    ac = Action("action/example_actions/py3.com.seyahdoo.micmute.zip")

    while threading.active_count() > 0:
        for t in threading.enumerate():
            if t is not threading.current_thread():
                t.join()

    exit(0)
