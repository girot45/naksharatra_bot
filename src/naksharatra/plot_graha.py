# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as transforms
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from settings.nakshatra_settings.schemas import AstroObject

def plot_object(
        ax,
        drawing_origin,
        astro_object: AstroObject,

):
    image = plt.imread(astro_object.image_path)
    imagebox = OffsetImage(image, zoom=astro_object.zoom * astro_object.radius)
    ab = AnnotationBbox(
        imagebox, (0, 0),
        xybox=drawing_origin,
        xycoords='data',
        frameon=False
    )
    ax.add_artist(ab)




def plot_moon_phase(day,drawing_origin,radius,fig,ax):


    image_path = "resources/img/moon.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius )
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    return 0


def plot_sun(drawing_origin,radius,fig,ax):

    image_path = "resources/img/sun.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius * 2)
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    
    return 0

def plot_inner_graha_phase(graha,drawing_origin,radius,ax):
    
    if (graha == "mercuri"):
        image_path = "resources/img/mercuri.png"

    elif (graha == "venus"):
        image_path = "resources/img/venus.png"

    else:
        print("That is not an inner graha! Use the outer graha function to plot ",graha)
        return
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius * 2)
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    return 0

def plot_outer_graha(graha,drawing_origin,radius,fig,ax):
    
    if (graha == "mars"):
        image_path = "resources/img/mars.png"
    elif (graha == "jupiter"):
        image_path = "resources/img/jupiter.png"
    elif (graha == "saturn"):
        image_path = "resources/img/saturn.png"
    else:
        print("That is not an outer graha! Use the inner graha function to plot",graha)
        return

    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius * 2)
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    return 0

def plot_rahu(drawing_origin,scale,fig,ax):
    

    # Загрузка изображения
    image_path = "resources/img/rahu.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=0.1)

    # Добавляем смещение
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)
    ax.add_artist(ab)

    return 0

def plot_ketu(drawing_origin,scale,fig,ax):


    image_path = "resources/img/ketu.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=0.1)

    # Добавляем смещение
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)
    ax.add_artist(ab)
    return 0
