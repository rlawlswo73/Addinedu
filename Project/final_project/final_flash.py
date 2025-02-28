import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib.request
from PyQt5 import uic
import numpy as np
import heapq
import numpy as np
import time

# ui
from_class = uic.loadUiType("/home/kjj73/dev_ws/Project/final_project/final_flash.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Final Flash!!")

        self.map_width, self.map_height = 950, 600
        self.grid_width, self.grid_height = 10, 10
        self.base_map.setFixedSize(self.map_width, self.map_height)
        self.grid_map.setFixedSize(self.map_width, self.map_height)
        self.basePixmap = QPixmap(self.base_map.width(), self.base_map.height())
        self.gridPixmap = QPixmap(self.base_map.width(), self.base_map.height())
        self.basePixmap.fill(Qt.white)
        self.gridPixmap.fill(Qt.transparent)

        self.base_map.setPixmap(self.basePixmap)
        self.grid_map.setPixmap(self.gridPixmap)

        self.mouse_x, self.mouse_y = None, None
        self.drawGrid()

        self.collision_area = np.zeros((int(self.map_width/self.grid_width), int(self.map_height/self.grid_height)), dtype=np.int32)
        # self.collision_outline = np.zeros((int(self.map_width/self.grid_width), int(self.map_height/self.grid_height)), dtype=np.int32)
        self.collision_list = []
        self.startPoint = [None, None]
        self.endPoint = [None, None]

        self.mapCreatebtn.clicked.connect(self.createMap)
        self.mapClear.clicked.connect(self.clearMap)
        self.fillCollision.clicked.connect(self.collisionFill)
        self.moveAction.clicked.connect(self.moveStart)

    def drawPath(self):
        path_painter = QPainter(self.grid_map.pixmap())
        if self.path != None:
            for i in self.path:
                path_painter.setPen(QPen(Qt.yellow, 1, Qt.SolidLine))
                path_painter.setBrush(QBrush(Qt.yellow))
                path_painter.drawRect((int(i[0])*self.grid_width + 1), (int(i[1])*self.grid_height + 1), 8, 8)
                self.update()
                # time.sleep(0.125)

        path_painter.setPen(QPen(Qt.green, 1, Qt.SolidLine))
        path_painter.setBrush(QBrush(Qt.green))
        path_painter.drawRect((self.startPoint[0]*self.grid_width + 1), (self.startPoint[1]*self.grid_height + 1), 8, 8)

        path_painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        path_painter.setBrush(QBrush(Qt.blue))
        path_painter.drawRect((self.endPoint[0]*self.grid_width + 1), (self.endPoint[1]*self.grid_height + 1), 8, 8)
        self.update()
        path_painter.end()
        pass

    def moveStart(self):
        self.startPoint[0] = int(self.x_StartPoint.text())
        self.startPoint[1] = int(self.y_StartPoint.text())

        self.endPoint[0] = int(self.x_EndPoint.text())
        self.endPoint[1] = int(self.y_EndPoint.text())

        point_painter = QPainter(self.grid_map.pixmap())
        
        if self.startPoint[0] != "" and self.startPoint[1] != "":
            point_painter.setPen(QPen(Qt.green, 1, Qt.SolidLine))
            point_painter.setBrush(QBrush(Qt.green))
            point_painter.drawRect((int(self.startPoint[0])*self.grid_width + 1), (int(self.startPoint[1])*self.grid_height + 1), 8, 8)

        if self.endPoint[0] != "" and self.endPoint[1] != "":
            point_painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
            point_painter.setBrush(QBrush(Qt.blue))
            point_painter.drawRect((self.endPoint[0]*self.grid_width + 1), (self.endPoint[1]*self.grid_height + 1), 8, 8)

        self.update()
        point_painter.end()

        start = (self.startPoint[0], self.startPoint[1])
        goal = (self.endPoint[0], self.endPoint[1])
        grid = self.collision_area

        self.path = self.astar(grid, start, goal)
        # print("경로:", self.path)
            # print(i[0], i[1])
        self.drawPath()

    # 지금 당장 쓰는 함수가 아님
    def collisionFill(self):
        for i in range(self.collision_area.shape[0]):
            for j in range(self.collision_area.shape[1]):
                if self.collision_area[i][j] == 255:
                    # 일단 필요가 없으니 pass (관련변수 self.collision_outline)
                    pass

    def clearMap(self):
        self.path = []
        self.startPoint = [None, None]
        self.endPoint = [None, None]
        # print(self.collision_list)
        self.collision_list = []
        self.collision_area.fill(0)
        # self.collision_outline.fill(0)
        self.base_map.pixmap().fill(Qt.white)
        self.grid_map.pixmap().fill(Qt.transparent)
        self.drawGrid()
        self.update()

    def createMap(self):
        for i in range(len(self.collision_list)):
            if (self.collision_list[i][0] > 0 and self.collision_list[i][1] > 0 and (self.collision_list[i][0] // self.grid_width) < self.collision_area.shape[0] and (self.collision_list[i][1] // self.grid_height) < self.collision_area.shape[1]):
                # print(self.collision_list[i][0]  // self.grid_width, int(self.collision_area.shape[0]))
                self.collision_area[int(self.collision_list[i][0]  // self.grid_width), int(self.collision_list[i][1] // self.grid_height)] = 255

        collision_painter = QPainter(self.grid_map.pixmap())
        collision_painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        collision_painter.setBrush(QBrush(Qt.black))

        for i in range(0, int(self.collision_area.shape[0])):
            for j in range(0, int(self.collision_area.shape[1])):
                if(self.collision_area[i][j] == 255):
                    collision_painter.drawRect((i*self.grid_width) + 1, (j*self.grid_height) + 1, 8, 8)

                    # collision_painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
                    # collision_painter.drawLine((i*self.grid_width), (j*self.grid_height+1), i, self.map_height)
                    # print(i,j,(i*self.grid_width)+1, (j*self.grid_height+1))
                    # print(i,j,"!!!")
                    self.update()
                # pass
        # print("Pixmap size:", self.grid_map.pixmap().size())
        # print("Grid map size:", self.grid_map.size())
        collision_painter.end()

    def drawGrid(self):
        grid_painter = QPainter(self.grid_map.pixmap())
        grid_painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))

        for i in range(10, self.map_width, self.grid_width):
            grid_painter.drawLine(i, 0, i, self.map_height)
        for i in range(10, self.map_height, self.grid_height):
            grid_painter.drawLine(0, i, self.map_width, i)

        grid_painter.end()

    def mouseMoveEvent(self, event):
        if self.mouse_x is None:
            self.mouse_x = event.x()
            self.mouse_y = event.y()
            return
        
        painter = QPainter(self.base_map.pixmap())
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        painter.drawLine(self.mouse_x - self.base_map.x(), self.mouse_y - self.base_map.y(), event.x() - self.base_map.x(), event.y() - self.base_map.y())
        painter.end()
        self.update()

        self.mouse_x = event.x()
        self.mouse_y = event.y()

        self.collision_list.append([self.mouse_x - self.base_map.x(), self.mouse_y - self.base_map.y()])
        # print([self.mouse_x, self.mouse_y])

    def mouseReleaseEvent(self, event):
        self.mouse_x = None 
        self.mouse_y = None

    # A* 알고리즘 구현
    def astar(self, grid, start, goal):
        # 이동할 수 있는 방향 (상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Manhattan Distance 휴리스틱 함수 (목표까지의 예상 거리)
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # 오픈 리스트: (f_score, (x, y)) 형태로 저장
        open_list = []
        heapq.heappush(open_list, (0, start))
        
        # 각 노드에 대해 f, g, h 값 저장
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}
        
        # 경로를 추적할 부모 노드
        came_from = {}
        
        while open_list:
            _, current = heapq.heappop(open_list)
            
            # 목표 지점에 도달하면 경로를 반환
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]  # 역순으로 경로 반환
            
            # 현재 노드에서 갈 수 있는 이웃 탐색
            for direction in directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                
                # 이웃이 경계 내에 있고, 장애물이 아니어야 함
                if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])) and grid[neighbor[0]][neighbor[1]] != 255:
                    tentative_g_score = g_score[current] + 1  # 이동 비용 (상, 하, 좌, 우는 동일하게 1로 설정)
                    
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                        heapq.heappush(open_list, (f_score[neighbor], neighbor))
        
        return None  # 경로가 없으면 None 반환

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())