from library import * 

def main():
    HEIGHT = 800
    WIDTH = 600
    mainloop = MainLoop(WIDTH,HEIGHT,"title", "std")
    rectangle = draw_rectangle(199, 199, 300, 400)
    window= mainloop.window()

    rectangle.draw(window,rectangle)

    mainloop.check_for_events()
    
if __name__ == "__main__":
    main()