let spacePlane = sprites.create(img`
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
`, SpriteKind.Player)
spacePlane.setStayInScreen(true)
info.setLife(3)
controller.moveSprite(spacePlane, 200, 200)
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    let dart = sprites.createProjectileFromSprite(img`
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
    `, spacePlane, 200, 0)
})
game.onUpdateInterval(500, function on_update_interval() {
    let bogey = sprites.create(img`
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
    `, SpriteKind.Enemy)
    bogey.setVelocity(-100, 0)
    bogey.left = scene.screenWidth()
    bogey.y = randint(0, scene.screenHeight())
    bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, OtherSprite: Sprite) {
    OtherSprite.destroy()
    info.changeLifeBy(-1)
})
