from scipy.stats import sem
import matplotlib.pyplot as plt
import pandas as pd


def autolabel(rects,ax):
    """
    Attach a text label near the axis of each bar displaying its height
    """
    (y_bottom,y_top) = ax.get_ylim()
    y_scale=(y_top-y_bottom)/10
    for rect in rects:
        height = rect.get_height()
        y_loc=(height*y_scale)/abs(height)
        x_loc=rect.get_x() + rect.get_width()/2.
        ax.text(x_loc, y_loc,'%d' % int(height)+'%',ha='center' ,va='bottom',color='white')
