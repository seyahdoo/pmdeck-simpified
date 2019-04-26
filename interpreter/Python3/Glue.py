
import sys


def on_event_received(event):

    try:
        if event == "initialize":
            on_initialize()
        if event == "on_pressed":
            on_pressed()
        if event == "on_released":
            on_released()
        if event == "on_update":
            on_update()
        if event == "on_exit":
            on_exit()
            sys.exit(0)
    except:
        pass
    return


def set_image_base64(image_string):
    print("SETIMAGE:" + image_string + "\n")
    sys.stdout.flush()
    return


if __name__ == "__main__":

    # os.chdir(os.path.dirname(sys.argv[0]))

    while True:
        line = sys.stdin.readline()
        line = line.rstrip("\n")
        on_event_received(line)

