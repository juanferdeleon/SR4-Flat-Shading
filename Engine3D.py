'''
        SR3 Obj Models

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Engine 3D

'''

from gl import Bitmap

bmp = Bitmap(800, 800)

def glInit():
    return bmp


if __name__ == '__main__':
    '''Main Program'''

    #Initialize bmp Object
    bmp = glInit()

    #Set all pixels to same color
    bmp.glClear()

    #Set pixel Colors
    bmp.glColor(1, 1, 0)

    bmp.glLoadObjModel('cube.obj', (0.5, 0.5), (0.5, 0.5))
    
    #Output BMP
    bmp.glWrite("test.bmp")
