import vtk
import numpy as np


def cell_colorer(origimage, name, cam_rotation, cam_position, focal, film_size, renderer, line_length=1):

    cells = list()

    import cv2
    img = cv2.imread(origimage, cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img, 128, 1, cv2.THRESH_BINARY)
    locs = np.transpose(np.where(thresh1 == 1))

    print('number of points in image: ', locs.shape[0])

    reader = vtk.vtkOBJReader()
    reader.SetFileName(name)
    reader.Update()

    colors = vtk.vtkNamedColors()

    # Initialize all of the cell data colors
    cellData = vtk.vtkUnsignedCharArray()
    cellData.SetNumberOfComponents(3)
    cellData.SetNumberOfTuples(reader.GetOutput().GetNumberOfCells())
    reader.GetOutput().GetCellData().SetScalars(cellData)

    mesh = reader.GetOutput()
    print(mesh.GetNumberOfCells())

    points = mesh.GetPoints()
    dataArray = points.GetData()

    # A lambda to scale the contents of the array x by 255
    def scale(x):
        for h in range(3):
            x[h] = x[h] * 255

    rgb = [0, 0, 0]
    colors.GetColorRGB("Banana", rgb)
    scale(rgb)
    for i in range(cellData.GetNumberOfTuples()):
        cellData.InsertTuple(i, rgb)

    count = 0

    for x, y in locs:
        if count % 1000 == 0:
            print(count)
        count += 1
        # Shifting to middle
        x = x / img.shape[0]
        y = y / img.shape[1]
        x -= 0.5
        y -= 0.5
        x = x * film_size[1]
        y = y * film_size[0]
        x, y = y, x

        loc = np.array([x, y, 0])
        rotation = cam_rotation.reshape((3, 3))
        normal = np.matmul(np.transpose(np.array([0, 0, 1])), rotation)

        rotated = np.matmul(np.transpose(loc), rotation)

        plane_at_cam_pos = rotated + cam_position

        # pn = 0.01 * focal * np.asarray(normal)
        # print('focal: ', focal)
        pn = normal * focal
        # pn = pn + cam_position

        new_loc = plane_at_cam_pos + pn
        # new_loc = cam_position + pn
        delta = new_loc - cam_position
        # line_eq_at_len = cam_position + line_length * delta#[:2]
        line_eq_at_len = cam_position + 100 * delta

        # Create a vtkPoints object and store the points in it
        points = vtk.vtkPoints()
        # points.InsertNextPoint(origin)
        points.InsertNextPoint(cam_position)
        points.InsertNextPoint(line_eq_at_len)

        startRay = cam_position
        endRay = line_eq_at_len

        # Find the cells that intersect the line and color those cells
        cellIds = vtk.vtkIdList()
        locator = vtk.vtkCellLocator()
        locator.SetDataSet(reader.GetOutput())
        locator.BuildLocator()
        locator.FindCellsAlongLine(startRay, endRay, 0.001, cellIds)

        colors.GetColorRGB("Tomato", rgb)
        scale(rgb)
        for i in range(cellIds.GetNumberOfIds()):
            # cellData.InsertTuple(cellIds.GetId(i), rgb)
            # print('cel Id: ', cellIds.GetId(i))#, end='---->')
            cells.append(cellIds.GetId(i))

    # Extract all the cells idenitied as intersection
    print('number of all the cell identified: ', cellIds.GetNumberOfIds())
    print('***************************************************')
    colors.GetColorRGB("Tomato", rgb)
    scale(rgb)

    cellPoints = vtk.vtkPoints()
    point_id_list = list()
    point2 = list()

    unicells = list(set(cells))

    for i in range(len(unicells)):
        cellData.InsertTuple(unicells[i], rgb)

        # cell = mesh.GetCell(i)
        cell = mesh.GetCell(unicells[i])
        points = cell.GetPoints()
        point_ids = cell.GetPointIds()

        for j in range(point_ids.GetNumberOfIds()):
            point_id = point_ids.GetId(j)
            point_id_list.append(point_id)
            cellPoints.InsertNextPoint(mesh.GetPoint(point_id))
            # point = points.GetPoint(point_id)
            # print(point_id)#, point)

        for k in range(points.GetNumberOfPoints()):
            point2.append(points.GetPoint(k))
        # print the points of the cell

    point_list = list()

    for i in range(cellPoints.GetNumberOfPoints()):
        # print(cellPoints.GetPoint(i))
        point_list.append(cellPoints.GetPoint(i))

    print('list of points: ', point_list)
    print()
    uniques = set(point_list)
    # faceIndex = vtk.vtkIdList()
    # reader.GetOutput().GetCellPoints(i, faceIndex)

    import pickle
    with open('output_set2.txt', 'wb') as f:
        pickle.dump(uniques, f)

    with open('output_cells2.txt', 'wb') as f:
        pickle.dump(cells, f)

    # print('total number of cells: ', num_cells)

    # Shrink each cell to make them visible
    shrink = vtk.vtkShrinkFilter()
    shrink.SetInputConnection(reader.GetOutputPort())
    shrink.SetShrinkFactor(0.95)

    # Convert the cells to polydata
    surface = vtk.vtkDataSetSurfaceFilter()
    surface.SetInputConnection(shrink.GetOutputPort())
    surface.SetNonlinearSubdivisionLevel(2)
    surface.Update()

    # Get the output data from the filter
    output = reader.GetOutput()

    # Create a vtkDataSetMapper to map the data to graphics primitives
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputData(output)

    # Create a vtkActor to represent the data in the rendering pipeline
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # add to the renderer
    renderer.AddActor(actor)

    return uniques
