import pygame as pg


pg.init()
FONT = pg.font.Font(None, 42)


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    password = ''

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    # Do something with the password and reset it.
                    print(password)  # I just print it to see if it works.
                    password = ''
                else:  # Add the character to the password string.
                    password += event.unicode

        screen.fill((30, 30, 30))
        # Render the asterisks and blit them.
        password_surface = FONT.render('*'*len(password), True, (70, 200, 150))
        screen.blit(password_surface, (30, 30))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()