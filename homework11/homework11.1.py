def count_points(win, draw, loss):
    win_points = win * 3
    draw_points = draw * 1
    loss_points = loss * 0
    points = win_points + draw_points + loss_points
    print('All points of a team is: ' + str(points))
count_points(3, 2, 2)