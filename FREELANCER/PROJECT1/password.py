from itertools import permutations
import math
# Please use "pip install matplotlib" or "pip3 install matplotlib" to install matplotlib 
import matplotlib.pyplot as plt 

class password():
    def __init__(self, rule):
        self.rule = rule
        # Longest distance
        self.longest_length = 0.0
        # List of longest path. The longest path is not unique. 
        self.longest_path = []
        # You may define some other useful global variables here. 
        # Your code goes here:






    # Position of each point. For example, the value positions["1"] is a tuple (0,0) which is the coordinate of point 1.
    def find_positions(self,i):
        # Your code goes here:
        j=0
        position = (-1,-1)
        for a in range(3):
            for b in range(3):
                j+=1
                if j==int(i):
                    return (b, a)
                    break

        return position

    # Find the longest path
    # Update the distance of the longest path in self.longest_length
    # Push all longest pathes into self.longest_path
    def find_longest_path(self):
        for path in permutations("123456789"):
            path = ''.join(path)
            # Your code goes here:

            #pass rule?
            passesRule = True
            # if self.rule ==1:
                
            # if self.rule ==2:

            positionList = []
            if self.rule==1:
                for i in range(len(path)-1):
                    corners = (path[i] == '1' and (path[i+1]=='3'or path[i+1]=='7' or path[i+1]=='9')) or (path[i] == '3' and (path[i+1]=='1' or path[i+1]=='7' or path[i+1]=='9')) or (path[i] == '7' and (path[i+1]=='3' or path[i+1]=='1' or path[i+1]=='9')) or (path[i] == '9' and (path[i+1]=='3' or path[i+1]=='7' or path[i+1]=='1'))
                    sides = (path[i] == '2' and path[i+1]=='8') or (path[i] == '4' and path[i+1]=='6') or (path[i] == '8' and path[i+1]=='2') or (path[i] == '6' and path[i+1]=='4')
                    # print(corners, sides)
                    passesRule = not (corners or sides) #and rule1
                    if not passesRule:
                        break
            else:
                for i in range(len(path)-1):
                    corners = (path[i] == '1' and ((path[i+1]=='3' and '2' in path[i:])  or (path[i+1]=='7' and '2' in path[i:]) or (path[i+1]=='9'and '5' in path[i:]))) or (path[i] == '3' and ((path[i+1]=='1' and '2' in path[i:]) or (path[i+1]=='7' and '5' in path[i:]) or (path[i+1]=='9' and '6' in path[i:]))) or (path[i] == '7' and ((path[i+1]=='3' and '5' in path[i:])or (path[i+1]=='1' and '4' in path[i:])or (path[i+1]=='9' and '8' in path[i:]))) or (path[i] == '9' and ((path[i+1]=='3' and '6' in path[i:])or (path[i+1]=='7' and '8' in path[i:])or (path[i+1]=='1' and '5' in path[i:])))
                    sides = (path[i] == '2' and (path[i+1]=='8' and '5' in path[i:])) or (path[i] == '4' and (path[i+1]=='6' and '5' in path[i:])) or (path[i] == '8' and (path[i+1]=='2' and '5' in path[i:])) or (path[i] == '6' and (path[i+1]=='4' and '5' in path[i:]))
                    # print(corners, sides)
                    passesRule = not (corners or sides) #and rule1
                    if not passesRule:
                        break
            
            if passesRule:
                for i in range(len(path)):
                    positionList.append(self.find_positions(path[i]))

                currentLength=0.0


            
                for i in range(len(positionList)-1):
                    # horizontal = (positionList[i] == (0,0) and positionList[i+1] == (0,2)) or (positionList[i] == (1, 0) and positionList[i+1] == (1,2)) or (positionList[i] == (2, 0) and positionList[i+1] == (2,2)) or (positionList[i] == (0,2) and positionList[i+1] == (0,0)) or (positionList[i] == (1, 2) and positionList[i+1] == (1,0)) or (positionList[i] == (2, 2) and positionList[i+1] == (2,0))
                    # vertical = (positionList[i] == (0,0) and positionList[i+1] == (2,0)) or (positionList[i] == (0, 1) and positionList[i+1] == (2,1)) or (positionList[i] == (0, 2) and positionList[i+1] == (2,2)) or (positionList[i] == (2,0) and positionList[i+1] == (0,0)) or (positionList[i] == (2, 1) and positionList[i+1] == (0,1)) or (positionList[i] == (2, 2) and positionList[i+1] == (0,2))
                    # diagonal = (positionList[i] == (0,0) and positionList[i+1] == (2,2)) or (positionList[i] == (2,2) and positionList[i+1] == (0,0)) or (positionList[i] == (2,0) and positionList[i+1] == (2,0)) or (positionList[i] == (2,0) and positionList[i+1] == (0,2))
                    # passesRule = not (horizontal and vertical and diagonal)


                    # passesRule = (((positionList[i][0] == positionList[i+1][0] and (positionList[i][1] == positionList[i+1][1]+2 or positionList[i][1] == positionList[i+1][1]-2)) #verticals
                    #     or (positionList[i][1] == positionList[i+1][1] and (positionList[i][0] == positionList[i+1][0]+2 or positionList[i][0] == positionList[i+1][0]-2)) # horizontals
                    #     or ((positionList[i][0] == positionList[i+1][0]+2 and positionList[i][1] == positionList[i+1][1]+2) or (positionList[i][0] == positionList[i+1][0]+2 and positionList[i][1] == positionList[i+1][1]-2) or (positionList[i][0] == positionList[i+1][0]-2 and positionList[i][1] == positionList[i+1][1]+2) or (positionList[i][0] == positionList[i+1][0]-2 and positionList[i][1] == positionList[i+1][1]-2)) # diagonals
                    #     ) and self.rule == 1)
                    #if passesRule:
                    currentLength += self.distance(positionList[i], positionList[i+1]) 
                # print(currentLength)
                #if passesRule:
                if currentLength > self.longest_length:
                    self.longest_path = [path]
                    #print("reset path")
                    self.longest_length = currentLength

                elif currentLength == self.longest_length:
                    self.longest_path.append(path)
        # print(len(self.longest_path))

    
    # Calculate distance between two points
    # Format of point is a tuple (x_value, y_value), for example, (1,2), (0,1)
    def distance(self, point1, point2):
        return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

    # Print and save the result
    def print_result(self):
        print("The longest length using rule " + str(self.rule) + " is:")
        print(self.longest_length)
        print()
        print("All paths with length distance using rule " + str(self.rule) + " is:") 
        print(self.longest_path)
        print()
        with open('results_rule'+str(self.rule)+'.txt', 'w') as file_handler:
            file_handler.write("{}\n".format(self.longest_length)) 
            for path in self.longest_path:
                file_handler.write("{}\n".format(path)) 

    # Verify the result
    def verify(self):
        # true_longest_length[0] and true_longest_path[0] are result of rule 1
        # true_longest_length[1] and true_longest_path[1] are result of rule 2
        # [7*sqrt(5)+sqrt(2), 5*sqrt(2)+3*sqrt(5)+4]
        true_longest_length = [17.066689404871624, 17.779271744364845]
        true_longest_path = [
            ['276183495', '294381675', '438167295', '492761835', '516729438', '518349276', '534927618', '538167294', '572943816', '576183492', '592761834', '594381672', '618349275', '672943815', '816729435', '834927615'],
            ['519283764', '519467382', '537281946', '537649182', '573461928', '573829164', '591643728', '591827346']]

        if abs(self.longest_length - true_longest_length[self.rule - 1]) > 1e-09:
            print(False)
            return 

        if set(self.longest_path) != set(true_longest_path[self.rule - 1]):
            print(False)
            return

        print(True)

    def draw_first_result(self):
        if len(self.longest_path) > 0:
            self.draw_path(self.longest_path[0])

    # Draw one path, where each path is a permutation of string "123456789"
    def draw_path(self, path):
        x, y = [], []
        coordinate = {'1':(0,0),
              '2':(1,0),
              '3':(2,0),
              '4':(0,1),
              '5':(1,1),
              '6':(2,1),
              '7':(0,2),
              '8':(1,2),
              '9':(2,2),
              }
        for i in range(9):
            x.append(coordinate[path[i]][1])
            y.append(coordinate[path[i]][0])

        plt.rcParams.update({'font.size': 20})
        plt.text( 0.05,-0.05,'1')
        plt.text( 1.05,-0.05,'2')
        plt.text( 2.05,-0.05,'3')
        plt.text( 0.05, 0.95,'4')
        plt.text( 1.05, 0.95,'5')
        plt.text( 2.05, 0.95,'6')
        plt.text( 0.05, 1.95,'7')
        plt.text( 1.05, 1.95,'8')
        plt.text( 2.05, 1.95,'9')

        plt.plot(x,y,'r-o')
        plt.axis("off")
        plt.axis('equal')
        plt.savefig("one_result_rule"+str(self.rule)+".png")
        plt.show()

if __name__ == "__main__":

    for rule in range(1,3):
        # Initialize the object using rule 1 or rule 2
        run = password(rule)
        # Find the longest path
        run.find_longest_path()
        # Draw and save the first longest path
        # You may need to close the window of the picture to resume running this code.
        run.draw_first_result()
        # Print and save the result
        run.print_result()
        # Verify the result 
        run.verify()