def calculate_length_and_drop(i, j):
    global max_len, max_drop, row, col, data_grid
    item = data_grid[i][j]
    length_increase = 0
    drop_increase = 0
    increased_by = False

    if i > 0:
        up = data_grid[i - 1][j]
        if up.get('value') < item.get('value'):
            if not up.get('visited'):
                calculate_length_and_drop(i - 1, j)
            if up.get('length') > length_increase:
                length_increase = up.get('length')
                drop_increase = up.get('drop')
                increased_by = up
            if up.get('length') == length_increase and up.get('drop') == drop_increase:
                drop_increase = up.get('drop')
                increased_by = up

    if i < row - 1:
        down = data_grid[i + 1][j]
        if down.get('value') < item.get('value'):
            if not down.get('visited'):
                calculate_length_and_drop(i + 1, j)
            if down.get('length') > length_increase:
                length_increase = down.get('length')
                drop_increase = down.get('drop')
                increased_by = down
            if down.get('length') == length_increase and down.get('drop') == drop_increase:
                drop_increase = down.get('drop')
                increased_by = down

    if j > 0:
        left = data_grid[i][j - 1]
        if left.get('value') < item.get('value'):
            if not left.get('visited'):
                calculate_length_and_drop(i, j - 1)
            if left.get('length') > length_increase:
                length_increase = left.get('length')
                drop_increase = left.get('drop')
                increased_by = left
            if left.get('length') == length_increase and left.get('drop') == drop_increase:
                drop_increase = left.get('drop')
                increased_by = left

    if j < col - 1:
        right = data_grid[i][j + 1]
        if right.get('value') < item.get('value'):
            if not right.get('visited'):
                calculate_length_and_drop(i, j + 1)
            if right.get('length') > length_increase:
                length_increase = right.get('length')
                drop_increase = right.get('drop')
                increased_by = right
            if right.get('length') == length_increase and right.get('drop') == drop_increase:
                drop_increase = right.get('drop')
                increased_by = right

    if increased_by:
        item['length'] = length_increase + 1
        item['drop'] = drop_increase + item.get('value') - increased_by.get('value')
        if item.get('length') > max_len or (item.get('length') == max_len and item.get('drop') > max_drop):
            max_len = item.get('length')
            max_drop = item.get('drop')

    item['visited'] = True


handle = open('map.txt', 'r')
lines = handle.readlines()
row, col = [int(v) for v in lines[0].split()]
max_len = 0
max_drop = 0
data_grid = [[{'value': int(v), 'visited': False, 'length': 1, 'drop': 0} for v in line.split()] for line in lines[1:]]

for r_i in range(row):
    for c_i in range(col):
        calculate_length_and_drop(r_i, c_i)
print 'Max Length: ' + str(max_len) + ' Max Drop: ' + str(max_drop)
