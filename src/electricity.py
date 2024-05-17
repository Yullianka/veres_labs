import math
def calculate_rope(distance, height_of_the_pillars):
 
    current_top = 0
    current_bottom = 0
    current_height = 0

    for pillar in height_of_the_pillars:

        if current_height != 0:

            temp_up_down = current_top + math.sqrt(distance ** 2 + (current_height - 1) ** 2)
            temp_down_down = current_bottom + distance
            temp_up_up = current_top + math.sqrt(distance ** 2 + (abs(current_height - pillar)) ** 2)
            temp_down_up = current_bottom + math.sqrt(distance ** 2 + (pillar - 1) ** 2)
            current_top = max(temp_up_up, temp_down_up)
            current_bottom = max(temp_up_down, temp_down_down)
        current_height = pillar

    return round(max(current_bottom, current_top),2)

def read_input(filename):
    with open(filename, 'r') as file:
        w = int(file.readline())
        heights = list(map(int, file.readline().split()))
    return w, heights

def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


input_filename = "../test/resources/electricity.in.txt"
output_filename = "../test/resources/electricity.out.txt"


distance, height_of_the_pillars = read_input(input_filename)

result = round(calculate_rope(distance, height_of_the_pillars), 2)

write_output(output_filename, result)
