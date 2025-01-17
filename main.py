import pygame
from block import Block

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Colour Drop")
clock = pygame.time.Clock()
running = True

my_sprites = pygame.sprite.Group()




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            new_block = Block(pygame.mouse.get_pos())
            my_sprites.add(new_block)

    for blk in my_sprites:

        my_sprites.remove(blk)
        touched_blocks = pygame.sprite.spritecollide(blk, my_sprites, False)
    
        # blk.blocks_above = []
        blk.blocks_below = []
        # if touched_blocks != 0:
        #     for i in touched_blocks:
        #         if i.rect.bottom < blk.rect.bottom:
        #             blk.blocks_above.append(i)
        #         else:
        #             blk.blocks_below.append(i)
        if touched_blocks != 0:
            for i in touched_blocks:
                if i.rect.bottom > blk.rect.bottom:
                    blk.blocks_below.append(i)

        if len(blk.blocks_below) != 0:
            blk.moving = False
        else:
            blk.moving = True

        my_sprites.add(blk)

    my_sprites.update()
    screen.fill((255,255,255))
    my_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

