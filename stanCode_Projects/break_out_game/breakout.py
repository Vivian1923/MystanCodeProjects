"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if num_lives > 0:
            # Update
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            # Check not out of frame
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
                graphics.set_dx()
            if graphics.ball.y <= 0:
                graphics.set_dy()
            if graphics.ball.y > graphics.window.height:
                num_lives -= 1
                pause(FRAME_RATE*50)
                graphics.set_dx0()
                graphics.set_dy0()
                graphics.door_is_close = False
                if num_lives != 0:
                    graphics.put_new_ball()
            # Check if there is brick
            maybe_brick1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            maybe_brick2 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y)
            maybe_brick3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_radius)
            maybe_brick4 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius,
                                                         graphics.ball.y + 2 * graphics.ball_radius)
            if maybe_brick1 is not None:
                if maybe_brick1 is graphics.paddle:
                    if graphics.get_dy() > 0:
                        graphics.set_dy()
                else:
                    graphics.set_dy()
                    graphics.window.remove(maybe_brick1)
                    graphics.count_bricks -= 1
            elif maybe_brick2 is not None:
                if maybe_brick2 is graphics.paddle:
                    if graphics.get_dy() > 0:
                        graphics.set_dy()
                else:
                    graphics.set_dy()
                    graphics.window.remove(maybe_brick2)
                    graphics.count_bricks -= 1
            elif maybe_brick3 is not None:
                if maybe_brick3 is graphics.paddle:  # 多問條件
                    if graphics.get_dy() > 0:
                        graphics.set_dy()
                else:
                    graphics.set_dy()
                    graphics.window.remove(maybe_brick3)
                    graphics.count_bricks -= 1
            elif maybe_brick4 is not None:
                if maybe_brick4 is graphics.paddle:
                    if graphics.get_dy() > 0:
                        graphics.set_dy()
                else:
                    graphics.set_dy()
                    graphics.window.remove(maybe_brick4)
                    graphics.count_bricks -= 1
            # Pause
            pause(FRAME_RATE)
        else:
            break
        if graphics.count_bricks == 0:
            break

if __name__ == '__main__':
    main()
