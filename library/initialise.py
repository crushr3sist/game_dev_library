import pygame


def initialise(set_print=bool, quit_func=bool):
    pygame.init()
    ERROR = pygame.get_error()
    SDL_VERSION = pygame.get_sdl_version()
    PYGAME_VERSION = pygame.version.ver

    if set_print == True:
        print(
            f"""
            SDL_VERSION : {SDL_VERSION}\n
            PYGAME_VERSION : {PYGAME_VERSION}\n
            
        """
        )
    else:
        pass
