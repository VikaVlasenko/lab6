import numpy as np

def scale(vertices, sx, sy, sz):
    scale_matrix = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    homogeneous_vertices = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = np.dot(homogeneous_vertices, scale_matrix.T)
    return transformed_vertices[:, :3]

def translate(vertices, tx, ty, tz):
    translate_matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    homogeneous_vertices = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = np.dot(homogeneous_vertices, translate_matrix.T)
    return transformed_vertices[:, :3]

def rotate_around_axis(vertices, axis='x', angle=0):
    if axis == 'x':
        rotate_matrix = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle), -np.sin(angle), 0],
            [0, np.sin(angle), np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'y':
        rotate_matrix = np.array([
            [np.cos(angle), 0, np.sin(angle), 0],
            [0, 1, 0, 0],
            [-np.sin(angle), 0, np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'z':
        rotate_matrix = np.array([
            [np.cos(angle), -np.sin(angle), 0, 0],
            [np.sin(angle), np.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    else:
        raise ValueError("Invalid axis. Use 'x', 'y', or 'z'.")

    homogeneous_vertices = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed_vertices = np.dot(homogeneous_vertices, rotate_matrix.T)
    return transformed_vertices[:, :3]