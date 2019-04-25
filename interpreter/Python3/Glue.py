
import sys


def on_event_received(event):

    try:
        if event == "initialize":
            initialize()
        if event == "on_pressed":
            on_pressed()
        if event == "on_released":
            on_released()
        if event == "on_update":
            on_update()
        if event == "on_exit":
            on_exit()
    except:
        pass
    return


def set_image(name):
    print(name)
    return


if __name__ == "__main__":

    # os.chdir(os.path.dirname(sys.argv[0]))

    while True:
        line = sys.stdin.readline()
        line = line.rstrip("\n")
        on_event_received(line)

