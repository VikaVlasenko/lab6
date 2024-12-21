import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Функция для создания буквы "V"
def create_letter_V():
    vertices = np.array([
        [0, 0, 0],  # Вершина 1
        [1, 1, 0],  # Вершина 2
        [2, 0, 0],  # Вершина 3
        [1, 1, 1],  # Вершина 4
        [2, 0, 1],  # Вершина 5
        [0, 0, 1]   # Вершина 6
    ])
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0],  # Основание
        [0, 3], [1, 4], [2, 5]  # Вертикальные рёбра
    ]
    return vertices, edges

# Функция для визуализации трехмерного объекта
def plot_3d_object(ax, vertices, edges):
    edge_vertices = np.array([vertices[edge] for edge in edges])
    line_segments = Line3DCollection(edge_vertices, colors='b')
    ax.add_collection(line_segments)
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

# Функция для построения ортографических проекций
def plot_orthographic_projections(ax, vertices):
    ax[0].scatter(vertices[:, 0], vertices[:, 1], color='r')
    ax[0].set_title('Oxy')
    ax[0].set_xlabel('X')
    ax[0].set_ylabel('Y')
    ax[0].set_xlim([-2, 2])
    ax[0].set_ylim([-2, 2])

    ax[1].scatter(vertices[:, 0], vertices[:, 2], color='g')
    ax[1].set_title('Oxz')
    ax[1].set_xlabel('X')
    ax[1].set_ylabel('Z')
    ax[1].set_xlim([-2, 2])
    ax[1].set_ylim([-2, 2])

    ax[2].scatter(vertices[:, 1], vertices[:, 2], color='b')
    ax[2].set_title('Oyz')
    ax[2].set_xlabel('Y')
    ax[2].set_ylabel('Z')
    ax[2].set_xlim([-2, 2])
    ax[2].set_ylim([-2, 2])

# Функции для преобразований
def scale(vertices, sx, sy, sz):
    scale_matrix = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    vertices_hom = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    transformed = (scale_matrix @ vertices_hom.T).T[:, :3]
    return transformed

def translate(vertices, tx, ty, tz):
    translate_matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    vertices_hom = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    transformed = (translate_matrix @ vertices_hom.T).T[:, :3]
    return transformed

def rotate_around_axis(vertices, axis='x', angle=0):
    if axis == 'x':
        rotation_matrix = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle), -np.sin(angle), 0],
            [0, np.sin(angle), np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'y':
        rotation_matrix = np.array([
            [np.cos(angle), 0, np.sin(angle), 0],
            [0, 1, 0, 0],
            [-np.sin(angle), 0, np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'z':
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle), 0, 0],
            [np.sin(angle), np.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    vertices_hom = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    transformed = (rotation_matrix @ vertices_hom.T).T[:, :3]
    return transformed

# Основная функция
def main():
    vertices, edges = create_letter_V()

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)
    ax3 = fig.add_subplot(122)
    ax4 = fig.add_subplot(122)

    # Визуализация исходного объекта
    plot_3d_object(ax1, vertices, edges)

    # Пример преобразований
    vertices = scale(vertices, 1.5, 1.5, 1.5)  # Масштабирование
    vertices = translate(vertices, 0.5, 0.5, 0.5)  # Перенос
    vertices = rotate_around_axis(vertices, axis='x', angle=np.pi / 4)  # Вращение вокруг оси X

    # Визуализация преобразованного объекта
    plot_3d_object(ax1, vertices, edges)

    # Ортографические проекции
    plot_orthographic_projections([ax2, ax3, ax4], vertices)

    plt.show()

if __name__ == "__main__":
    main()