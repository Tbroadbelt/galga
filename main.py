spacePlane = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . 9 9 9 . . . . . .
    . . . . . . 9 9 9 9 9 . . . . .
    . . . 7 7 7 9 9 9 9 9 7 7 7 . .
    . . . 7 7 7 7 7 7 7 7 7 7 7 . .
    . . . . 7 7 2 7 2 7 2 7 7 . . .
    . . . . . . 7 7 7 7 7 . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), SpriteKind.player)
spacePlane.set_stay_in_screen(True)
info.set_life(3)
controller.move_sprite(spacePlane, 200, 200)
def on_a_pressed():
    dart = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . 2 2 2 2 . . .
        . . . . . . . 2 2 1 1 1 1 2 . .
        . . . . 2 2 3 3 1 1 1 1 1 1 . .
        . . 3 3 3 3 1 1 1 1 1 1 1 1 . .
        . . 1 1 1 1 1 1 1 1 1 1 1 1 . .
        . . 3 3 2 2 3 1 1 1 1 1 1 1 . .
        . . . . . . 2 2 3 1 1 1 1 2 . .
        . . . . . . . . . 2 2 2 2 . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
        spacePlane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
def on_update_interval():
    bogey = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . 2 2 . . .
        . . . . . . . . . f f f f 5 . .
        . . . . . . . . . 2 4 2 2 . . .
        . . . . . . . . . 2 4 2 . . . .
        . . . . . . 2 2 2 2 4 2 . . . .
        . . . . . 2 2 9 9 4 2 2 . . . .
        . . . . . 2 2 9 9 4 2 2 . . . .
        . . . . . . 2 2 2 2 4 2 . . . .
        . . . . . . . . . 2 4 2 . . . .
        . . . . . . . . . 2 4 2 2 . . .
        . . . . . . . . . f f f f 5 . .
        . . . . . . . . . . . 2 2 . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
        SpriteKind.enemy)
    bogey.set_velocity(-100,0)
    bogey.left = scene.screen_width()
    bogey.y = randint(0, scene.screen_height())
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)     
game.on_update_interval(500, on_update_interval)
def on_on_overlap(sprite, OtherSprite):
    OtherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)
def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)                   