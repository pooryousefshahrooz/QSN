#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
import matplotlib.pyplot as plt

#import globalsvariables
import glob
import os
import datetime
import calendar
import glob, os
import itertools
from collections import OrderedDict
import sys
import csv
import numpy as np

from collections import OrderedDict
import numpy
colors = ['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL']

import numpy as np
from pylab import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import os
import datetime
import calendar
import glob, os
import itertools
from collections import OrderedDict
import numpy as np


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import os
import datetime

import calendar
import glob, os
import itertools
from collections import OrderedDict

import numpy as np
import numpy
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
from pylab import *
import numpy as np

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


from collections import OrderedDict
import numpy
colors = ['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','AQUA','LIME','GREEN','TEAL']
markers=['3','4','8','s','p','P','o','v','^','<','*','h','H','+','x','X','D','d','|','_']
import numpy as np

global_font_size = 32
figure_width = 10
figure_highth = 10

space_from_x_y_axis = 25
style=itertools.cycle(["-","--","-.",":","None",""," ","-","--","-.",":"])




markers=['4','<','8','s','p','P','o','v','^','<','*','h','H','+','x','X','D','d','|','_']
descriptions=['point', 'pixel', 'circle', 'triangle_down', 'tri_down', 'octagon', 'square', 'pentagon', 'plus (filled)','star', 'hexagon1', 'hexagon2', 'plus', 'x', 'x (filled)','diamond', 'thin_diamond', 'vline', 'hline']
csfont = {'fontname':'Times New Roman'}
# import statistics
from pylab import *
# import pandas
import pandas as pd


# In[3]:


def set_plotting_global_attributes(x_axis_label,y_axis_label,x_axis_font_size,
                                   y_axis_font_size,x_axis_tick_font_size,
                                   y_axis_tick_font_size,x_axis_pad,y_axis_pad,
                                  image_width,image_lenght):
    import matplotlib.pyplot as plt
    global global_font_size
    global figure_width
    global figure_highth
    global space_from_x_y_axis
    global style
    global markers
    global csfont
    global descriptions
    font_size = 44
#     plt.figure(figsize=(10,0))
    global fig
    global global_mark_every
    global_mark_every = 1
    #matplotlib.rcParams['text.usetex'] = True
    fig = plt.figure()
    if image_width==0:
        image_width = 5.6
        image_lenght = 3.8
    fig.set_size_inches(image_width, image_lenght, forward=True)# default 
#     fig.set_size_inches(14, 8)
#     fig.set_size_inches(8, 6)
    global style
    #matplotlib.rcParams['text.usetex'] = True
    global markers
    
    global descriptions

    label_size = 40
    #matplotlib.rcParams['text.usetex'] = True
    csfont = {'fontname':'Times New Roman'}
    #write your code related to basemap here
    #plt.title('title',**csfont)
    plt.rcParams['xtick.labelsize'] = x_axis_tick_font_size 
    #matplotlib.rcParams['text.usetex'] = True
    plt.rcParams['ytick.labelsize']= y_axis_tick_font_size
    #matplotlib.rcParams['text.usetex'] = True
    plt.xlabel(x_axis_label, fontsize=x_axis_font_size,labelpad=x_axis_pad)
    #matplotlib.rcParams['text.usetex'] = True
    plt.ylabel(y_axis_label,fontsize=y_axis_font_size,labelpad=y_axis_pad)
    
    plt.grid(True)
    plt.tight_layout()
    #matplotlib.rcParams['text.usetex'] = True
    #plt.ylim(ymin=0) 
    return plt

# In[ ]:


def multiple_box_plot_on_each_x_axis(x_axis_label,y_axis_label,tickets_on_x_axis,x_axis_values,
                                     each_approach_each_x_axis_pont_values,x_axis_label_font_size,y_axis_label_font_size,
                                     x_axis_tick_font_size,
                                   y_axis_tick_font_size,
                                     legend_font_size,marker_size,box_width,
                                     x_axis_label_rotation_degree,plot_file_name):

#     data_a = [[1,2,5], [5,7,2,2,5], [7,2,5]]
#     data_b = [[6,4,2], [1,2,5,3,2], [2,3,5,1]]
#     data_a = [[0.4,0.5,0.6,0.5,0.6,0.1,0.0],  [0.4,0.3,0.3,0.4,0.6,0.0], [0.2,0.2,0.2,0.1,0.0]]
#     data_b = [[0.3,0.3,0.4,0.3,0.6,0.2,0.0,0.0],  [0.2,0.3,0.2,0.2,0.5,0.0], [0.1,0.1,0.2,0.1,0.0]] 
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label,
                                        x_axis_label_font_size,
                                   y_axis_label_font_size,x_axis_tick_font_size,
                                   y_axis_tick_font_size,0,0,
                                  6,3.6)
    #ticks = ['A', 'B', 'C']
    data_values ={}
    ID = 0
    for scheme in each_approach_each_x_axis_pont_values:
        this_scheme_values = []
        for x_axis_value in x_axis_values:
            values = each_approach_each_x_axis_pont_values[scheme][x_axis_value]
            this_scheme_values.append(values)
        data_values[ID] = this_scheme_values
        ID +=1
    #print('data_values',data_values)
    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)

    #plt.figure()
    colors = ['#D7191C','#2C7BB6','#8E44AD']
    color_index = 0
#     for scheme,x_axis_values in each_approach_each_x_axis_pont_values.items():
#         bpl = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.4, sym='', widths=0.6)
#         set_box_color(bpl, '#D7191C')
    plt_values = []
    for ID,data_value in data_values.items():
        #print('data_value',data_value)
        if ID==0:
            bpl = plt.boxplot(data_value, showmeans=True,meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                      "markersize":marker_size},positions=np.array(range(len(data_value)))*2.0-0.4, sym='', widths=box_width)
        elif ID==1:
            bpl = plt.boxplot(data_value,showmeans=True,meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                      "markersize":marker_size}, positions=np.array(range(len(data_value)))*2.0+0.1, sym='', widths=box_width)
        elif ID==2:
            bpl = plt.boxplot(data_value,showmeans=True, meanprops={"marker":"o","markerfacecolor":"white",
                                                                    "markeredgecolor":"black","markersize":marker_size},
                              positions=np.array(range(len(data_value)))*2.0+0.7, sym='', widths=box_width)

#         if ID>0:
#             bpl = plt.boxplot(data_value, positions=np.array(range(len(data_value)))*2.0+0.4, sym='', widths=0.6)
#         else:
#             bpl = plt.boxplot(data_value, positions=np.array(range(len(data_value)))*2.0-0.4, sym='', widths=0.6)
        #print('positions',np.array(range(len(data_value)))*2.0-0.4)
        set_box_color(bpl, colors[color_index])
        color_index+=1
#     bpl = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.4, sym='', widths=0.6)
#     bpr = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0.4, sym='', widths=0.6)
#     set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
#     set_box_color(bpr, '#2C7BB6')

    # draw temporary red and blue lines and use them to create a legend
    
    color_index = 0
    for scheme in each_approach_each_x_axis_pont_values:
        plt.plot([], c=colors[color_index], label=scheme)
        color_index +=1
#     plt.plot([], c='#D7191C', label='Apples')
#     plt.plot([], c='#2C7BB6', label='Oranges')
    #plt.legend()
    if len(list(each_approach_each_x_axis_pont_values.keys()))>1:
        plt.legend(fontsize=legend_font_size)
    
    plt.xticks(range(0, len(tickets_on_x_axis) * 2, 2), tickets_on_x_axis,rotation = x_axis_label_rotation_degree)
    #plt.xlim(-2, len(tickets_on_x_axis)*2)
    #plt.ylim(0, 1)
    plt.minorticks_on()
    plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(plot_file_name)

# In[ ]:


def ploting_simple_y_as_x(x_axix_label,y_axix_label,
                          x_axis_font_size, y_axis_font_size, x_axis_tick_font_size,
                          y_axis_tick_font_size, x_axis_pad, y_axis_pad,
                          x_min_value,y_axis_provided_min_value,tick_flag,xticks_points,
                          y_axis_provided_max_value,
                          dictionary_keys_in_order,
                          each_scheme_each_step_value,
                          x_axis_points,tickets_on_x_axis,
                          log_scale,legend_flag,
                          print_flag,legend_num_column,
                          legend_font_size,plot_name,
                          having_mark_on_linkes_flag,given_marker_size,image_width,plot_height,
                         legends_on_the_right_flag):
    
 
    colors = ['C0',"C0","C1", 'C1','C2','C2','C3','C3','C4','C5']
    style=[ 'solid', 'dashed','solid', 'dashed', 'solid', 'dashed','solid', 'dashed','solid', 'dashed']
    plt = set_plotting_global_attributes(x_axix_label,y_axix_label,x_axis_font_size, 
                          y_axis_font_size, x_axis_tick_font_size,
                          y_axis_tick_font_size, x_axis_pad, y_axis_pad,
                                         image_width,plot_height)
                        
            
    #print Read_and_Detection_time_with_convergence_Det_Alg
    my_dic = {}


    my_class_labels = []

    
#     x = np.arange(len(topologies))
    x = np.arange(max(x_axis_points))
    x = []
    for point_x_axis in x_axis_points:
        x.append((point_x_axis))
    x.sort()
    #print('we have %s as our x '%(x))
    sizes = []
    #plt.gca().set_color_cycle(['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL'])


    index = 0
    color_index =0
    for scheme_key in dictionary_keys_in_order:
        label_of_result = scheme_key
        y_axis_values = []
        import math
        from math import log
        x_values_for_this_scheme = []
        for point in x_axis_points:
            try:
                value  = each_scheme_each_step_value[scheme_key][point]
                if print_flag:
                    print("we get the values for scheme %s point %s %s"%(scheme_key,point,value))            
                y_axis_values.append(value)
                x_values_for_this_scheme.append(point)
            except:
                pass
        sizes.append(str(scheme_key))
        #print("these are the x and y axis values",Convergence_times,label_of_result)
        if having_mark_on_linkes_flag:
            plot(x_values_for_this_scheme, y_axis_values,colors[color_index],
                 linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=2.0,
                 markersize=given_marker_size,markerfacecolor='black',markeredgewidth='2', 
                 markeredgecolor=colors[color_index])
        else:
            plot(x_values_for_this_scheme, y_axis_values,colors[color_index],
                 linestyle=style[index],markevery=(0.0,0.1),linewidth=2.0)
            
#         print("scheme %s x points %s      "%(scheme_key,x))
#         print("scheme %s y_axis points %s "%(scheme_key,y_axis_values))
        index = index +1
        color_index+=1
        if color_index >=len(colors):
            color_index = 1
        if index >= len(style):
            index = 2
    my_class_labels = sizes

    plt.grid(True)
    plt.xlim(xmin=x_min_value)

    plt.grid(True)

    plt.grid(which='minor', linestyle=':', linewidth='0.1', color='black')

    plt.tight_layout()
    if log_scale:
        plt.yscale('log')
    if legend_flag:
        plt.legend([label for label in my_class_labels ],handlelength=1.0,fontsize=legend_font_size, ncol=legend_num_column,handleheight=2.4, labelspacing=0.02)
    if legends_on_the_right_flag:
        ax = plt.subplot(111)
        ax.legend([label for label in my_class_labels ],handlelength=1.0,fontsize=legend_font_size,loc='center left', bbox_to_anchor=(1, 0.5))
        # ax.xticks(np.arange(min(x_values_for_this_scheme), max(x_values_for_this_scheme)+1, 0.1))
    plt.ylim(y_axis_provided_min_value, y_axis_provided_max_value)
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
    
    # start, end = ax.get_xlim()
    # ax.xaxis.set_ticks(np.arange(start, end, 0.1))
    # plt.xticks(np.arange(0, 1, 20)) 
    plt.grid( which='minor', color='#999999', linestyle='-', alpha=0.1)
    # plt.xticks(np.arange(min(x_values_for_this_scheme), x_max_value, x_axis_tick_frequency))
    if tick_flag:
        ax = plt.subplot(111)
        ax.set_xticks(xticks_points)
    # plt.set_xticks([0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
    plt.tight_layout()
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
    # plt.locator_params(axis='both', nbins=10)
    plt.savefig(plot_name)
    plt.show()



# In[ ]:


def plot_histogram(data,number_of_bins,x_axis_label,y_axis_label,histogram_title,plot_file_name):
    import matplotlib.pyplot as plt
    import numpy as np
    # Plotting a basic histogram
    plt.hist(data, bins=number_of_bins, color='skyblue', edgecolor='black')
     
    # Adding labels and title
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(histogram_title)
     
    # Display the plot
    # plt.show()
    plt.tight_layout()
    plt.savefig(plot_file_name)

# In[ ]:


def plotting_multi_scheme_two_y_axis(x_axis_label1,y_axis_label1,y_axis_label2,
                        x_axis_label_font_size,
                        y_axis_label_font_size,x_axis_pad,y_axis_pad,
                        each_scheme_x_axis_y_axis_values1,each_scheme_x_axis_y_axis_values2,
                        x_axis_label_fot_size,y_axis_values_font_size,legend_flag,
                       legend_font_size,legend_num_column,plot_name):
    
#     plt = set_plotting_global_attributes(x_axis_label,y_axis_label,x_axis_label_font_size,
#                                          y_axis_label_font_size,x_axis_pad,y_axis_pad)
    
    colors = ['BLACK', 'RED', 'BLUE','GREEN','MAROON','AQUA','OLIVE','LIME','TEAL']
    style=[ 'solid', 'dashed', 'dashdot', 'dotted',":",'solid', 'dashed', 'dashdot']
    legend_labels_for_first = []
    all_legend_labels = []
    lines = []
    # create figure and axis objects with subplots()
    fig,ax = plt.subplots()
#     fig = plt.figure()
#     fig.set_size_inches(14, 8, forward=True)
#     plt.grid(True)
#     plt.tight_layout()
    color_indx = 0
    line_style_indx = 0
    for scheme in each_scheme_x_axis_y_axis_values1:
        x_axis_values = each_scheme_x_axis_y_axis_values1[scheme]["x_axis_values"]
        y_axis_values = each_scheme_x_axis_y_axis_values1[scheme]["y_axis_values"]
        # make a plot
        line = ax.plot(x_axis_values,
                y_axis_values,
                color=colors[color_indx], 
                marker="o")
        color_indx+=1
        lines.append(line)
        legend_labels_for_first.append(scheme)
        all_legend_labels.append("Utility, "+scheme)
    # set x-axis label
    ax.set_xlabel(x_axis_label1, fontsize = x_axis_label_fot_size)
    # set y-axis label
    ax.set_ylabel(y_axis_label1,
                  color="Black",
                  fontsize=y_axis_values_font_size)
    color_indx+=1
    
    legend_labels_for_second = []
    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    for scheme in each_scheme_x_axis_y_axis_values2:
        x_axis_values = each_scheme_x_axis_y_axis_values2[scheme]["x_axis_values"]
        y_axis_values = each_scheme_x_axis_y_axis_values2[scheme]["y_axis_values"]
        # make a plot with different y-axis using second axis object
        line = ax2.plot(x_axis_values, y_axis_values,color=colors[color_indx],marker="o")
        color_indx+=1
        lines.append(line)
        legend_labels_for_second.append(scheme)
        all_legend_labels.append("Fidelity, "+scheme)
    ax2.set_ylabel(y_axis_label2,color="Black",fontsize=y_axis_values_font_size)

    color_indx+=1
#     ax2.yticks(rotation=45)
#     plt.ylim(0, y_axis_provided_max_value)
#     plt.minorticks_on()
#     plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#     if legend_flag:
# #         plt.legend([label for label in legend_labels_for_first ],fontsize=legend_font_size, ncol=legend_num_column,handleheight=2.4, labelspacing=0.02)
#         plt.legend([label for label in all_legend_labels ],fontsize=legend_font_size, ncol=legend_num_column,handleheight=2.4, labelspacing=0.02)
#     ax2.legend(loc=0)
    first_flag = True
    for line in lines:
        if first_flag:
            lines_sum = line
            first_flag = False
        else:
            lines_sum = lines_sum+line
#     if legend_flag:
    ax.legend(lines_sum, all_legend_labels, loc=0)
#     if legend_flag:
#         ax2.legend([label for label in all_legend_labels],fontsize=legend_font_size, ncol=legend_num_column,handleheight=2.4, labelspacing=0.02)
#     plt.rcParams['xtick.labelsize'] = x_axis_label_fot_size 
#     #matplotlib.rcParams['text.usetex'] = True
#     plt.rcParams['ytick.labelsize']= y_axis_values_font_size
    plt.tight_layout()
    plt.grid(True)
#     plt.xlabel( fontsize=20,labelpad=0)
    #matplotlib.rcParams['text.usetex'] = True
#     plt.ylabel(fontsize=20,labelpad=0)
#     fig, ax = plt.subplots()
#     plt.grid(which='major', linestyle='-', linewidth='0.2', color='red')

    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
#     plt.savefig(plot_name)
    plt.show()

    # save the plot as a file
    fig.savefig('plots/two_different_y_axis_for_single_python_plot_with_twinx.jpg',
                format='jpeg',
                dpi=100,
                bbox_inches='tight')

# In[51]:


def plotting_2D(x_axix_label,y_axix_label,z_axis_label,
                          x_axis_font_size, y_axis_font_size, x_axis_tick_font_size,
                          y_axis_tick_font_size, x_axis_pad, y_axis_pad,
                          x_min_value,y_axis_provided_min_value,
                          y_axis_provided_max_value,
                          
                          x,
                          y,z,lower_point,middle_point,upper_point,
                          log_scale,legend_flag,
                          print_flag,legend_num_column,
                          legend_font_size,plot_name,
                          having_mark_on_linkes_flag,given_marker_size,image_width,plot_height):
    import matplotlib.colors as colors
#     plt = set_plotting_global_attributes(x_axix_label,y_axix_label,x_axis_font_size, 
#                           y_axis_font_size, x_axis_tick_font_size,
#                           y_axis_tick_font_size, x_axis_pad, y_axis_pad,
#                                          image_width,plot_height)
    
    def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
        new_cmap = colors.LinearSegmentedColormap.from_list(
            'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
            cmap(np.linspace(minval, maxval, n)))
        return new_cmap
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6,4))
    arr = np.linspace(0, 50, 100).reshape((10, 10))

    cmap = plt.get_cmap('plasma')
    new_cmap = truncate_colormap(cmap, 0.2, 0.9)
    plt.scatter(x,y,c = z,marker="s", s=100,cmap=plt.cm.get_cmap(new_cmap,11))
    plt.xlim(min(x),max(x)+.1)
    plt.ylim(min(y),max(y)+.1)
#     plt.yticks(np.arange(0.8, 1.01, step=0.05)) 
    cbar = plt.colorbar(orientation="vertical", extend="both",
                       pad=0.05, shrink=1, aspect=20, format="%.3f")

#     cbar.set_label(label=z_axis_label, size=16)
    cbar.set_ticks([lower_point+0.3,middle_point,upper_point-0.1])
    cbar.set_ticklabels(["$\leq $"+str(lower_point),str(middle_point),"$\geq $"+str(upper_point)])
    cbar.ax.tick_params(labelsize=17)
#     plt.rcParams['xtick.labelsize'] = 30 
#     #matplotlib.rcParams['text.usetex'] = True
#     plt.rcParams['ytick.labelsize']= 30
    plt.grid( which='minor', color='#999999', linestyle='-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(plot_name)
    plt.show()
    
# x = [0,0,0,0,2,2,2,2,3,3,3,3]# repeater life time 
# y = [0,1,2,3,0,1,2,3,0,1,2,3] # end node life time
# z = [-1,-1,-1,0,1,1,2,2,3,4,4,4]
# x = [0,1,2]# repeater life time 
# y = [0,0,0] # end node life time
# z = [-1,-1,-1]
# # 2.3,6,9.9
# each_scheme_each_step_value = {}
# plotting_2D("E_M_t","R_M_t","Utility",
#                           14, 14, 14,
#                           14, 0, 0,
#                           0,0,
#                           100,
                          
                          
#                           x,y,z,2,6,10,
#                           False,True,
#                           False,1,
#                           14,"plots/2D.pdf",
#                           False,3,6,3.6)

# In[ ]:


x = [1,1,1,1,            2,2,2,2,            3,3,3,3,         4,4,4,4]# repeater life time 
y = [1,2,3,4,            1,2,3,4,            1,2,3,4,         1,2,3,4] # end node life time
z = [-100,-100,-100,-100,-100,-100,-100,-100,-30,-30,-20,-10, -5,-1,4,4]

# In[2]:


# def ploting_simple_y_as_x(x_axix_label,y_axix_label,
#                           x_axis_font_size, y_axis_font_size, x_axis_tick_font_size,
#                           y_axis_tick_font_size, x_axis_pad, y_axis_pad,
#                           x_min_value,y_axis_provided_min_value,
#                           y_axis_provided_max_value,
#                           dictionary_keys_in_order,
#                           each_scheme_each_step_value,
#                           x_axis_points,tickets_on_x_axis,
#                           log_scale,legend_flag,
#                           print_flag,legend_num_column,
#                           legend_font_size,plot_name,
#                           having_mark_on_linkes_flag,given_marker_size,image_width,plot_height,
#                          legends_on_the_right_flag):
    
 
#     colors = ['BLACK', 'RED', 'BLUE','GREEN','MAROON','AQUA','OLIVE','LIME','TEAL']
#     style=[ 'solid', 'dashed', 'dashdot', 'dotted',":",'solid', 'dashed', 'dashdot']
#     plt = set_plotting_global_attributes(x_axix_label,y_axix_label,x_axis_font_size, 
#                           y_axis_font_size, x_axis_tick_font_size,
#                           y_axis_tick_font_size, x_axis_pad, y_axis_pad,
#                                          image_width,plot_height)
                        
            
#     #print Read_and_Detection_time_with_convergence_Det_Alg
#     my_dic = {}


#     my_class_labels = []

    
# #     x = np.arange(len(topologies))
#     x = np.arange(max(x_axis_points))
#     x = []
#     for point_x_axis in x_axis_points:
#         x.append((point_x_axis))
#     x.sort()
#     #print('we have %s as our x '%(x))
#     sizes = []
#     #plt.gca().set_color_cycle(['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL'])

#     #print 'Convergene_time_dictionary',Convergene_time_dictionary
#     index = 0
#     color_index =0
#     for scheme_key in dictionary_keys_in_order:
#         label_of_result = scheme_key
#         y_axis_values = []
#         import math
#         from math import log
#         x_values_for_this_scheme = []
#         for point in x_axis_points:
#             try:
#                 value  = each_scheme_each_step_value[scheme_key][point]
#                 if print_flag:
#                     print("we get the values for scheme %s point %s %s"%(scheme_key,point,value))            
#                 y_axis_values.append(value)
#                 x_values_for_this_scheme.append(point)
#             except:
#                 pass
#         sizes.append(str(scheme_key))
#         #print("these are the x and y axis values",Convergence_times,label_of_result)
#         if having_mark_on_linkes_flag:
#             plot(x_values_for_this_scheme, y_axis_values,colors[color_index],
#                  linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=3.0,
#                  markersize=given_marker_size,markerfacecolor='black',markeredgewidth='2', 
#                  markeredgecolor=colors[color_index])
#         else:
#             plot(x_values_for_this_scheme, y_axis_values,colors[color_index],
#                  linestyle=style[index],markevery=(0.0,0.1),linewidth=3.0)
            
# #         print("scheme %s x points %s      "%(scheme_key,x))
# #         print("scheme %s y_axis points %s "%(scheme_key,y_axis_values))
#         index = index +1
#         color_index+=1
#         if color_index >=len(colors):
#             color_index = 1
#         if index >= len(style):
#             index = 2
            
# #         if color_index >= len(colors):
# #             index = 0
        
        
    
    
#     my_class_labels = sizes

#     plt.grid(True)
# #     plt.ylim(ymin=0)
# #     plt.ylim(ymin=0)
#     plt.xlim(xmin=x_min_value)
# #     plt.tight_layout()
# #     new_ticks = [ str(y) for y in topologies]
# #     plt.xticks(x, new_ticks,fontsize=32)
#     plt.grid(True)
# #     fig, ax = plt.subplots()
# #     plt.grid(which='major', linestyle='-', linewidth='0.2', color='red')

#     plt.grid(which='minor', linestyle=':', linewidth='0.2', color='black')

#     plt.tight_layout()
#     if log_scale:
#         plt.yscale('log')
# #     plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=28)
# #     plt.legend([label for label in my_class_labels ],fontsize=23)
#     if legend_flag:
#         plt.legend([label for label in my_class_labels ],fontsize=legend_font_size, ncol=legend_num_column,handleheight=2.4, labelspacing=0.02)
#     if legends_on_the_right_flag:
#         ax = plt.subplot(111)
#         ax.legend([label for label in my_class_labels ],fontsize=legend_font_size,loc='center left', bbox_to_anchor=(1, 0.5))
# #     plt.legend(loc=7)
# #     plt.tight_layout()
# #     plt.subplots_adjust(right=0.75)

# #     plt.xticks(range(0, len(tickets_on_x_axis) * 2, 2), tickets_on_x_axis)
# #     plt.xlim(-2, len(tickets_on_x_axis)*2)
#     plt.ylim(y_axis_provided_min_value, y_axis_provided_max_value)
#     plt.minorticks_on()
#     plt.grid(which='minor', linestyle=':', linewidth='0.2', color='black')

# #     plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#     plt.grid( which='minor', color='#999999', linestyle='-', alpha=0.2)
    
#     plt.tight_layout()
#     plt.grid(which='minor', linestyle=':', linewidth='0.2', color='black')

#     plt.savefig(plot_name)
#     plt.show()

# In[ ]:


def get_arrs(x_values,my_dictionary):
    import csv
    summation = 0
    for key,value in my_dictionary.items():
        summation  = summation +(value)
    arrs= []
    import os
    cum=0.0
    for i in x_values:
        cum = cum + my_dictionary[i]
        
        
        arrs.append(float(cum)/float(summation))


    return arrs


    



# In[ ]:


# each_scheme_each_step_value = {'GA, |Paths|=3': {
#     0: 7.03, 1: 7.03, 2: 7.03, 3: 7.11, 4: 7.2, 5: 7.4, 6: 7.56, 7: 7.6, 8: 7.66, 9: 7.8, 10: 7.84, 11: 7.86, 12: 7.9, 13: 8.01, 14: 8.03, 15: 8.06, 16: 8.08, 17: 8.12, 18: 8.16, 19: 8.2, 20: 8.23, 21: 8.28, 22: 8.29, 23: 8.33, 24: 8.36, 25: 8.36, 26: 8.39, 27: 8.43, 28: 8.45, 29: 8.47, 30: 8.5, 31: 8.5, 32: 8.53, 33: 8.57, 34: 8.58, 35: 8.6, 36: 8.62, 37: 8.62, 38: 8.64, 39: 8.64, 40: 8.66, 41: 8.67, 42: 8.68, 43: 8.7, 44: 8.71, 45: 8.71, 46: 8.73, 47: 8.73, 48: 8.75, 49: 8.76, 50: 8.76, 51: 8.78, 52: 8.79, 53: 8.79, 54: 8.79, 55: 8.81, 56: 8.82, 57: 8.83, 58: 8.85, 59: 8.85, 60: 8.85, 61: 8.86, 62: 8.88, 63: 8.88, 64: 8.88, 65: 8.9, 66: 8.9, 67: 8.91, 68: 8.92, 69: 8.92, 70: 8.92, 71: 8.93, 72: 8.94, 73: 8.94, 74: 8.95, 75: 8.96, 76: 8.96, 77: 8.96, 78: 8.97, 79: 8.97, 80: 8.97, 81: 8.97, 82: 8.98, 83: 8.98, 84: 8.99, 85: 8.99, 86: 8.99, 87: 9.0, 88: 9.0, 89: 9.0, 90: 9.0, 91: 9.0, 92: 9.01, 93: 9.01, 94: 9.01, 95: 9.02, 96: 9.02, 97: 9.03, 98: 9.04, 99: 9.04, 100: 9.04, 101: 9.04, 102: 9.04, 103: 9.05, 104: 9.05, 105: 9.06, 106: 9.06, 107: 9.07, 108: 9.08, 109: 9.08, 110: 9.09, 111: 9.09, 112: 9.1, 113: 9.1, 114: 9.1, 115: 9.1, 116: 9.1, 117: 9.11, 118: 9.11, 119: 9.11, 120: 9.12, 121: 9.12, 122: 9.12, 123: 9.13, 124: 9.14, 125: 9.14, 126: 9.15, 127: 9.15, 128: 9.15, 129: 9.15, 130: 9.16, 131: 9.16, 132: 9.16, 133: 9.17, 134: 9.17, 135: 9.17, 136: 9.17, 137: 9.17, 138: 9.2, 139: 9.2, 140: 9.21, 141: 9.22, 142: 9.22, 143: 9.22, 144: 9.22, 145: 9.22, 146: 9.23, 147: 9.23, 148: 9.23, 149: 9.23, 150: 9.24, 151: 9.24, 152: 9.24, 153: 9.24, 154: 9.24, 155: 9.24, 156: 9.24, 157: 9.25, 158: 9.25, 159: 9.25, 160: 9.25, 161: 9.26, 162: 9.26, 163: 9.26, 164: 9.26, 165: 9.26, 166: 9.26, 167: 9.27, 168: 9.27, 169: 9.27, 170: 9.27, 171: 9.27, 172: 9.28, 173: 9.28, 174: 9.28, 175: 9.28, 176: 9.28, 177: 9.28, 178: 9.28, 179: 9.28, 180: 9.29, 181: 9.29, 182: 9.29, 183: 9.29, 184: 9.29, 185: 9.29, 186: 9.29, 187: 9.29, 188: 9.29, 189: 9.29, 190: 9.29, 191: 9.3, 192: 9.3, 193: 9.3, 194: 9.3, 195: 9.3, 196: 9.3, 197: 9.3, 198: 9.3, 199: 9.3, 200: 9.3, 201: 9.3, 202: 9.3, 203: 9.3, 204: 9.31, 205: 9.31, 206: 9.31, 207: 9.31, 208: 9.33, 209: 9.33, 210: 9.33, 211: 9.33, 212: 9.33, 213: 9.33, 214: 9.33, 215: 9.33, 216: 9.33, 217: 9.33, 218: 9.33, 219: 9.33, 220: 9.33, 221: 9.34, 222: 9.34, 223: 9.34, 224: 9.34, 225: 9.34, 226: 9.34, 227: 9.34, 228: 9.34, 229: 9.34, 230: 9.34, 231: 9.34, 232: 9.34, 233: 9.34, 234: 9.34, 235: 9.34, 236: 9.34, 237: 9.34, 238: 9.34, 239: 9.35, 240: 9.35, 241: 9.35, 242: 9.35, 243: 9.35, 244: 9.35, 245: 9.36, 246: 9.36, 247: 9.36, 248: 9.36, 249: 9.36, 250: 9.36, 251: 9.36, 252: 9.36, 253: 9.36, 254: 9.36, 255: 9.37, 256: 9.37, 257: 9.37, 258: 9.37, 259: 9.37, 260: 9.37, 261: 9.37, 262: 9.37, 263: 9.37, 264: 9.37, 265: 9.37, 266: 9.37, 267: 9.37, 268: 9.37, 269: 9.37, 270: 9.37, 271: 9.37, 272: 9.37, 273: 9.37, 274: 9.38, 275: 9.38, 276: 9.38, 277: 9.38, 278: 9.38, 279: 9.38, 280: 9.38, 281: 9.38, 282: 9.38, 283: 9.38, 284: 9.38, 285: 9.38, 286: 9.38, 287: 9.38, 288: 9.38, 289: 9.38, 290: 9.38, 291: 9.38, 292: 9.38, 293: 9.38, 294: 9.38, 295: 9.38, 296: 9.38, 297: 9.38, 298: 9.39, 299: 9.39, 300: 9.39, 301: 9.39, 302: 9.39, 303: 9.39, 304: 9.39, 305: 9.39, 306: 9.39, 307: 9.39, 308: 9.39, 309: 9.39, 310: 9.39, 311: 9.39, 312: 9.39, 313: 9.39, 314: 9.39, 315: 9.39, 316: 9.39, 317: 9.39, 318: 9.39, 319: 9.39, 320: 9.39, 321: 9.39, 322: 9.39, 323: 9.4, 324: 9.4, 325: 9.4, 326: 9.4, 327: 9.4, 328: 9.4, 329: 9.4, 330: 9.4, 331: 9.4, 332: 9.4, 333: 9.4, 334: 9.4, 335: 9.4, 336: 9.4, 337: 9.41, 338: 9.41, 339: 9.41, 340: 9.41, 341: 9.41, 342: 9.41, 343: 9.41, 344: 9.41, 345: 9.41, 346: 9.41, 347: 9.41, 348: 9.41, 349: 9.41, 350: 9.41, 351: 9.41, 352: 9.41, 353: 9.41, 354: 9.41, 355: 9.41, 356: 9.41, 357: 9.41, 358: 9.41, 359: 9.41, 360: 9.41, 361: 9.41, 362: 9.41, 363: 9.41, 364: 9.41, 365: 9.41, 366: 9.41, 367: 9.41, 368: 9.41, 369: 9.42, 370: 9.42, 371: 9.42, 372: 9.42, 373: 9.42, 374: 9.42, 375: 9.42, 376: 9.42, 377: 9.42, 378: 9.42, 379: 9.42, 380: 9.43, 381: 9.43, 382: 9.43, 383: 9.43, 384: 9.43, 385: 9.43, 386: 9.43, 387: 9.43, 388: 9.43, 389: 9.43, 390: 9.43, 391: 9.43, 392: 9.43, 393: 9.43, 394: 9.43, 395: 9.43, 396: 9.43, 397: 9.43, 398: 9.43, 399: 9.43, 400: 9.43, 401: 9.43, 402: 9.43, 403: 9.44, 404: 9.44, 405: 9.44, 406: 9.44, 407: 9.44, 408: 9.44, 409: 9.44, 410: 9.44, 411: 9.44, 412: 9.44, 413: 9.44, 414: 9.44, 415: 9.44, 416: 9.44, 417: 9.44, 418: 9.44, 419: 9.44, 420: 9.44, 421: 9.44, 422: 9.44, 423: 9.44, 424: 9.44, 425: 9.44, 426: 9.44, 427: 9.44, 428: 9.44, 429: 9.44, 430: 9.44, 431: 9.44, 432: 9.44, 433: 9.44, 434: 9.44, 435: 9.44, 436: 9.44, 437: 9.44, 438: 9.45, 439: 9.45, 440: 9.45, 441: 9.45, 442: 9.45, 443: 9.45, 444: 9.45, 445: 9.45, 446: 9.45, 447: 9.45, 448: 9.45, 449: 9.45, 450: 9.45, 451: 9.45, 452: 9.45, 453: 9.45, 454: 9.45, 455: 9.45, 456: 9.45, 457: 9.45, 458: 9.45, 459: 9.45, 460: 9.45, 461: 9.45, 462: 9.45, 463: 9.45, 464: 9.45, 465: 9.45, 466: 9.45, 467: 9.45, 468: 9.45, 469: 9.45, 470: 9.45, 471: 9.45, 472: 9.45, 473: 9.45, 474: 9.45, 475: 9.45, 476: 9.45, 477: 9.45, 478: 9.45, 479: 9.45, 480: 9.45, 481: 9.45, 482: 9.45, 483: 9.45, 484: 9.45, 485: 9.45, 486: 9.45, 487: 9.45, 488: 9.45, 489: 9.45, 490: 9.45, 491: 9.45, 492: 9.45, 493: 9.45, 494: 9.45, 495: 9.45, 496: 9.45, 497: 9.45, 498: 9.45, 499: 9.45, 500: 9.45, 501: 9.45, 502: 9.45, 503: 9.45, 504: 9.45, 505: 9.45, 506: 9.45, 507: 9.45, 508: 9.45, 509: 9.45, 510: 9.45, 511: 9.45, 512: 9.45, 513: 9.45, 514: 9.45, 515: 9.45, 516: 9.45, 517: 9.45, 518: 9.45, 519: 9.45, 520: 9.45, 521: 9.45, 522: 9.45, 523: 9.46, 524: 9.46, 525: 9.46, 526: 9.46, 527: 9.46, 528: 9.46, 529: 9.46, 530: 9.46, 531: 9.46, 532: 9.46, 533: 9.46, 534: 9.46, 535: 9.46, 536: 9.46, 537: 9.46, 538: 9.46, 539: 9.46, 540: 9.46, 541: 9.46, 542: 9.46, 543: 9.46, 544: 9.46, 545: 9.46, 546: 9.46, 547: 9.46, 548: 9.46, 549: 9.46, 550: 9.46, 551: 9.46, 552: 9.46, 553: 9.46, 554: 9.46, 555: 9.46, 556: 9.46, 557: 9.46, 558: 9.46, 559: 9.46, 560: 9.46, 561: 9.46, 562: 9.46, 563: 9.46, 564: 9.46, 565: 9.46, 566: 9.46, 567: 9.46, 568: 9.46, 569: 9.46, 570: 9.46, 571: 9.46, 572: 9.46, 573: 9.46, 574: 9.46, 575: 9.46, 576: 9.46, 577: 9.46, 578: 9.46, 579: 9.46, 580: 9.46, 581: 9.46, 582: 9.46, 583: 9.46, 584: 9.46, 585: 9.46, 586: 9.46, 587: 9.46, 588: 9.46, 589: 9.46, 590: 9.46, 591: 9.46, 592: 9.46, 593: 9.46, 594: 9.46, 595: 9.46, 596: 9.46, 597: 9.46, 598: 9.46, 599: 9.46, 600: 9.46, 601: 9.46, 602: 9.46, 603: 9.46, 604: 9.46, 605: 9.46, 606: 9.46, 607: 9.46, 608: 9.46, 609: 9.46, 610: 9.46, 611: 9.46, 612: 9.46, 613: 9.47, 614: 9.47, 615: 9.47, 616: 9.47, 617: 9.47, 618: 9.47, 619: 9.47, 620: 9.47, 621: 9.47, 622: 9.47, 623: 9.47, 624: 9.47, 625: 9.47, 626: 9.47, 627: 9.47, 628: 9.47, 629: 9.47, 630: 9.47, 631: 9.47, 632: 9.47, 633: 9.47, 634: 9.47, 635: 9.47, 636: 9.47, 637: 9.47, 638: 9.47, 639: 9.47, 640: 9.47, 641: 9.47, 642: 9.47, 643: 9.47, 644: 9.47, 645: 9.47, 646: 9.47, 647: 9.47, 648: 9.47, 649: 9.47, 650: 9.47, 651: 9.47, 652: 9.47, 653: 9.47, 654: 9.47, 655: 9.47, 656: 9.47, 657: 9.47, 658: 9.48, 659: 9.48, 660: 9.48, 661: 9.48, 662: 9.48, 663: 9.48, 664: 9.48, 665: 9.48, 666: 9.48, 667: 9.48, 668: 9.48, 669: 9.48, 670: 9.48, 671: 9.48, 672: 9.48, 673: 9.48, 674: 9.48, 675: 9.48, 676: 9.48, 677: 9.48, 678: 9.48, 679: 9.48, 680: 9.48, 681: 9.48, 682: 9.48, 683: 9.48, 684: 9.48, 685: 9.48, 686: 9.48, 687: 9.48, 688: 9.48, 689: 9.48, 690: 9.48, 691: 9.48, 692: 9.48, 693: 9.48, 694: 9.48, 695: 9.48, 696: 9.48, 697: 9.48, 698: 9.48, 699: 9.48, 700: 9.48, 701: 9.48, 702: 9.48, 703: 9.48, 704: 9.48, 705: 9.48, 706: 9.48, 707: 9.48, 708: 9.48, 709: 9.48, 710: 9.48, 711: 9.48, 712: 9.48, 713: 9.48, 714: 9.48, 715: 9.48, 716: 9.48, 717: 9.48, 718: 9.48, 719: 9.48, 720: 9.48, 721: 9.48, 722: 9.48, 723: 9.48, 724: 9.48, 725: 9.48, 726: 9.48, 727: 9.48, 728: 9.48, 729: 9.48, 730: 9.48, 731: 9.48, 732: 9.48, 733: 9.48, 734: 9.48, 735: 9.48, 736: 9.48, 737: 9.49, 738: 9.49, 739: 9.49, 740: 9.49, 741: 9.49, 742: 9.49, 743: 9.49, 744: 9.49, 745: 9.49, 746: 9.49, 747: 9.49, 748: 9.49, 749: 9.49, 750: 9.49, 751: 9.49, 752: 9.49, 753: 9.49, 754: 9.49, 755: 9.49, 756: 9.49, 757: 9.49, 758: 9.49, 759: 9.49, 760: 9.49, 761: 9.49, 762: 9.49, 763: 9.49, 764: 9.49, 765: 9.49, 766: 9.49, 767: 9.49, 768: 9.49, 769: 9.49, 770: 9.49, 771: 9.49, 772: 9.49, 773: 9.49, 774: 9.49, 775: 9.49, 776: 9.49, 777: 9.49, 778: 9.49, 779: 9.49, 780: 9.49, 781: 9.49, 782: 9.49, 783: 9.49, 784: 9.49, 785: 9.49, 786: 9.49, 787: 9.49, 788: 9.49, 789: 9.49, 790: 9.49, 791: 9.49, 792: 9.49, 793: 9.49, 794: 9.49, 795: 9.49, 796: 9.49, 797: 9.49, 798: 9.49, 799: 9.49, 800: 9.49, 801: 9.49, 802: 9.49, 803: 9.49, 804: 9.49, 805: 9.49, 806: 9.49, 807: 9.49, 808: 9.49, 809: 9.49, 810: 9.49, 811: 9.49, 812: 9.49, 813: 9.49, 814: 9.49, 815: 9.49, 816: 9.49, 817: 9.49, 818: 9.49, 819: 9.49, 820: 9.49, 821: 9.49, 822: 9.49, 823: 9.49, 824: 9.49, 825: 9.49, 826: 9.49, 827: 9.49, 828: 9.49, 829: 9.49, 830: 9.49, 831: 9.49, 832: 9.49, 833: 9.49, 834: 9.49, 835: 9.49, 836: 9.49, 837: 9.49, 838: 9.49, 839: 9.49, 840: 9.49, 841: 9.49, 842: 9.49, 843: 9.49, 844: 9.49, 845: 9.49, 846: 9.49, 847: 9.49, 848: 9.49, 849: 9.49, 850: 9.49, 851: 9.49, 852: 9.49, 853: 9.49, 854: 9.49, 855: 9.49, 856: 9.49, 857: 9.49, 858: 9.49, 859: 9.49, 860: 9.49, 861: 9.49, 862: 9.49, 863: 9.49, 864: 9.49, 865: 9.49, 866: 9.49, 867: 9.49, 868: 9.49, 869: 9.49, 870: 9.49, 871: 9.49, 872: 9.49, 873: 9.49, 874: 9.49, 875: 9.49, 876: 9.49, 877: 9.49, 878: 9.49, 879: 9.49, 880: 9.49, 881: 9.49, 882: 9.49, 883: 9.49, 884: 9.49, 885: 9.49, 886: 9.49, 887: 9.49, 888: 9.49, 889: 9.49, 890: 9.49, 891: 9.49, 892: 9.49, 893: 9.49, 894: 9.49, 895: 9.49, 896: 9.49, 897: 9.5, 898: 9.5, 899: 9.5, 900: 9.5, 901: 9.5, 902: 9.5, 903: 9.5, 904: 9.5, 905: 9.5, 906: 9.5, 907: 9.5, 908: 9.5, 909: 9.5, 910: 9.5, 911: 9.5, 912: 9.5, 913: 9.5, 914: 9.5, 915: 9.5, 916: 9.5, 917: 9.5, 918: 9.5, 919: 9.5, 920: 9.5, 921: 9.5, 922: 9.5, 923: 9.5, 924: 9.5, 925: 9.5, 926: 9.5, 927: 9.5, 928: 9.5, 929: 9.5, 930: 9.5, 931: 9.5, 932: 9.5, 933: 9.5, 934: 9.5, 935: 9.5, 936: 9.5, 937: 9.5, 938: 9.5, 939: 9.5, 940: 9.5, 941: 9.5, 942: 9.5, 943: 9.5, 944: 9.5, 945: 9.5, 946: 9.5, 947: 9.5, 948: 9.5, 949: 9.5, 950: 9.5, 951: 9.5, 952: 9.5, 953: 9.5, 954: 9.5, 955: 9.5, 956: 9.5, 957: 9.5, 958: 9.5, 959: 9.5, 960: 9.5, 961: 9.5, 962: 9.5, 963: 9.5, 964: 9.5, 965: 9.5, 966: 9.5, 967: 9.5, 968: 9.5, 969: 9.5, 970: 9.5, 971: 9.5, 972: 9.5, 973: 9.5, 974: 9.5, 975: 9.5, 976: 9.5, 977: 9.5, 978: 9.51, 979: 9.51, 980: 9.51, 981: 9.51, 982: 9.51, 983: 9.51, 984: 9.51, 985: 9.51, 986: 9.51, 987: 9.51, 988: 9.51, 989: 9.51, 990: 9.51, 991: 9.51, 992: 9.51, 993: 9.51, 994: 9.51, 995: 9.51, 996: 9.51, 997: 9.51, 998: 9.51, 999: 9.51}, 'GA, |Paths|=6': {0: 8.8, 1: 8.8, 2: 8.88, 3: 8.97, 4: 9.04, 5: 9.17, 6: 9.18, 7: 9.19, 8: 9.25, 9: 9.28, 10: 9.29, 11: 9.31, 12: 9.35, 13: 9.36, 14: 9.41, 15: 9.41, 16: 9.42, 17: 9.42, 18: 9.43, 19: 9.45, 20: 9.46, 21: 9.47, 22: 9.47, 23: 9.47, 24: 9.49, 25: 9.49, 26: 9.5, 27: 9.51, 28: 9.51, 29: 9.51, 30: 9.52, 31: 9.52, 32: 9.52, 33: 9.52, 34: 9.52, 35: 9.53, 36: 9.53, 37: 9.54, 38: 9.54, 39: 9.55, 40: 9.55, 41: 9.56, 42: 9.56, 43: 9.56, 44: 9.57, 45: 9.57, 46: 9.57, 47: 9.6, 48: 9.6, 49: 9.6, 50: 9.6, 51: 9.62, 52: 9.63, 53: 9.63, 54: 9.63, 55: 9.63, 56: 9.64, 57: 9.64, 58: 9.64, 59: 9.64, 60: 9.65, 61: 9.65, 62: 9.65, 63: 9.66, 64: 9.66, 65: 9.68, 66: 9.68, 67: 9.68, 68: 9.68, 69: 9.69, 70: 9.69, 71: 9.69, 72: 9.7, 73: 9.7, 74: 9.7, 75: 9.7, 76: 9.7, 77: 9.7, 78: 9.7, 79: 9.71, 80: 9.71, 81: 9.71, 82: 9.72, 83: 9.72, 84: 9.73, 85: 9.73, 86: 9.73, 87: 9.73, 88: 9.73, 89: 9.73, 90: 9.74, 91: 9.74, 92: 9.74, 93: 9.75, 94: 9.75, 95: 9.75, 96: 9.75, 97: 9.76, 98: 9.76, 99: 9.76, 100: 9.76, 101: 9.76, 102: 9.76, 103: 9.77, 104: 9.77, 105: 9.77, 106: 9.77, 107: 9.77, 108: 9.77, 109: 9.77, 110: 9.77, 111: 9.77, 112: 9.77, 113: 9.77, 114: 9.78, 115: 9.79, 116: 9.79, 117: 9.79, 118: 9.79, 119: 9.79, 120: 9.8, 121: 9.8, 122: 9.8, 123: 9.8, 124: 9.8, 125: 9.8, 126: 9.8, 127: 9.8, 128: 9.8, 129: 9.81, 130: 9.81, 131: 9.81, 132: 9.81, 133: 9.81, 134: 9.81, 135: 9.81, 136: 9.81, 137: 9.81, 138: 9.81, 139: 9.81, 140: 9.81, 141: 9.81, 142: 9.81, 143: 9.81, 144: 9.81, 145: 9.81, 146: 9.81, 147: 9.81, 148: 9.82, 149: 9.82, 150: 9.82, 151: 9.82, 152: 9.82, 153: 9.82, 154: 9.82, 155: 9.83, 156: 9.83, 157: 9.83, 158: 9.83, 159: 9.83, 160: 9.84, 161: 9.84, 162: 9.84, 163: 9.84, 164: 9.84, 165: 9.84, 166: 9.84, 167: 9.84, 168: 9.84, 169: 9.84, 170: 9.84, 171: 9.84, 172: 9.84, 173: 9.84, 174: 9.84, 175: 9.84, 176: 9.84, 177: 9.84, 178: 9.84, 179: 9.84, 180: 9.85, 181: 9.85, 182: 9.85, 183: 9.85, 184: 9.85, 185: 9.85, 186: 9.85, 187: 9.85, 188: 9.85, 189: 9.85, 190: 9.85, 191: 9.85, 192: 9.85, 193: 9.85, 194: 9.85, 195: 9.86, 196: 9.86, 197: 9.86, 198: 9.86, 199: 9.86, 200: 9.86, 201: 9.86, 202: 9.86, 203: 9.86, 204: 9.86, 205: 9.86, 206: 9.86, 207: 9.86, 208: 9.86, 209: 9.86, 210: 9.86, 211: 9.86, 212: 9.86, 213: 9.86, 214: 9.86, 215: 9.86, 216: 9.86, 217: 9.86, 218: 9.86, 219: 9.86, 220: 9.86, 221: 9.86, 222: 9.86, 223: 9.86, 224: 9.86, 225: 9.86, 226: 9.86, 227: 9.86, 228: 9.86, 229: 9.86, 230: 9.87, 231: 9.87, 232: 9.87, 233: 9.87, 234: 9.88, 235: 9.88, 236: 9.88, 237: 9.88, 238: 9.88, 239: 9.88, 240: 9.88, 241: 9.88, 242: 9.88, 243: 9.88, 244: 9.88, 245: 9.88, 246: 9.88, 247: 9.88, 248: 9.88, 249: 9.88, 250: 9.88, 251: 9.88, 252: 9.88, 253: 9.88, 254: 9.88, 255: 9.88, 256: 9.88, 257: 9.88, 258: 9.88, 259: 9.88, 260: 9.88, 261: 9.88, 262: 9.88, 263: 9.88, 264: 9.88, 265: 9.88, 266: 9.88, 267: 9.88, 268: 9.88, 269: 9.88, 270: 9.88, 271: 9.88, 272: 9.88, 273: 9.88, 274: 9.88, 275: 9.88, 276: 9.88, 277: 9.88, 278: 9.88, 279: 9.88, 280: 9.88, 281: 9.88, 282: 9.88, 283: 9.88, 284: 9.88, 285: 9.88, 286: 9.88, 287: 9.88, 288: 9.88, 289: 9.88, 290: 9.88, 291: 9.88, 292: 9.88, 293: 9.88, 294: 9.88, 295: 9.88, 296: 9.88, 297: 9.89, 298: 9.89, 299: 9.9, 300: 9.9, 301: 9.9, 302: 9.9, 303: 9.9, 304: 9.9, 305: 9.9, 306: 9.9, 307: 9.9, 308: 9.9, 309: 9.9, 310: 9.9, 311: 9.9, 312: 9.9, 313: 9.9, 314: 9.9, 315: 9.9, 316: 9.9, 317: 9.9, 318: 9.9, 319: 9.9, 320: 9.9, 321: 9.9, 322: 9.9, 323: 9.9, 324: 9.9, 325: 9.9, 326: 9.9, 327: 9.9, 328: 9.9, 329: 9.9, 330: 9.9, 331: 9.9, 332: 9.9, 333: 9.9, 334: 9.9, 335: 9.9, 336: 9.9, 337: 9.9, 338: 9.9, 339: 9.9, 340: 9.9, 341: 9.9, 342: 9.9, 343: 9.9, 344: 9.9, 345: 9.9, 346: 9.9, 347: 9.91, 348: 9.91, 349: 9.91, 350: 9.91, 351: 9.91, 352: 9.91, 353: 9.91, 354: 9.91, 355: 9.91, 356: 9.91, 357: 9.91, 358: 9.91, 359: 9.91, 360: 9.91, 361: 9.91, 362: 9.91, 363: 9.91, 364: 9.91, 365: 9.91, 366: 9.91, 367: 9.91, 368: 9.92, 369: 9.92, 370: 9.92, 371: 9.92, 372: 9.92, 373: 9.92, 374: 9.92, 375: 9.92, 376: 9.92, 377: 9.92, 378: 9.92, 379: 9.92, 380: 9.92, 381: 9.92, 382: 9.92, 383: 9.92, 384: 9.92, 385: 9.92, 386: 9.92, 387: 9.93, 388: 9.93, 389: 9.93, 390: 9.93, 391: 9.93, 392: 9.93, 393: 9.93, 394: 9.93, 395: 9.93, 396: 9.93, 397: 9.93, 398: 9.93, 399: 9.93, 400: 9.93, 401: 9.93, 402: 9.93, 403: 9.93, 404: 9.93, 405: 9.93, 406: 9.93, 407: 9.93, 408: 9.93, 409: 9.93, 410: 9.93, 411: 9.93, 412: 9.93, 413: 9.93, 414: 9.93, 415: 9.93, 416: 9.93, 417: 9.93, 418: 9.93, 419: 9.93, 420: 9.93, 421: 9.93, 422: 9.93, 423: 9.94, 424: 9.94, 425: 9.94, 426: 9.94, 427: 9.94, 428: 9.94, 429: 9.94, 430: 9.94, 431: 9.94, 432: 9.94, 433: 9.94, 434: 9.94, 435: 9.94, 436: 9.94, 437: 9.94, 438: 9.94, 439: 9.94, 440: 9.94, 441: 9.94, 442: 9.94, 443: 9.94, 444: 9.94, 445: 9.94, 446: 9.94, 447: 9.94, 448: 9.94, 449: 9.94, 450: 9.94, 451: 9.94, 452: 9.94, 453: 9.94, 454: 9.94, 455: 9.94, 456: 9.94, 457: 9.94, 458: 9.94, 459: 9.94, 460: 9.94, 461: 9.94, 462: 9.94, 463: 9.94, 464: 9.95, 465: 9.95, 466: 9.95, 467: 9.95, 468: 9.95, 469: 9.95, 470: 9.95, 471: 9.95, 472: 9.95, 473: 9.95, 474: 9.95, 475: 9.95, 476: 9.95, 477: 9.95, 478: 9.95, 479: 9.95, 480: 9.95, 481: 9.95, 482: 9.95, 483: 9.95, 484: 9.95, 485: 9.95, 486: 9.95, 487: 9.95, 488: 9.95, 489: 9.95, 490: 9.95, 491: 9.95, 492: 9.95, 493: 9.95, 494: 9.95, 495: 9.95, 496: 9.95, 497: 9.95, 498: 9.95, 499: 9.95, 500: 9.95, 501: 9.95, 502: 9.95, 503: 9.95, 504: 9.95, 505: 9.95, 506: 9.95, 507: 9.95, 508: 9.95, 509: 9.95, 510: 9.95, 511: 9.95, 512: 9.95, 513: 9.96, 514: 9.96, 515: 9.96, 516: 9.96, 517: 9.96, 518: 9.96, 519: 9.96, 520: 9.96, 521: 9.96, 522: 9.96, 523: 9.96, 524: 9.96, 525: 9.96, 526: 9.96, 527: 9.96, 528: 9.96, 529: 9.96, 530: 9.96, 531: 9.96, 532: 9.96, 533: 9.96, 534: 9.96, 535: 9.96, 536: 9.96, 537: 9.96, 538: 9.96, 539: 9.96, 540: 9.96, 541: 9.96, 542: 9.96, 543: 9.96, 544: 9.96, 545: 9.96, 546: 9.96, 547: 9.96, 548: 9.96, 549: 9.96, 550: 9.96, 551: 9.96, 552: 9.96, 553: 9.96, 554: 9.96, 555: 9.96, 556: 9.96, 557: 9.96, 558: 9.96, 559: 9.96, 560: 9.96, 561: 9.96, 562: 9.96, 563: 9.96, 564: 9.96, 565: 9.96, 566: 9.96, 567: 9.96, 568: 9.96, 569: 9.96, 570: 9.96, 571: 9.96, 572: 9.96, 573: 9.96, 574: 9.96, 575: 9.96, 576: 9.96, 577: 9.96, 578: 9.96, 579: 9.96, 580: 9.96, 581: 9.96, 582: 9.96, 583: 9.96, 584: 9.96, 585: 9.96, 586: 9.96, 587: 9.96, 588: 9.96, 589: 9.96, 590: 9.96, 591: 9.96, 592: 9.96, 593: 9.96, 594: 9.96, 595: 9.96, 596: 9.96, 597: 9.96, 598: 9.96, 599: 9.96, 600: 9.96, 601: 9.96, 602: 9.96, 603: 9.96, 604: 9.96, 605: 9.96, 606: 9.96, 607: 9.96, 608: 9.96, 609: 9.96, 610: 9.96, 611: 9.96, 612: 9.96, 613: 9.96, 614: 9.96, 615: 9.96, 616: 9.96, 617: 9.96, 618: 9.96, 619: 9.96, 620: 9.96, 621: 9.96, 622: 9.96, 623: 9.96, 624: 9.96, 625: 9.96, 626: 9.96, 627: 9.96, 628: 9.96, 629: 9.96, 630: 9.96, 631: 9.96, 632: 9.96, 633: 9.96, 634: 9.96, 635: 9.96, 636: 9.96, 637: 9.96, 638: 9.96, 639: 9.96, 640: 9.96, 641: 9.96, 642: 9.96, 643: 9.96, 644: 9.96, 645: 9.96, 646: 9.96, 647: 9.96, 648: 9.96, 649: 9.96, 650: 9.96, 651: 9.96, 652: 9.96, 653: 9.96, 654: 9.96, 655: 9.96, 656: 9.96, 657: 9.96, 658: 9.96, 659: 9.96, 660: 9.96, 661: 9.96, 662: 9.96, 663: 9.96, 664: 9.96, 665: 9.96, 666: 9.96, 667: 9.96, 668: 9.96, 669: 9.96, 670: 9.96, 671: 9.96, 672: 9.96, 673: 9.96, 674: 9.96, 675: 9.96, 676: 9.96, 677: 9.96, 678: 9.96, 679: 9.96, 680: 9.96, 681: 9.96, 682: 9.96, 683: 9.96, 684: 9.96, 685: 9.96, 686: 9.96, 687: 9.96, 688: 9.96, 689: 9.96, 690: 9.96, 691: 9.96, 692: 9.96, 693: 9.97, 694: 9.97, 695: 9.97, 696: 9.97, 697: 9.97, 698: 9.97, 699: 9.97, 700: 9.97, 701: 9.97, 702: 9.97, 703: 9.97, 704: 9.97, 705: 9.97, 706: 9.97, 707: 9.97, 708: 9.97, 709: 9.97, 710: 9.97, 711: 9.97, 712: 9.97, 713: 9.97, 714: 9.97, 715: 9.97, 716: 9.97, 717: 9.97, 718: 9.97, 719: 9.97, 720: 9.97, 721: 9.97, 722: 9.97, 723: 9.97, 724: 9.97, 725: 9.97, 726: 9.97, 727: 9.97, 728: 9.97, 729: 9.97, 730: 9.97, 731: 9.97, 732: 9.97, 733: 9.97, 734: 9.97, 735: 9.97, 736: 9.97, 737: 9.97, 738: 9.97, 739: 9.97, 740: 9.97, 741: 9.97, 742: 9.97, 743: 9.97, 744: 9.97, 745: 9.97, 746: 9.97, 747: 9.97, 748: 9.97, 749: 9.97, 750: 9.97, 751: 9.97, 752: 9.97, 753: 9.97, 754: 9.97, 755: 9.97, 756: 9.97, 757: 9.97, 758: 9.97, 759: 9.97, 760: 9.97, 761: 9.97, 762: 9.97, 763: 9.97, 764: 9.97, 765: 9.97, 766: 9.97, 767: 9.97, 768: 9.97, 769: 9.97, 770: 9.97, 771: 9.97, 772: 9.97, 773: 9.97, 774: 9.97, 775: 9.97, 776: 9.97, 777: 9.97, 778: 9.97, 779: 9.97, 780: 9.97, 781: 9.97, 782: 9.97, 783: 9.97, 784: 9.97, 785: 9.97, 786: 9.97, 787: 9.97, 788: 9.97, 789: 9.97, 790: 9.97, 791: 9.97, 792: 9.97, 793: 9.97, 794: 9.97, 795: 9.97, 796: 9.97, 797: 9.97, 798: 9.97, 799: 9.97, 800: 9.97, 801: 9.97, 802: 9.97, 803: 9.97, 804: 9.97, 805: 9.97, 806: 9.97, 807: 9.97, 808: 9.97, 809: 9.97, 810: 9.97, 811: 9.97, 812: 9.97, 813: 9.97, 814: 9.97, 815: 9.97, 816: 9.97, 817: 9.97, 818: 9.97, 819: 9.97, 820: 9.97, 821: 9.97, 822: 9.97, 823: 9.97, 824: 9.97, 825: 9.97, 826: 9.97, 827: 9.97, 828: 9.97, 829: 9.97, 830: 9.97, 831: 9.97, 832: 9.97, 833: 9.97, 834: 9.97, 835: 9.97, 836: 9.97, 837: 9.97, 838: 9.97, 839: 9.97, 840: 9.97, 841: 9.97, 842: 9.97, 843: 9.97, 844: 9.97, 845: 9.97, 846: 9.97, 847: 9.97, 848: 9.97, 849: 9.97, 850: 9.97, 851: 9.97, 852: 9.97, 853: 9.97, 854: 9.97, 855: 9.97, 856: 9.97, 857: 9.97, 858: 9.97, 859: 9.97, 860: 9.97, 861: 9.97, 862: 9.97, 863: 9.97, 864: 9.97, 865: 9.97, 866: 9.97, 867: 9.97, 868: 9.97, 869: 9.97, 870: 9.97, 871: 9.97, 872: 9.97, 873: 9.97, 874: 9.97, 875: 9.97, 876: 9.97, 877: 9.97, 878: 9.97, 879: 9.97, 880: 9.97, 881: 9.97, 882: 9.97, 883: 9.97, 884: 9.97, 885: 9.97, 886: 9.97, 887: 9.97, 888: 9.97, 889: 9.97, 890: 9.98, 891: 9.98, 892: 9.98, 893: 9.98, 894: 9.98, 895: 9.98, 896: 9.98, 897: 9.98, 898: 9.98, 899: 9.98, 900: 9.98, 901: 9.98, 902: 9.98, 903: 9.98, 904: 9.98, 905: 9.98, 906: 9.98, 907: 9.98, 908: 9.98, 909: 9.98, 910: 9.98, 911: 9.98, 912: 9.98, 913: 9.98, 914: 9.98, 915: 9.98, 916: 9.98, 917: 9.98, 918: 9.98, 919: 9.98, 920: 9.98, 921: 9.98, 922: 9.98, 923: 9.98, 924: 9.98, 925: 9.98, 926: 9.98, 927: 9.98, 928: 9.98, 929: 9.98, 930: 9.98, 931: 9.98, 932: 9.98, 933: 9.98, 934: 9.98, 935: 9.98, 936: 9.98, 937: 9.98, 938: 9.98, 939: 9.98, 940: 9.98, 941: 9.98, 942: 9.98, 943: 9.98, 944: 9.98, 945: 9.98, 946: 9.98, 947: 9.98, 948: 9.98, 949: 9.98, 950: 9.98, 951: 9.98, 952: 9.98, 953: 9.98, 954: 9.98, 955: 9.98, 956: 9.98, 957: 9.98, 958: 9.98, 959: 9.98, 960: 9.98, 961: 9.98, 962: 9.98, 963: 9.98, 964: 9.98, 965: 9.98, 966: 9.98, 967: 9.98, 968: 9.98, 969: 9.98, 970: 9.98, 971: 9.98, 972: 9.98, 973: 9.98, 974: 9.98, 975: 9.98, 976: 9.98, 977: 9.98, 978: 9.98, 979: 9.98, 980: 9.98, 981: 9.98, 982: 9.98, 983: 9.98, 984: 9.98, 985: 9.98, 986: 9.98, 987: 9.98, 988: 9.98, 989: 9.98, 990: 9.98, 991: 9.98, 992: 9.98, 993: 9.98, 994: 9.98, 995: 9.98, 996: 9.98, 997: 9.98, 998: 9.98, 999: 9.98}, 'GA, |Paths|=1': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0, 25: 0.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.0, 31: 0.0, 32: 0.0, 33: 0.0, 34: 0.0, 35: 0.0, 36: 0.0, 37: 0.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 0.0, 42: 0.0, 43: 0.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 0.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 0.0, 53: 0.0, 54: 0.0, 55: 0.0, 56: 0.0, 57: 0.0, 58: 0.0, 59: 0.0, 60: 0.0, 61: 0.0, 62: 0.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 0.0, 68: 0.0, 69: 0.0, 70: 0.0, 71: 0.0, 72: 0.0, 73: 0.0, 74: 0.0, 75: 0.0, 76: 0.0, 77: 0.0, 78: 0.0, 79: 0.0, 80: 0.0, 81: 0.0, 82: 0.0, 83: 0.0, 84: 0.0, 85: 0.0, 86: 0.0, 87: 0.0, 88: 0.0, 89: 0.0, 90: 0.0, 91: 0.0, 92: 0.0, 93: 0.0, 94: 0.0, 95: 0.0, 96: 0.0, 97: 0.0, 98: 0.0, 99: 0.0, 100: 0.0, 101: 0.0, 102: 0.0, 103: 0.0, 104: 0.0, 105: 0.0, 106: 0.0, 107: 0.0, 108: 0.0, 109: 0.0, 110: 0.0, 111: 0.0, 112: 0.0, 113: 0.0, 114: 0.0, 115: 0.0, 116: 0.0, 117: 0.0, 118: 0.0, 119: 0.0, 120: 0.0, 121: 0.0, 122: 0.0, 123: 0.0, 124: 0.0, 125: 0.0, 126: 0.0, 127: 0.0, 128: 0.0, 129: 0.0, 130: 0.0, 131: 0.0, 132: 0.0, 133: 0.0, 134: 0.0, 135: 0.0, 136: 0.0, 137: 0.0, 138: 0.0, 139: 0.0, 140: 0.0, 141: 0.0, 142: 0.0, 143: 0.0, 144: 0.0, 145: 0.0, 146: 0.0, 147: 0.0, 148: 0.0, 149: 0.0, 150: 0.0, 151: 0.0, 152: 0.0, 153: 0.0, 154: 0.0, 155: 0.0, 156: 0.0, 157: 0.0, 158: 0.0, 159: 0.0, 160: 0.0, 161: 0.0, 162: 0.0, 163: 0.0, 164: 0.0, 165: 0.0, 166: 0.0, 167: 0.0, 168: 0.0, 169: 0.0, 170: 0.0, 171: 0.0, 172: 0.0, 173: 0.0, 174: 0.0, 175: 0.0, 176: 0.0, 177: 0.0, 178: 0.0, 179: 0.0, 180: 0.0, 181: 0.0, 182: 0.0, 183: 0.0, 184: 0.0, 185: 0.0, 186: 0.0, 187: 0.0, 188: 0.0, 189: 0.0, 190: 0.0, 191: 0.0, 192: 0.0, 193: 0.0, 194: 0.0, 195: 0.0, 196: 0.0, 197: 0.0, 198: 0.0, 199: 0.0, 200: 0.0, 201: 0.0, 202: 0.0, 203: 0.0, 204: 0.0, 205: 0.0, 206: 0.0, 207: 0.0, 208: 0.0, 209: 0.0, 210: 0.0, 211: 0.0, 212: 0.0, 213: 0.0, 214: 0.0, 215: 0.0, 216: 0.0, 217: 0.0, 218: 0.0, 219: 0.0, 220: 0.0, 221: 0.0, 222: 0.0, 223: 0.0, 224: 0.0, 225: 0.0, 226: 0.0, 227: 0.0, 228: 0.0, 229: 0.0, 230: 0.0, 231: 0.0, 232: 0.0, 233: 0.0, 234: 0.0, 235: 0.0, 236: 0.0, 237: 0.0, 238: 0.0, 239: 0.0, 240: 0.0, 241: 0.0, 242: 0.0, 243: 0.0, 244: 0.0, 245: 0.0, 246: 0.0, 247: 0.0, 248: 0.0, 249: 0.0, 250: 0.0, 251: 0.0, 252: 0.0, 253: 0.0, 254: 0.0, 255: 0.0, 256: 0.0, 257: 0.0, 258: 0.0, 259: 0.0, 260: 0.0, 261: 0.0, 262: 0.0, 263: 0.0, 264: 0.0, 265: 0.0, 266: 0.0, 267: 0.0, 268: 0.0, 269: 0.0, 270: 0.0, 271: 0.0, 272: 0.0, 273: 0.0, 274: 0.0, 275: 0.0, 276: 0.0, 277: 0.0, 278: 0.0, 279: 0.0, 280: 0.0, 281: 0.0, 282: 0.0, 283: 0.0, 284: 0.0, 285: 0.0, 286: 0.0, 287: 0.0, 288: 0.0, 289: 0.0, 290: 0.0, 291: 0.0, 292: 0.0, 293: 0.0, 294: 0.0, 295: 0.0, 296: 0.0, 297: 0.0, 298: 0.0, 299: 0.0, 300: 0.0, 301: 0.0, 302: 0.0, 303: 0.0, 304: 0.0, 305: 0.0, 306: 0.0, 307: 0.0, 308: 0.0, 309: 0.0, 310: 0.0, 311: 0.0, 312: 0.0, 313: 0.0, 314: 0.0, 315: 0.0, 316: 0.0, 317: 0.0, 318: 0.0, 319: 0.0, 320: 0.0, 321: 0.0, 322: 0.0, 323: 0.0, 324: 0.0, 325: 0.0, 326: 0.0, 327: 0.0, 328: 0.0, 329: 0.0, 330: 0.0, 331: 0.0, 332: 0.0, 333: 0.0, 334: 0.0, 335: 0.0, 336: 0.0, 337: 0.0, 338: 0.0, 339: 0.0, 340: 0.0, 341: 0.0, 342: 0.0, 343: 0.0, 344: 0.0, 345: 0.0, 346: 0.0, 347: 0.0, 348: 0.0, 349: 0.0, 350: 0.0, 351: 0.0, 352: 0.0, 353: 0.0, 354: 0.0, 355: 0.0, 356: 0.0, 357: 0.0, 358: 0.0, 359: 0.0, 360: 0.0, 361: 0.0, 362: 0.0, 363: 0.0, 364: 0.0, 365: 0.0, 366: 0.0, 367: 0.0, 368: 0.0, 369: 0.0, 370: 0.0, 371: 0.0, 372: 0.0, 373: 0.0, 374: 0.0, 375: 0.0, 376: 0.0, 377: 0.0, 378: 0.0, 379: 0.0, 380: 0.0, 381: 0.0, 382: 0.0, 383: 0.0, 384: 0.0, 385: 0.0, 386: 0.0, 387: 0.0, 388: 0.0, 389: 0.0, 390: 0.0, 391: 0.0, 392: 0.0, 393: 0.0, 394: 0.0, 395: 0.0, 396: 0.0, 397: 0.0, 398: 0.0, 399: 0.0, 400: 0.0, 401: 0.0, 402: 0.0, 403: 0.0, 404: 0.0, 405: 0.0, 406: 0.0, 407: 0.0, 408: 0.0, 409: 0.0, 410: 0.0, 411: 0.0, 412: 0.0, 413: 0.0, 414: 0.0, 415: 0.0, 416: 0.0, 417: 0.0, 418: 0.0, 419: 0.0, 420: 0.0, 421: 0.0, 422: 0.0, 423: 0.0, 424: 0.0, 425: 0.0, 426: 0.0, 427: 0.0, 428: 0.0, 429: 0.0, 430: 0.0, 431: 0.0, 432: 0.0, 433: 0.0, 434: 0.0, 435: 0.0, 436: 0.0, 437: 0.0, 438: 0.0, 439: 0.0, 440: 0.0, 441: 0.0, 442: 0.0, 443: 0.0, 444: 0.0, 445: 0.0, 446: 0.0, 447: 0.0, 448: 0.0, 449: 0.0, 450: 0.0, 451: 0.0, 452: 0.0, 453: 0.0, 454: 0.0, 455: 0.0, 456: 0.0, 457: 0.0, 458: 0.0, 459: 0.0, 460: 0.0, 461: 0.0, 462: 0.0, 463: 0.0, 464: 0.0, 465: 0.0, 466: 0.0, 467: 0.0, 468: 0.0, 469: 0.0, 470: 0.0, 471: 0.0, 472: 0.0, 473: 0.0, 474: 0.0, 475: 0.0, 476: 0.0, 477: 0.0, 478: 0.0, 479: 0.0, 480: 0.0, 481: 0.0, 482: 0.0, 483: 0.0, 484: 0.0, 485: 0.0, 486: 0.0, 487: 0.0, 488: 0.0, 489: 0.0, 490: 0.0, 491: 0.0, 492: 0.0, 493: 0.0, 494: 0.0, 495: 0.0, 496: 0.0, 497: 0.0, 498: 0.0, 499: 0.0, 500: 0.0, 501: 0.0, 502: 0.0, 503: 0.0, 504: 0.0, 505: 0.0, 506: 0.0, 507: 0.0, 508: 0.0, 509: 0.0, 510: 0.0, 511: 0.0, 512: 0.0, 513: 0.0, 514: 0.0, 515: 0.0, 516: 0.0, 517: 0.0, 518: 0.0, 519: 0.0, 520: 0.0, 521: 0.0, 522: 0.0, 523: 0.0, 524: 0.0, 525: 0.0, 526: 0.0, 527: 0.0, 528: 0.0, 529: 0.0, 530: 0.0, 531: 0.0, 532: 0.0, 533: 0.0, 534: 0.0, 535: 0.0, 536: 0.0, 537: 0.0, 538: 0.0, 539: 0.0, 540: 0.0, 541: 0.0, 542: 0.0, 543: 0.0, 544: 0.0, 545: 0.0, 546: 0.0, 547: 0.0, 548: 0.0, 549: 0.0, 550: 0.0, 551: 0.0, 552: 0.0, 553: 0.0, 554: 0.0, 555: 0.0, 556: 0.0, 557: 0.0, 558: 0.0, 559: 0.0, 560: 0.0, 561: 0.0, 562: 0.0, 563: 0.0, 564: 0.0, 565: 0.0, 566: 0.0, 567: 0.0, 568: 0.0, 569: 0.0, 570: 0.0, 571: 0.0, 572: 0.0, 573: 0.0, 574: 0.0, 575: 0.0, 576: 0.0, 577: 0.0, 578: 0.0, 579: 0.0, 580: 0.0, 581: 0.0, 582: 0.0, 583: 0.0, 584: 0.0, 585: 0.0, 586: 0.0, 587: 0.0, 588: 0.0, 589: 0.0, 590: 0.0, 591: 0.0, 592: 0.0, 593: 0.0, 594: 0.0, 595: 0.0, 596: 0.0, 597: 0.0, 598: 0.0, 599: 0.0, 600: 0.0, 601: 0.0, 602: 0.0, 603: 0.0, 604: 0.0, 605: 0.0, 606: 0.0, 607: 0.0, 608: 0.0, 609: 0.0, 610: 0.0, 611: 0.0, 612: 0.0, 613: 0.0, 614: 0.0, 615: 0.0, 616: 0.0, 617: 0.0, 618: 0.0, 619: 0.0, 620: 0.0, 621: 0.0, 622: 0.0, 623: 0.0, 624: 0.0, 625: 0.0, 626: 0.0, 627: 0.0, 628: 0.0, 629: 0.0, 630: 0.0, 631: 0.0, 632: 0.0, 633: 0.0, 634: 0.0, 635: 0.0, 636: 0.0, 637: 0.0, 638: 0.0, 639: 0.0, 640: 0.0, 641: 0.0, 642: 0.0, 643: 0.0, 644: 0.0, 645: 0.0, 646: 0.0, 647: 0.0, 648: 0.0, 649: 0.0, 650: 0.0, 651: 0.0, 652: 0.0, 653: 0.0, 654: 0.0, 655: 0.0, 656: 0.0, 657: 0.0, 658: 0.0, 659: 0.0, 660: 0.0, 661: 0.0, 662: 0.0, 663: 0.0, 664: 0.0, 665: 0.0, 666: 0.0, 667: 0.0, 668: 0.0, 669: 0.0, 670: 0.0, 671: 0.0, 672: 0.0, 673: 0.0, 674: 0.0, 675: 0.0, 676: 0.0, 677: 0.0, 678: 0.0, 679: 0.0, 680: 0.0, 681: 0.0, 682: 0.0, 683: 0.0, 684: 0.0, 685: 0.0, 686: 0.0, 687: 0.0, 688: 0.0, 689: 0.0, 690: 0.0, 691: 0.0, 692: 0.0, 693: 0.0, 694: 0.0, 695: 0.0, 696: 0.0, 697: 0.0, 698: 0.0, 699: 0.0, 700: 0.0, 701: 0.0, 702: 0.0, 703: 0.0, 704: 0.0, 705: 0.0, 706: 0.0, 707: 0.0, 708: 0.0, 709: 0.0, 710: 0.0, 711: 0.0, 712: 0.0, 713: 0.0, 714: 0.0, 715: 0.0, 716: 0.0, 717: 0.0, 718: 0.0, 719: 0.0, 720: 0.0, 721: 0.0, 722: 0.0, 723: 0.0, 724: 0.0, 725: 0.0, 726: 0.0, 727: 0.0, 728: 0.0, 729: 0.0, 730: 0.0, 731: 0.0, 732: 0.0, 733: 0.0, 734: 0.0, 735: 0.0, 736: 0.0, 737: 0.0, 738: 0.0, 739: 0.0, 740: 0.0, 741: 0.0, 742: 0.0, 743: 0.0, 744: 0.0, 745: 0.0, 746: 0.0, 747: 0.0, 748: 0.0, 749: 0.0, 750: 0.0, 751: 0.0, 752: 0.0, 753: 0.0, 754: 0.0, 755: 0.0, 756: 0.0, 757: 0.0, 758: 0.0, 759: 0.0, 760: 0.0, 761: 0.0, 762: 0.0, 763: 0.0, 764: 0.0, 765: 0.0, 766: 0.0, 767: 0.0, 768: 0.0, 769: 0.0, 770: 0.0, 771: 0.0, 772: 0.0, 773: 0.0, 774: 0.0, 775: 0.0, 776: 0.0, 777: 0.0, 778: 0.0, 779: 0.0, 780: 0.0, 781: 0.0, 782: 0.0, 783: 0.0, 784: 0.0, 785: 0.0, 786: 0.0, 787: 0.0, 788: 0.0, 789: 0.0, 790: 0.0, 791: 0.0, 792: 0.0, 793: 0.0, 794: 0.0, 795: 0.0, 796: 0.0, 797: 0.0, 798: 0.0, 799: 0.0, 800: 0.0, 801: 0.0, 802: 0.0, 803: 0.0, 804: 0.0, 805: 0.0, 806: 0.0, 807: 0.0, 808: 0.0, 809: 0.0, 810: 0.0, 811: 0.0, 812: 0.0, 813: 0.0, 814: 0.0, 815: 0.0, 816: 0.0, 817: 0.0, 818: 0.0, 819: 0.0, 820: 0.0, 821: 0.0, 822: 0.0, 823: 0.0, 824: 0.0, 825: 0.0, 826: 0.0, 827: 0.0, 828: 0.0, 829: 0.0, 830: 0.0, 831: 0.0, 832: 0.0, 833: 0.0, 834: 0.0, 835: 0.0, 836: 0.0, 837: 0.0, 838: 0.0, 839: 0.0, 840: 0.0, 841: 0.0, 842: 0.0, 843: 0.0, 844: 0.0, 845: 0.0, 846: 0.0, 847: 0.0, 848: 0.0, 849: 0.0, 850: 0.0, 851: 0.0, 852: 0.0, 853: 0.0, 854: 0.0, 855: 0.0, 856: 0.0, 857: 0.0, 858: 0.0, 859: 0.0, 860: 0.0, 861: 0.0, 862: 0.0, 863: 0.0, 864: 0.0, 865: 0.0, 866: 0.0, 867: 0.0, 868: 0.0, 869: 0.0, 870: 0.0, 871: 0.0, 872: 0.0, 873: 0.0, 874: 0.0, 875: 0.0, 876: 0.0, 877: 0.0, 878: 0.0, 879: 0.0, 880: 0.0, 881: 0.0, 882: 0.0, 883: 0.0, 884: 0.0, 885: 0.0, 886: 0.0, 887: 0.0, 888: 0.0, 889: 0.0, 890: 0.0, 891: 0.0, 892: 0.0, 893: 0.0, 894: 0.0, 895: 0.0, 896: 0.0, 897: 0.0, 898: 0.0, 899: 0.0, 900: 0.0, 901: 0.0, 902: 0.0, 903: 0.0, 904: 0.0, 905: 0.0, 906: 0.0, 907: 0.0, 908: 0.0, 909: 0.0, 910: 0.0, 911: 0.0, 912: 0.0, 913: 0.0, 914: 0.0, 915: 0.0, 916: 0.0, 917: 0.0, 918: 0.0, 919: 0.0, 920: 0.0, 921: 0.0, 922: 0.0, 923: 0.0, 924: 0.0, 925: 0.0, 926: 0.0, 927: 0.0, 928: 0.0, 929: 0.0, 930: 0.0, 931: 0.0, 932: 0.0, 933: 0.0, 934: 0.0, 935: 0.0, 936: 0.0, 937: 0.0, 938: 0.0, 939: 0.0, 940: 0.0, 941: 0.0, 942: 0.0, 943: 0.0, 944: 0.0, 945: 0.0, 946: 0.0, 947: 0.0, 948: 0.0, 949: 0.0, 950: 0.0, 951: 0.0, 952: 0.0, 953: 0.0, 954: 0.0, 955: 0.0, 956: 0.0, 957: 0.0, 958: 0.0, 959: 0.0, 960: 0.0, 961: 0.0, 962: 0.0, 963: 0.0, 964: 0.0, 965: 0.0, 966: 0.0, 967: 0.0, 968: 0.0, 969: 0.0, 970: 0.0, 971: 0.0, 972: 0.0, 973: 0.0, 974: 0.0, 975: 0.0, 976: 0.0, 977: 0.0, 978: 0.0, 979: 0.0, 980: 0.0, 981: 0.0, 982: 0.0, 983: 0.0, 984: 0.0, 985: 0.0, 986: 0.0, 987: 0.0, 988: 0.0, 989: 0.0, 990: 0.0, 991: 0.0, 992: 0.0, 993: 0.0, 994: 0.0, 995: 0.0, 996: 0.0, 997: 0.0, 998: 0.0, 999: 0.0}, 'Hop-based shortest path, |Paths|=3': {1: 7.492439999999999, 0: 7.492439999999999, 2: 7.492439999999999, 3: 7.492439999999999, 4: 7.492439999999999, 5: 7.492439999999999, 6: 7.492439999999999, 7: 7.492439999999999, 8: 7.492439999999999, 9: 7.492439999999999, 10: 7.492439999999999, 11: 7.492439999999999, 12: 7.492439999999999, 13: 7.492439999999999, 14: 7.492439999999999, 15: 7.492439999999999, 16: 7.492439999999999, 17: 7.492439999999999, 18: 7.492439999999999, 19: 7.492439999999999, 20: 7.492439999999999, 21: 7.492439999999999, 22: 7.492439999999999, 23: 7.492439999999999, 24: 7.492439999999999, 25: 7.492439999999999, 26: 7.492439999999999, 27: 7.492439999999999, 28: 7.492439999999999, 29: 7.492439999999999, 30: 7.492439999999999, 31: 7.492439999999999, 32: 7.492439999999999, 33: 7.492439999999999, 34: 7.492439999999999, 35: 7.492439999999999, 36: 7.492439999999999, 37: 7.492439999999999, 38: 7.492439999999999, 39: 7.492439999999999, 40: 7.492439999999999, 41: 7.492439999999999, 42: 7.492439999999999, 43: 7.492439999999999, 44: 7.492439999999999, 45: 7.492439999999999, 46: 7.492439999999999, 47: 7.492439999999999, 48: 7.492439999999999, 49: 7.492439999999999, 50: 7.492439999999999, 51: 7.492439999999999, 52: 7.492439999999999, 53: 7.492439999999999, 54: 7.492439999999999, 55: 7.492439999999999, 56: 7.492439999999999, 57: 7.492439999999999, 58: 7.492439999999999, 59: 7.492439999999999, 60: 7.492439999999999, 61: 7.492439999999999, 62: 7.492439999999999, 63: 7.492439999999999, 64: 7.492439999999999, 65: 7.492439999999999, 66: 7.492439999999999, 67: 7.492439999999999, 68: 7.492439999999999, 69: 7.492439999999999, 70: 7.492439999999999, 71: 7.492439999999999, 72: 7.492439999999999, 73: 7.492439999999999, 74: 7.492439999999999, 75: 7.492439999999999, 76: 7.492439999999999, 77: 7.492439999999999, 78: 7.492439999999999, 79: 7.492439999999999, 80: 7.492439999999999, 81: 7.492439999999999, 82: 7.492439999999999, 83: 7.492439999999999, 84: 7.492439999999999, 85: 7.492439999999999, 86: 7.492439999999999, 87: 7.492439999999999, 88: 7.492439999999999, 89: 7.492439999999999, 90: 7.492439999999999, 91: 7.492439999999999, 92: 7.492439999999999, 93: 7.492439999999999, 94: 7.492439999999999, 95: 7.492439999999999, 96: 7.492439999999999, 97: 7.492439999999999, 98: 7.492439999999999, 99: 7.492439999999999, 100: 7.492439999999999, 101: 7.492439999999999, 102: 7.492439999999999, 103: 7.492439999999999, 104: 7.492439999999999, 105: 7.492439999999999, 106: 7.492439999999999, 107: 7.492439999999999, 108: 7.492439999999999, 109: 7.492439999999999, 110: 7.492439999999999, 111: 7.492439999999999, 112: 7.492439999999999, 113: 7.492439999999999, 114: 7.492439999999999, 115: 7.492439999999999, 116: 7.492439999999999, 117: 7.492439999999999, 118: 7.492439999999999, 119: 7.492439999999999, 120: 7.492439999999999, 121: 7.492439999999999, 122: 7.492439999999999, 123: 7.492439999999999, 124: 7.492439999999999, 125: 7.492439999999999, 126: 7.492439999999999, 127: 7.492439999999999, 128: 7.492439999999999, 129: 7.492439999999999, 130: 7.492439999999999, 131: 7.492439999999999, 132: 7.492439999999999, 133: 7.492439999999999, 134: 7.492439999999999, 135: 7.492439999999999, 136: 7.492439999999999, 137: 7.492439999999999, 138: 7.492439999999999, 139: 7.492439999999999, 140: 7.492439999999999, 141: 7.492439999999999, 142: 7.492439999999999, 143: 7.492439999999999, 144: 7.492439999999999, 145: 7.492439999999999, 146: 7.492439999999999, 147: 7.492439999999999, 148: 7.492439999999999, 149: 7.492439999999999, 150: 7.492439999999999, 151: 7.492439999999999, 152: 7.492439999999999, 153: 7.492439999999999, 154: 7.492439999999999, 155: 7.492439999999999, 156: 7.492439999999999, 157: 7.492439999999999, 158: 7.492439999999999, 159: 7.492439999999999, 160: 7.492439999999999, 161: 7.492439999999999, 162: 7.492439999999999, 163: 7.492439999999999, 164: 7.492439999999999, 165: 7.492439999999999, 166: 7.492439999999999, 167: 7.492439999999999, 168: 7.492439999999999, 169: 7.492439999999999, 170: 7.492439999999999, 171: 7.492439999999999, 172: 7.492439999999999, 173: 7.492439999999999, 174: 7.492439999999999, 175: 7.492439999999999, 176: 7.492439999999999, 177: 7.492439999999999, 178: 7.492439999999999, 179: 7.492439999999999, 180: 7.492439999999999, 181: 7.492439999999999, 182: 7.492439999999999, 183: 7.492439999999999, 184: 7.492439999999999, 185: 7.492439999999999, 186: 7.492439999999999, 187: 7.492439999999999, 188: 7.492439999999999, 189: 7.492439999999999, 190: 7.492439999999999, 191: 7.492439999999999, 192: 7.492439999999999, 193: 7.492439999999999, 194: 7.492439999999999, 195: 7.492439999999999, 196: 7.492439999999999, 197: 7.492439999999999, 198: 7.492439999999999, 199: 7.492439999999999, 200: 7.492439999999999, 201: 7.492439999999999, 202: 7.492439999999999, 203: 7.492439999999999, 204: 7.492439999999999, 205: 7.492439999999999, 206: 7.492439999999999, 207: 7.492439999999999, 208: 7.492439999999999, 209: 7.492439999999999, 210: 7.492439999999999, 211: 7.492439999999999, 212: 7.492439999999999, 213: 7.492439999999999, 214: 7.492439999999999, 215: 7.492439999999999, 216: 7.492439999999999, 217: 7.492439999999999, 218: 7.492439999999999, 219: 7.492439999999999, 220: 7.492439999999999, 221: 7.492439999999999, 222: 7.492439999999999, 223: 7.492439999999999, 224: 7.492439999999999, 225: 7.492439999999999, 226: 7.492439999999999, 227: 7.492439999999999, 228: 7.492439999999999, 229: 7.492439999999999, 230: 7.492439999999999, 231: 7.492439999999999, 232: 7.492439999999999, 233: 7.492439999999999, 234: 7.492439999999999, 235: 7.492439999999999, 236: 7.492439999999999, 237: 7.492439999999999, 238: 7.492439999999999, 239: 7.492439999999999, 240: 7.492439999999999, 241: 7.492439999999999, 242: 7.492439999999999, 243: 7.492439999999999, 244: 7.492439999999999, 245: 7.492439999999999, 246: 7.492439999999999, 247: 7.492439999999999, 248: 7.492439999999999, 249: 7.492439999999999, 250: 7.492439999999999, 251: 7.492439999999999, 252: 7.492439999999999, 253: 7.492439999999999, 254: 7.492439999999999, 255: 7.492439999999999, 256: 7.492439999999999, 257: 7.492439999999999, 258: 7.492439999999999, 259: 7.492439999999999, 260: 7.492439999999999, 261: 7.492439999999999, 262: 7.492439999999999, 263: 7.492439999999999, 264: 7.492439999999999, 265: 7.492439999999999, 266: 7.492439999999999, 267: 7.492439999999999, 268: 7.492439999999999, 269: 7.492439999999999, 270: 7.492439999999999, 271: 7.492439999999999, 272: 7.492439999999999, 273: 7.492439999999999, 274: 7.492439999999999, 275: 7.492439999999999, 276: 7.492439999999999, 277: 7.492439999999999, 278: 7.492439999999999, 279: 7.492439999999999, 280: 7.492439999999999, 281: 7.492439999999999, 282: 7.492439999999999, 283: 7.492439999999999, 284: 7.492439999999999, 285: 7.492439999999999, 286: 7.492439999999999, 287: 7.492439999999999, 288: 7.492439999999999, 289: 7.492439999999999, 290: 7.492439999999999, 291: 7.492439999999999, 292: 7.492439999999999, 293: 7.492439999999999, 294: 7.492439999999999, 295: 7.492439999999999, 296: 7.492439999999999, 297: 7.492439999999999, 298: 7.492439999999999, 299: 7.492439999999999, 300: 7.492439999999999, 301: 7.492439999999999, 302: 7.492439999999999, 303: 7.492439999999999, 304: 7.492439999999999, 305: 7.492439999999999, 306: 7.492439999999999, 307: 7.492439999999999, 308: 7.492439999999999, 309: 7.492439999999999, 310: 7.492439999999999, 311: 7.492439999999999, 312: 7.492439999999999, 313: 7.492439999999999, 314: 7.492439999999999, 315: 7.492439999999999, 316: 7.492439999999999, 317: 7.492439999999999, 318: 7.492439999999999, 319: 7.492439999999999, 320: 7.492439999999999, 321: 7.492439999999999, 322: 7.492439999999999, 323: 7.492439999999999, 324: 7.492439999999999, 325: 7.492439999999999, 326: 7.492439999999999, 327: 7.492439999999999, 328: 7.492439999999999, 329: 7.492439999999999, 330: 7.492439999999999, 331: 7.492439999999999, 332: 7.492439999999999, 333: 7.492439999999999, 334: 7.492439999999999, 335: 7.492439999999999, 336: 7.492439999999999, 337: 7.492439999999999, 338: 7.492439999999999, 339: 7.492439999999999, 340: 7.492439999999999, 341: 7.492439999999999, 342: 7.492439999999999, 343: 7.492439999999999, 344: 7.492439999999999, 345: 7.492439999999999, 346: 7.492439999999999, 347: 7.492439999999999, 348: 7.492439999999999, 349: 7.492439999999999, 350: 7.492439999999999, 351: 7.492439999999999, 352: 7.492439999999999, 353: 7.492439999999999, 354: 7.492439999999999, 355: 7.492439999999999, 356: 7.492439999999999, 357: 7.492439999999999, 358: 7.492439999999999, 359: 7.492439999999999, 360: 7.492439999999999, 361: 7.492439999999999, 362: 7.492439999999999, 363: 7.492439999999999, 364: 7.492439999999999, 365: 7.492439999999999, 366: 7.492439999999999, 367: 7.492439999999999, 368: 7.492439999999999, 369: 7.492439999999999, 370: 7.492439999999999, 371: 7.492439999999999, 372: 7.492439999999999, 373: 7.492439999999999, 374: 7.492439999999999, 375: 7.492439999999999, 376: 7.492439999999999, 377: 7.492439999999999, 378: 7.492439999999999, 379: 7.492439999999999, 380: 7.492439999999999, 381: 7.492439999999999, 382: 7.492439999999999, 383: 7.492439999999999, 384: 7.492439999999999, 385: 7.492439999999999, 386: 7.492439999999999, 387: 7.492439999999999, 388: 7.492439999999999, 389: 7.492439999999999, 390: 7.492439999999999, 391: 7.492439999999999, 392: 7.492439999999999, 393: 7.492439999999999, 394: 7.492439999999999, 395: 7.492439999999999, 396: 7.492439999999999, 397: 7.492439999999999, 398: 7.492439999999999, 399: 7.492439999999999, 400: 7.492439999999999, 401: 7.492439999999999, 402: 7.492439999999999, 403: 7.492439999999999, 404: 7.492439999999999, 405: 7.492439999999999, 406: 7.492439999999999, 407: 7.492439999999999, 408: 7.492439999999999, 409: 7.492439999999999, 410: 7.492439999999999, 411: 7.492439999999999, 412: 7.492439999999999, 413: 7.492439999999999, 414: 7.492439999999999, 415: 7.492439999999999, 416: 7.492439999999999, 417: 7.492439999999999, 418: 7.492439999999999, 419: 7.492439999999999, 420: 7.492439999999999, 421: 7.492439999999999, 422: 7.492439999999999, 423: 7.492439999999999, 424: 7.492439999999999, 425: 7.492439999999999, 426: 7.492439999999999, 427: 7.492439999999999, 428: 7.492439999999999, 429: 7.492439999999999, 430: 7.492439999999999, 431: 7.492439999999999, 432: 7.492439999999999, 433: 7.492439999999999, 434: 7.492439999999999, 435: 7.492439999999999, 436: 7.492439999999999, 437: 7.492439999999999, 438: 7.492439999999999, 439: 7.492439999999999, 440: 7.492439999999999, 441: 7.492439999999999, 442: 7.492439999999999, 443: 7.492439999999999, 444: 7.492439999999999, 445: 7.492439999999999, 446: 7.492439999999999, 447: 7.492439999999999, 448: 7.492439999999999, 449: 7.492439999999999, 450: 7.492439999999999, 451: 7.492439999999999, 452: 7.492439999999999, 453: 7.492439999999999, 454: 7.492439999999999, 455: 7.492439999999999, 456: 7.492439999999999, 457: 7.492439999999999, 458: 7.492439999999999, 459: 7.492439999999999, 460: 7.492439999999999, 461: 7.492439999999999, 462: 7.492439999999999, 463: 7.492439999999999, 464: 7.492439999999999, 465: 7.492439999999999, 466: 7.492439999999999, 467: 7.492439999999999, 468: 7.492439999999999, 469: 7.492439999999999, 470: 7.492439999999999, 471: 7.492439999999999, 472: 7.492439999999999, 473: 7.492439999999999, 474: 7.492439999999999, 475: 7.492439999999999, 476: 7.492439999999999, 477: 7.492439999999999, 478: 7.492439999999999, 479: 7.492439999999999, 480: 7.492439999999999, 481: 7.492439999999999, 482: 7.492439999999999, 483: 7.492439999999999, 484: 7.492439999999999, 485: 7.492439999999999, 486: 7.492439999999999, 487: 7.492439999999999, 488: 7.492439999999999, 489: 7.492439999999999, 490: 7.492439999999999, 491: 7.492439999999999, 492: 7.492439999999999, 493: 7.492439999999999, 494: 7.492439999999999, 495: 7.492439999999999, 496: 7.492439999999999, 497: 7.492439999999999, 498: 7.492439999999999, 499: 7.492439999999999, 500: 7.492439999999999, 501: 7.492439999999999, 502: 7.492439999999999, 503: 7.492439999999999, 504: 7.492439999999999, 505: 7.492439999999999, 506: 7.492439999999999, 507: 7.492439999999999, 508: 7.492439999999999, 509: 7.492439999999999, 510: 7.492439999999999, 511: 7.492439999999999, 512: 7.492439999999999, 513: 7.492439999999999, 514: 7.492439999999999, 515: 7.492439999999999, 516: 7.492439999999999, 517: 7.492439999999999, 518: 7.492439999999999, 519: 7.492439999999999, 520: 7.492439999999999, 521: 7.492439999999999, 522: 7.492439999999999, 523: 7.492439999999999, 524: 7.492439999999999, 525: 7.492439999999999, 526: 7.492439999999999, 527: 7.492439999999999, 528: 7.492439999999999, 529: 7.492439999999999, 530: 7.492439999999999, 531: 7.492439999999999, 532: 7.492439999999999, 533: 7.492439999999999, 534: 7.492439999999999, 535: 7.492439999999999, 536: 7.492439999999999, 537: 7.492439999999999, 538: 7.492439999999999, 539: 7.492439999999999, 540: 7.492439999999999, 541: 7.492439999999999, 542: 7.492439999999999, 543: 7.492439999999999, 544: 7.492439999999999, 545: 7.492439999999999, 546: 7.492439999999999, 547: 7.492439999999999, 548: 7.492439999999999, 549: 7.492439999999999, 550: 7.492439999999999, 551: 7.492439999999999, 552: 7.492439999999999, 553: 7.492439999999999, 554: 7.492439999999999, 555: 7.492439999999999, 556: 7.492439999999999, 557: 7.492439999999999, 558: 7.492439999999999, 559: 7.492439999999999, 560: 7.492439999999999, 561: 7.492439999999999, 562: 7.492439999999999, 563: 7.492439999999999, 564: 7.492439999999999, 565: 7.492439999999999, 566: 7.492439999999999, 567: 7.492439999999999, 568: 7.492439999999999, 569: 7.492439999999999, 570: 7.492439999999999, 571: 7.492439999999999, 572: 7.492439999999999, 573: 7.492439999999999, 574: 7.492439999999999, 575: 7.492439999999999, 576: 7.492439999999999, 577: 7.492439999999999, 578: 7.492439999999999, 579: 7.492439999999999, 580: 7.492439999999999, 581: 7.492439999999999, 582: 7.492439999999999, 583: 7.492439999999999, 584: 7.492439999999999, 585: 7.492439999999999, 586: 7.492439999999999, 587: 7.492439999999999, 588: 7.492439999999999, 589: 7.492439999999999, 590: 7.492439999999999, 591: 7.492439999999999, 592: 7.492439999999999, 593: 7.492439999999999, 594: 7.492439999999999, 595: 7.492439999999999, 596: 7.492439999999999, 597: 7.492439999999999, 598: 7.492439999999999, 599: 7.492439999999999, 600: 7.492439999999999, 601: 7.492439999999999, 602: 7.492439999999999, 603: 7.492439999999999, 604: 7.492439999999999, 605: 7.492439999999999, 606: 7.492439999999999, 607: 7.492439999999999, 608: 7.492439999999999, 609: 7.492439999999999, 610: 7.492439999999999, 611: 7.492439999999999, 612: 7.492439999999999, 613: 7.492439999999999, 614: 7.492439999999999, 615: 7.492439999999999, 616: 7.492439999999999, 617: 7.492439999999999, 618: 7.492439999999999, 619: 7.492439999999999, 620: 7.492439999999999, 621: 7.492439999999999, 622: 7.492439999999999, 623: 7.492439999999999, 624: 7.492439999999999, 625: 7.492439999999999, 626: 7.492439999999999, 627: 7.492439999999999, 628: 7.492439999999999, 629: 7.492439999999999, 630: 7.492439999999999, 631: 7.492439999999999, 632: 7.492439999999999, 633: 7.492439999999999, 634: 7.492439999999999, 635: 7.492439999999999, 636: 7.492439999999999, 637: 7.492439999999999, 638: 7.492439999999999, 639: 7.492439999999999, 640: 7.492439999999999, 641: 7.492439999999999, 642: 7.492439999999999, 643: 7.492439999999999, 644: 7.492439999999999, 645: 7.492439999999999, 646: 7.492439999999999, 647: 7.492439999999999, 648: 7.492439999999999, 649: 7.492439999999999, 650: 7.492439999999999, 651: 7.492439999999999, 652: 7.492439999999999, 653: 7.492439999999999, 654: 7.492439999999999, 655: 7.492439999999999, 656: 7.492439999999999, 657: 7.492439999999999, 658: 7.492439999999999, 659: 7.492439999999999, 660: 7.492439999999999, 661: 7.492439999999999, 662: 7.492439999999999, 663: 7.492439999999999, 664: 7.492439999999999, 665: 7.492439999999999, 666: 7.492439999999999, 667: 7.492439999999999, 668: 7.492439999999999, 669: 7.492439999999999, 670: 7.492439999999999, 671: 7.492439999999999, 672: 7.492439999999999, 673: 7.492439999999999, 674: 7.492439999999999, 675: 7.492439999999999, 676: 7.492439999999999, 677: 7.492439999999999, 678: 7.492439999999999, 679: 7.492439999999999, 680: 7.492439999999999, 681: 7.492439999999999, 682: 7.492439999999999, 683: 7.492439999999999, 684: 7.492439999999999, 685: 7.492439999999999, 686: 7.492439999999999, 687: 7.492439999999999, 688: 7.492439999999999, 689: 7.492439999999999, 690: 7.492439999999999, 691: 7.492439999999999, 692: 7.492439999999999, 693: 7.492439999999999, 694: 7.492439999999999, 695: 7.492439999999999, 696: 7.492439999999999, 697: 7.492439999999999, 698: 7.492439999999999, 699: 7.492439999999999, 700: 7.492439999999999, 701: 7.492439999999999, 702: 7.492439999999999, 703: 7.492439999999999, 704: 7.492439999999999, 705: 7.492439999999999, 706: 7.492439999999999, 707: 7.492439999999999, 708: 7.492439999999999, 709: 7.492439999999999, 710: 7.492439999999999, 711: 7.492439999999999, 712: 7.492439999999999, 713: 7.492439999999999, 714: 7.492439999999999, 715: 7.492439999999999, 716: 7.492439999999999, 717: 7.492439999999999, 718: 7.492439999999999, 719: 7.492439999999999, 720: 7.492439999999999, 721: 7.492439999999999, 722: 7.492439999999999, 723: 7.492439999999999, 724: 7.492439999999999, 725: 7.492439999999999, 726: 7.492439999999999, 727: 7.492439999999999, 728: 7.492439999999999, 729: 7.492439999999999, 730: 7.492439999999999, 731: 7.492439999999999, 732: 7.492439999999999, 733: 7.492439999999999, 734: 7.492439999999999, 735: 7.492439999999999, 736: 7.492439999999999, 737: 7.492439999999999, 738: 7.492439999999999, 739: 7.492439999999999, 740: 7.492439999999999, 741: 7.492439999999999, 742: 7.492439999999999, 743: 7.492439999999999, 744: 7.492439999999999, 745: 7.492439999999999, 746: 7.492439999999999, 747: 7.492439999999999, 748: 7.492439999999999, 749: 7.492439999999999, 750: 7.492439999999999, 751: 7.492439999999999, 752: 7.492439999999999, 753: 7.492439999999999, 754: 7.492439999999999, 755: 7.492439999999999, 756: 7.492439999999999, 757: 7.492439999999999, 758: 7.492439999999999, 759: 7.492439999999999, 760: 7.492439999999999, 761: 7.492439999999999, 762: 7.492439999999999, 763: 7.492439999999999, 764: 7.492439999999999, 765: 7.492439999999999, 766: 7.492439999999999, 767: 7.492439999999999, 768: 7.492439999999999, 769: 7.492439999999999, 770: 7.492439999999999, 771: 7.492439999999999, 772: 7.492439999999999, 773: 7.492439999999999, 774: 7.492439999999999, 775: 7.492439999999999, 776: 7.492439999999999, 777: 7.492439999999999, 778: 7.492439999999999, 779: 7.492439999999999, 780: 7.492439999999999, 781: 7.492439999999999, 782: 7.492439999999999, 783: 7.492439999999999, 784: 7.492439999999999, 785: 7.492439999999999, 786: 7.492439999999999, 787: 7.492439999999999, 788: 7.492439999999999, 789: 7.492439999999999, 790: 7.492439999999999, 791: 7.492439999999999, 792: 7.492439999999999, 793: 7.492439999999999, 794: 7.492439999999999, 795: 7.492439999999999, 796: 7.492439999999999, 797: 7.492439999999999, 798: 7.492439999999999, 799: 7.492439999999999, 800: 7.492439999999999, 801: 7.492439999999999, 802: 7.492439999999999, 803: 7.492439999999999, 804: 7.492439999999999, 805: 7.492439999999999, 806: 7.492439999999999, 807: 7.492439999999999, 808: 7.492439999999999, 809: 7.492439999999999, 810: 7.492439999999999, 811: 7.492439999999999, 812: 7.492439999999999, 813: 7.492439999999999, 814: 7.492439999999999, 815: 7.492439999999999, 816: 7.492439999999999, 817: 7.492439999999999, 818: 7.492439999999999, 819: 7.492439999999999, 820: 7.492439999999999, 821: 7.492439999999999, 822: 7.492439999999999, 823: 7.492439999999999, 824: 7.492439999999999, 825: 7.492439999999999, 826: 7.492439999999999, 827: 7.492439999999999, 828: 7.492439999999999, 829: 7.492439999999999, 830: 7.492439999999999, 831: 7.492439999999999, 832: 7.492439999999999, 833: 7.492439999999999, 834: 7.492439999999999, 835: 7.492439999999999, 836: 7.492439999999999, 837: 7.492439999999999, 838: 7.492439999999999, 839: 7.492439999999999, 840: 7.492439999999999, 841: 7.492439999999999, 842: 7.492439999999999, 843: 7.492439999999999, 844: 7.492439999999999, 845: 7.492439999999999, 846: 7.492439999999999, 847: 7.492439999999999, 848: 7.492439999999999, 849: 7.492439999999999, 850: 7.492439999999999, 851: 7.492439999999999, 852: 7.492439999999999, 853: 7.492439999999999, 854: 7.492439999999999, 855: 7.492439999999999, 856: 7.492439999999999, 857: 7.492439999999999, 858: 7.492439999999999, 859: 7.492439999999999, 860: 7.492439999999999, 861: 7.492439999999999, 862: 7.492439999999999, 863: 7.492439999999999, 864: 7.492439999999999, 865: 7.492439999999999, 866: 7.492439999999999, 867: 7.492439999999999, 868: 7.492439999999999, 869: 7.492439999999999, 870: 7.492439999999999, 871: 7.492439999999999, 872: 7.492439999999999, 873: 7.492439999999999, 874: 7.492439999999999, 875: 7.492439999999999, 876: 7.492439999999999, 877: 7.492439999999999, 878: 7.492439999999999, 879: 7.492439999999999, 880: 7.492439999999999, 881: 7.492439999999999, 882: 7.492439999999999, 883: 7.492439999999999, 884: 7.492439999999999, 885: 7.492439999999999, 886: 7.492439999999999, 887: 7.492439999999999, 888: 7.492439999999999, 889: 7.492439999999999, 890: 7.492439999999999, 891: 7.492439999999999, 892: 7.492439999999999, 893: 7.492439999999999, 894: 7.492439999999999, 895: 7.492439999999999, 896: 7.492439999999999, 897: 7.492439999999999, 898: 7.492439999999999, 899: 7.492439999999999, 900: 7.492439999999999, 901: 7.492439999999999, 902: 7.492439999999999, 903: 7.492439999999999, 904: 7.492439999999999, 905: 7.492439999999999, 906: 7.492439999999999, 907: 7.492439999999999, 908: 7.492439999999999, 909: 7.492439999999999, 910: 7.492439999999999, 911: 7.492439999999999, 912: 7.492439999999999, 913: 7.492439999999999, 914: 7.492439999999999, 915: 7.492439999999999, 916: 7.492439999999999, 917: 7.492439999999999, 918: 7.492439999999999, 919: 7.492439999999999, 920: 7.492439999999999, 921: 7.492439999999999, 922: 7.492439999999999, 923: 7.492439999999999, 924: 7.492439999999999, 925: 7.492439999999999, 926: 7.492439999999999, 927: 7.492439999999999, 928: 7.492439999999999, 929: 7.492439999999999, 930: 7.492439999999999, 931: 7.492439999999999, 932: 7.492439999999999, 933: 7.492439999999999, 934: 7.492439999999999, 935: 7.492439999999999, 936: 7.492439999999999, 937: 7.492439999999999, 938: 7.492439999999999, 939: 7.492439999999999, 940: 7.492439999999999, 941: 7.492439999999999, 942: 7.492439999999999, 943: 7.492439999999999, 944: 7.492439999999999, 945: 7.492439999999999, 946: 7.492439999999999, 947: 7.492439999999999, 948: 7.492439999999999, 949: 7.492439999999999, 950: 7.492439999999999, 951: 7.492439999999999, 952: 7.492439999999999, 953: 7.492439999999999, 954: 7.492439999999999, 955: 7.492439999999999, 956: 7.492439999999999, 957: 7.492439999999999, 958: 7.492439999999999, 959: 7.492439999999999, 960: 7.492439999999999, 961: 7.492439999999999, 962: 7.492439999999999, 963: 7.492439999999999, 964: 7.492439999999999, 965: 7.492439999999999, 966: 7.492439999999999, 967: 7.492439999999999, 968: 7.492439999999999, 969: 7.492439999999999, 970: 7.492439999999999, 971: 7.492439999999999, 972: 7.492439999999999, 973: 7.492439999999999, 974: 7.492439999999999, 975: 7.492439999999999, 976: 7.492439999999999, 977: 7.492439999999999, 978: 7.492439999999999, 979: 7.492439999999999, 980: 7.492439999999999, 981: 7.492439999999999, 982: 7.492439999999999, 983: 7.492439999999999, 984: 7.492439999999999, 985: 7.492439999999999, 986: 7.492439999999999, 987: 7.492439999999999, 988: 7.492439999999999, 989: 7.492439999999999, 990: 7.492439999999999, 991: 7.492439999999999, 992: 7.492439999999999, 993: 7.492439999999999, 994: 7.492439999999999, 995: 7.492439999999999, 996: 7.492439999999999, 997: 7.492439999999999, 998: 7.492439999999999, 999: 7.492439999999999}, 'Hop-based shortest path, |Paths|=1': {1: 0.0, 0: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0, 25: 0.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.0, 31: 0.0, 32: 0.0, 33: 0.0, 34: 0.0, 35: 0.0, 36: 0.0, 37: 0.0, 38: 0.0, 39: 0.0, 40: 0.0, 41: 0.0, 42: 0.0, 43: 0.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 0.0, 49: 0.0, 50: 0.0, 51: 0.0, 52: 0.0, 53: 0.0, 54: 0.0, 55: 0.0, 56: 0.0, 57: 0.0, 58: 0.0, 59: 0.0, 60: 0.0, 61: 0.0, 62: 0.0, 63: 0.0, 64: 0.0, 65: 0.0, 66: 0.0, 67: 0.0, 68: 0.0, 69: 0.0, 70: 0.0, 71: 0.0, 72: 0.0, 73: 0.0, 74: 0.0, 75: 0.0, 76: 0.0, 77: 0.0, 78: 0.0, 79: 0.0, 80: 0.0, 81: 0.0, 82: 0.0, 83: 0.0, 84: 0.0, 85: 0.0, 86: 0.0, 87: 0.0, 88: 0.0, 89: 0.0, 90: 0.0, 91: 0.0, 92: 0.0, 93: 0.0, 94: 0.0, 95: 0.0, 96: 0.0, 97: 0.0, 98: 0.0, 99: 0.0, 100: 0.0, 101: 0.0, 102: 0.0, 103: 0.0, 104: 0.0, 105: 0.0, 106: 0.0, 107: 0.0, 108: 0.0, 109: 0.0, 110: 0.0, 111: 0.0, 112: 0.0, 113: 0.0, 114: 0.0, 115: 0.0, 116: 0.0, 117: 0.0, 118: 0.0, 119: 0.0, 120: 0.0, 121: 0.0, 122: 0.0, 123: 0.0, 124: 0.0, 125: 0.0, 126: 0.0, 127: 0.0, 128: 0.0, 129: 0.0, 130: 0.0, 131: 0.0, 132: 0.0, 133: 0.0, 134: 0.0, 135: 0.0, 136: 0.0, 137: 0.0, 138: 0.0, 139: 0.0, 140: 0.0, 141: 0.0, 142: 0.0, 143: 0.0, 144: 0.0, 145: 0.0, 146: 0.0, 147: 0.0, 148: 0.0, 149: 0.0, 150: 0.0, 151: 0.0, 152: 0.0, 153: 0.0, 154: 0.0, 155: 0.0, 156: 0.0, 157: 0.0, 158: 0.0, 159: 0.0, 160: 0.0, 161: 0.0, 162: 0.0, 163: 0.0, 164: 0.0, 165: 0.0, 166: 0.0, 167: 0.0, 168: 0.0, 169: 0.0, 170: 0.0, 171: 0.0, 172: 0.0, 173: 0.0, 174: 0.0, 175: 0.0, 176: 0.0, 177: 0.0, 178: 0.0, 179: 0.0, 180: 0.0, 181: 0.0, 182: 0.0, 183: 0.0, 184: 0.0, 185: 0.0, 186: 0.0, 187: 0.0, 188: 0.0, 189: 0.0, 190: 0.0, 191: 0.0, 192: 0.0, 193: 0.0, 194: 0.0, 195: 0.0, 196: 0.0, 197: 0.0, 198: 0.0, 199: 0.0, 200: 0.0, 201: 0.0, 202: 0.0, 203: 0.0, 204: 0.0, 205: 0.0, 206: 0.0, 207: 0.0, 208: 0.0, 209: 0.0, 210: 0.0, 211: 0.0, 212: 0.0, 213: 0.0, 214: 0.0, 215: 0.0, 216: 0.0, 217: 0.0, 218: 0.0, 219: 0.0, 220: 0.0, 221: 0.0, 222: 0.0, 223: 0.0, 224: 0.0, 225: 0.0, 226: 0.0, 227: 0.0, 228: 0.0, 229: 0.0, 230: 0.0, 231: 0.0, 232: 0.0, 233: 0.0, 234: 0.0, 235: 0.0, 236: 0.0, 237: 0.0, 238: 0.0, 239: 0.0, 240: 0.0, 241: 0.0, 242: 0.0, 243: 0.0, 244: 0.0, 245: 0.0, 246: 0.0, 247: 0.0, 248: 0.0, 249: 0.0, 250: 0.0, 251: 0.0, 252: 0.0, 253: 0.0, 254: 0.0, 255: 0.0, 256: 0.0, 257: 0.0, 258: 0.0, 259: 0.0, 260: 0.0, 261: 0.0, 262: 0.0, 263: 0.0, 264: 0.0, 265: 0.0, 266: 0.0, 267: 0.0, 268: 0.0, 269: 0.0, 270: 0.0, 271: 0.0, 272: 0.0, 273: 0.0, 274: 0.0, 275: 0.0, 276: 0.0, 277: 0.0, 278: 0.0, 279: 0.0, 280: 0.0, 281: 0.0, 282: 0.0, 283: 0.0, 284: 0.0, 285: 0.0, 286: 0.0, 287: 0.0, 288: 0.0, 289: 0.0, 290: 0.0, 291: 0.0, 292: 0.0, 293: 0.0, 294: 0.0, 295: 0.0, 296: 0.0, 297: 0.0, 298: 0.0, 299: 0.0, 300: 0.0, 301: 0.0, 302: 0.0, 303: 0.0, 304: 0.0, 305: 0.0, 306: 0.0, 307: 0.0, 308: 0.0, 309: 0.0, 310: 0.0, 311: 0.0, 312: 0.0, 313: 0.0, 314: 0.0, 315: 0.0, 316: 0.0, 317: 0.0, 318: 0.0, 319: 0.0, 320: 0.0, 321: 0.0, 322: 0.0, 323: 0.0, 324: 0.0, 325: 0.0, 326: 0.0, 327: 0.0, 328: 0.0, 329: 0.0, 330: 0.0, 331: 0.0, 332: 0.0, 333: 0.0, 334: 0.0, 335: 0.0, 336: 0.0, 337: 0.0, 338: 0.0, 339: 0.0, 340: 0.0, 341: 0.0, 342: 0.0, 343: 0.0, 344: 0.0, 345: 0.0, 346: 0.0, 347: 0.0, 348: 0.0, 349: 0.0, 350: 0.0, 351: 0.0, 352: 0.0, 353: 0.0, 354: 0.0, 355: 0.0, 356: 0.0, 357: 0.0, 358: 0.0, 359: 0.0, 360: 0.0, 361: 0.0, 362: 0.0, 363: 0.0, 364: 0.0, 365: 0.0, 366: 0.0, 367: 0.0, 368: 0.0, 369: 0.0, 370: 0.0, 371: 0.0, 372: 0.0, 373: 0.0, 374: 0.0, 375: 0.0, 376: 0.0, 377: 0.0, 378: 0.0, 379: 0.0, 380: 0.0, 381: 0.0, 382: 0.0, 383: 0.0, 384: 0.0, 385: 0.0, 386: 0.0, 387: 0.0, 388: 0.0, 389: 0.0, 390: 0.0, 391: 0.0, 392: 0.0, 393: 0.0, 394: 0.0, 395: 0.0, 396: 0.0, 397: 0.0, 398: 0.0, 399: 0.0, 400: 0.0, 401: 0.0, 402: 0.0, 403: 0.0, 404: 0.0, 405: 0.0, 406: 0.0, 407: 0.0, 408: 0.0, 409: 0.0, 410: 0.0, 411: 0.0, 412: 0.0, 413: 0.0, 414: 0.0, 415: 0.0, 416: 0.0, 417: 0.0, 418: 0.0, 419: 0.0, 420: 0.0, 421: 0.0, 422: 0.0, 423: 0.0, 424: 0.0, 425: 0.0, 426: 0.0, 427: 0.0, 428: 0.0, 429: 0.0, 430: 0.0, 431: 0.0, 432: 0.0, 433: 0.0, 434: 0.0, 435: 0.0, 436: 0.0, 437: 0.0, 438: 0.0, 439: 0.0, 440: 0.0, 441: 0.0, 442: 0.0, 443: 0.0, 444: 0.0, 445: 0.0, 446: 0.0, 447: 0.0, 448: 0.0, 449: 0.0, 450: 0.0, 451: 0.0, 452: 0.0, 453: 0.0, 454: 0.0, 455: 0.0, 456: 0.0, 457: 0.0, 458: 0.0, 459: 0.0, 460: 0.0, 461: 0.0, 462: 0.0, 463: 0.0, 464: 0.0, 465: 0.0, 466: 0.0, 467: 0.0, 468: 0.0, 469: 0.0, 470: 0.0, 471: 0.0, 472: 0.0, 473: 0.0, 474: 0.0, 475: 0.0, 476: 0.0, 477: 0.0, 478: 0.0, 479: 0.0, 480: 0.0, 481: 0.0, 482: 0.0, 483: 0.0, 484: 0.0, 485: 0.0, 486: 0.0, 487: 0.0, 488: 0.0, 489: 0.0, 490: 0.0, 491: 0.0, 492: 0.0, 493: 0.0, 494: 0.0, 495: 0.0, 496: 0.0, 497: 0.0, 498: 0.0, 499: 0.0, 500: 0.0, 501: 0.0, 502: 0.0, 503: 0.0, 504: 0.0, 505: 0.0, 506: 0.0, 507: 0.0, 508: 0.0, 509: 0.0, 510: 0.0, 511: 0.0, 512: 0.0, 513: 0.0, 514: 0.0, 515: 0.0, 516: 0.0, 517: 0.0, 518: 0.0, 519: 0.0, 520: 0.0, 521: 0.0, 522: 0.0, 523: 0.0, 524: 0.0, 525: 0.0, 526: 0.0, 527: 0.0, 528: 0.0, 529: 0.0, 530: 0.0, 531: 0.0, 532: 0.0, 533: 0.0, 534: 0.0, 535: 0.0, 536: 0.0, 537: 0.0, 538: 0.0, 539: 0.0, 540: 0.0, 541: 0.0, 542: 0.0, 543: 0.0, 544: 0.0, 545: 0.0, 546: 0.0, 547: 0.0, 548: 0.0, 549: 0.0, 550: 0.0, 551: 0.0, 552: 0.0, 553: 0.0, 554: 0.0, 555: 0.0, 556: 0.0, 557: 0.0, 558: 0.0, 559: 0.0, 560: 0.0, 561: 0.0, 562: 0.0, 563: 0.0, 564: 0.0, 565: 0.0, 566: 0.0, 567: 0.0, 568: 0.0, 569: 0.0, 570: 0.0, 571: 0.0, 572: 0.0, 573: 0.0, 574: 0.0, 575: 0.0, 576: 0.0, 577: 0.0, 578: 0.0, 579: 0.0, 580: 0.0, 581: 0.0, 582: 0.0, 583: 0.0, 584: 0.0, 585: 0.0, 586: 0.0, 587: 0.0, 588: 0.0, 589: 0.0, 590: 0.0, 591: 0.0, 592: 0.0, 593: 0.0, 594: 0.0, 595: 0.0, 596: 0.0, 597: 0.0, 598: 0.0, 599: 0.0, 600: 0.0, 601: 0.0, 602: 0.0, 603: 0.0, 604: 0.0, 605: 0.0, 606: 0.0, 607: 0.0, 608: 0.0, 609: 0.0, 610: 0.0, 611: 0.0, 612: 0.0, 613: 0.0, 614: 0.0, 615: 0.0, 616: 0.0, 617: 0.0, 618: 0.0, 619: 0.0, 620: 0.0, 621: 0.0, 622: 0.0, 623: 0.0, 624: 0.0, 625: 0.0, 626: 0.0, 627: 0.0, 628: 0.0, 629: 0.0, 630: 0.0, 631: 0.0, 632: 0.0, 633: 0.0, 634: 0.0, 635: 0.0, 636: 0.0, 637: 0.0, 638: 0.0, 639: 0.0, 640: 0.0, 641: 0.0, 642: 0.0, 643: 0.0, 644: 0.0, 645: 0.0, 646: 0.0, 647: 0.0, 648: 0.0, 649: 0.0, 650: 0.0, 651: 0.0, 652: 0.0, 653: 0.0, 654: 0.0, 655: 0.0, 656: 0.0, 657: 0.0, 658: 0.0, 659: 0.0, 660: 0.0, 661: 0.0, 662: 0.0, 663: 0.0, 664: 0.0, 665: 0.0, 666: 0.0, 667: 0.0, 668: 0.0, 669: 0.0, 670: 0.0, 671: 0.0, 672: 0.0, 673: 0.0, 674: 0.0, 675: 0.0, 676: 0.0, 677: 0.0, 678: 0.0, 679: 0.0, 680: 0.0, 681: 0.0, 682: 0.0, 683: 0.0, 684: 0.0, 685: 0.0, 686: 0.0, 687: 0.0, 688: 0.0, 689: 0.0, 690: 0.0, 691: 0.0, 692: 0.0, 693: 0.0, 694: 0.0, 695: 0.0, 696: 0.0, 697: 0.0, 698: 0.0, 699: 0.0, 700: 0.0, 701: 0.0, 702: 0.0, 703: 0.0, 704: 0.0, 705: 0.0, 706: 0.0, 707: 0.0, 708: 0.0, 709: 0.0, 710: 0.0, 711: 0.0, 712: 0.0, 713: 0.0, 714: 0.0, 715: 0.0, 716: 0.0, 717: 0.0, 718: 0.0, 719: 0.0, 720: 0.0, 721: 0.0, 722: 0.0, 723: 0.0, 724: 0.0, 725: 0.0, 726: 0.0, 727: 0.0, 728: 0.0, 729: 0.0, 730: 0.0, 731: 0.0, 732: 0.0, 733: 0.0, 734: 0.0, 735: 0.0, 736: 0.0, 737: 0.0, 738: 0.0, 739: 0.0, 740: 0.0, 741: 0.0, 742: 0.0, 743: 0.0, 744: 0.0, 745: 0.0, 746: 0.0, 747: 0.0, 748: 0.0, 749: 0.0, 750: 0.0, 751: 0.0, 752: 0.0, 753: 0.0, 754: 0.0, 755: 0.0, 756: 0.0, 757: 0.0, 758: 0.0, 759: 0.0, 760: 0.0, 761: 0.0, 762: 0.0, 763: 0.0, 764: 0.0, 765: 0.0, 766: 0.0, 767: 0.0, 768: 0.0, 769: 0.0, 770: 0.0, 771: 0.0, 772: 0.0, 773: 0.0, 774: 0.0, 775: 0.0, 776: 0.0, 777: 0.0, 778: 0.0, 779: 0.0, 780: 0.0, 781: 0.0, 782: 0.0, 783: 0.0, 784: 0.0, 785: 0.0, 786: 0.0, 787: 0.0, 788: 0.0, 789: 0.0, 790: 0.0, 791: 0.0, 792: 0.0, 793: 0.0, 794: 0.0, 795: 0.0, 796: 0.0, 797: 0.0, 798: 0.0, 799: 0.0, 800: 0.0, 801: 0.0, 802: 0.0, 803: 0.0, 804: 0.0, 805: 0.0, 806: 0.0, 807: 0.0, 808: 0.0, 809: 0.0, 810: 0.0, 811: 0.0, 812: 0.0, 813: 0.0, 814: 0.0, 815: 0.0, 816: 0.0, 817: 0.0, 818: 0.0, 819: 0.0, 820: 0.0, 821: 0.0, 822: 0.0, 823: 0.0, 824: 0.0, 825: 0.0, 826: 0.0, 827: 0.0, 828: 0.0, 829: 0.0, 830: 0.0, 831: 0.0, 832: 0.0, 833: 0.0, 834: 0.0, 835: 0.0, 836: 0.0, 837: 0.0, 838: 0.0, 839: 0.0, 840: 0.0, 841: 0.0, 842: 0.0, 843: 0.0, 844: 0.0, 845: 0.0, 846: 0.0, 847: 0.0, 848: 0.0, 849: 0.0, 850: 0.0, 851: 0.0, 852: 0.0, 853: 0.0, 854: 0.0, 855: 0.0, 856: 0.0, 857: 0.0, 858: 0.0, 859: 0.0, 860: 0.0, 861: 0.0, 862: 0.0, 863: 0.0, 864: 0.0, 865: 0.0, 866: 0.0, 867: 0.0, 868: 0.0, 869: 0.0, 870: 0.0, 871: 0.0, 872: 0.0, 873: 0.0, 874: 0.0, 875: 0.0, 876: 0.0, 877: 0.0, 878: 0.0, 879: 0.0, 880: 0.0, 881: 0.0, 882: 0.0, 883: 0.0, 884: 0.0, 885: 0.0, 886: 0.0, 887: 0.0, 888: 0.0, 889: 0.0, 890: 0.0, 891: 0.0, 892: 0.0, 893: 0.0, 894: 0.0, 895: 0.0, 896: 0.0, 897: 0.0, 898: 0.0, 899: 0.0, 900: 0.0, 901: 0.0, 902: 0.0, 903: 0.0, 904: 0.0, 905: 0.0, 906: 0.0, 907: 0.0, 908: 0.0, 909: 0.0, 910: 0.0, 911: 0.0, 912: 0.0, 913: 0.0, 914: 0.0, 915: 0.0, 916: 0.0, 917: 0.0, 918: 0.0, 919: 0.0, 920: 0.0, 921: 0.0, 922: 0.0, 923: 0.0, 924: 0.0, 925: 0.0, 926: 0.0, 927: 0.0, 928: 0.0, 929: 0.0, 930: 0.0, 931: 0.0, 932: 0.0, 933: 0.0, 934: 0.0, 935: 0.0, 936: 0.0, 937: 0.0, 938: 0.0, 939: 0.0, 940: 0.0, 941: 0.0, 942: 0.0, 943: 0.0, 944: 0.0, 945: 0.0, 946: 0.0, 947: 0.0, 948: 0.0, 949: 0.0, 950: 0.0, 951: 0.0, 952: 0.0, 953: 0.0, 954: 0.0, 955: 0.0, 956: 0.0, 957: 0.0, 958: 0.0, 959: 0.0, 960: 0.0, 961: 0.0, 962: 0.0, 963: 0.0, 964: 0.0, 965: 0.0, 966: 0.0, 967: 0.0, 968: 0.0, 969: 0.0, 970: 0.0, 971: 0.0, 972: 0.0, 973: 0.0, 974: 0.0, 975: 0.0, 976: 0.0, 977: 0.0, 978: 0.0, 979: 0.0, 980: 0.0, 981: 0.0, 982: 0.0, 983: 0.0, 984: 0.0, 985: 0.0, 986: 0.0, 987: 0.0, 988: 0.0, 989: 0.0, 990: 0.0, 991: 0.0, 992: 0.0, 993: 0.0, 994: 0.0, 995: 0.0, 996: 0.0, 997: 0.0, 998: 0.0, 999: 0.0}, 'Hop-based shortest path, |Paths|=6': {1: 8.439073333333333, 0: 8.439073333333333, 2: 8.439073333333333, 3: 8.439073333333333, 4: 8.439073333333333, 5: 8.439073333333333, 6: 8.439073333333333, 7: 8.439073333333333, 8: 8.439073333333333, 9: 8.439073333333333, 10: 8.439073333333333, 11: 8.439073333333333, 12: 8.439073333333333, 13: 8.439073333333333, 14: 8.439073333333333, 15: 8.439073333333333, 16: 8.439073333333333, 17: 8.439073333333333, 18: 8.439073333333333, 19: 8.439073333333333, 20: 8.439073333333333, 21: 8.439073333333333, 22: 8.439073333333333, 23: 8.439073333333333, 24: 8.439073333333333, 25: 8.439073333333333, 26: 8.439073333333333, 27: 8.439073333333333, 28: 8.439073333333333, 29: 8.439073333333333, 30: 8.439073333333333, 31: 8.439073333333333, 32: 8.439073333333333, 33: 8.439073333333333, 34: 8.439073333333333, 35: 8.439073333333333, 36: 8.439073333333333, 37: 8.439073333333333, 38: 8.439073333333333, 39: 8.439073333333333, 40: 8.439073333333333, 41: 8.439073333333333, 42: 8.439073333333333, 43: 8.439073333333333, 44: 8.439073333333333, 45: 8.439073333333333, 46: 8.439073333333333, 47: 8.439073333333333, 48: 8.439073333333333, 49: 8.439073333333333, 50: 8.439073333333333, 51: 8.439073333333333, 52: 8.439073333333333, 53: 8.439073333333333, 54: 8.439073333333333, 55: 8.439073333333333, 56: 8.439073333333333, 57: 8.439073333333333, 58: 8.439073333333333, 59: 8.439073333333333, 60: 8.439073333333333, 61: 8.439073333333333, 62: 8.439073333333333, 63: 8.439073333333333, 64: 8.439073333333333, 65: 8.439073333333333, 66: 8.439073333333333, 67: 8.439073333333333, 68: 8.439073333333333, 69: 8.439073333333333, 70: 8.439073333333333, 71: 8.439073333333333, 72: 8.439073333333333, 73: 8.439073333333333, 74: 8.439073333333333, 75: 8.439073333333333, 76: 8.439073333333333, 77: 8.439073333333333, 78: 8.439073333333333, 79: 8.439073333333333, 80: 8.439073333333333, 81: 8.439073333333333, 82: 8.439073333333333, 83: 8.439073333333333, 84: 8.439073333333333, 85: 8.439073333333333, 86: 8.439073333333333, 87: 8.439073333333333, 88: 8.439073333333333, 89: 8.439073333333333, 90: 8.439073333333333, 91: 8.439073333333333, 92: 8.439073333333333, 93: 8.439073333333333, 94: 8.439073333333333, 95: 8.439073333333333, 96: 8.439073333333333, 97: 8.439073333333333, 98: 8.439073333333333, 99: 8.439073333333333, 100: 8.439073333333333, 101: 8.439073333333333, 102: 8.439073333333333, 103: 8.439073333333333, 104: 8.439073333333333, 105: 8.439073333333333, 106: 8.439073333333333, 107: 8.439073333333333, 108: 8.439073333333333, 109: 8.439073333333333, 110: 8.439073333333333, 111: 8.439073333333333, 112: 8.439073333333333, 113: 8.439073333333333, 114: 8.439073333333333, 115: 8.439073333333333, 116: 8.439073333333333, 117: 8.439073333333333, 118: 8.439073333333333, 119: 8.439073333333333, 120: 8.439073333333333, 121: 8.439073333333333, 122: 8.439073333333333, 123: 8.439073333333333, 124: 8.439073333333333, 125: 8.439073333333333, 126: 8.439073333333333, 127: 8.439073333333333, 128: 8.439073333333333, 129: 8.439073333333333, 130: 8.439073333333333, 131: 8.439073333333333, 132: 8.439073333333333, 133: 8.439073333333333, 134: 8.439073333333333, 135: 8.439073333333333, 136: 8.439073333333333, 137: 8.439073333333333, 138: 8.439073333333333, 139: 8.439073333333333, 140: 8.439073333333333, 141: 8.439073333333333, 142: 8.439073333333333, 143: 8.439073333333333, 144: 8.439073333333333, 145: 8.439073333333333, 146: 8.439073333333333, 147: 8.439073333333333, 148: 8.439073333333333, 149: 8.439073333333333, 150: 8.439073333333333, 151: 8.439073333333333, 152: 8.439073333333333, 153: 8.439073333333333, 154: 8.439073333333333, 155: 8.439073333333333, 156: 8.439073333333333, 157: 8.439073333333333, 158: 8.439073333333333, 159: 8.439073333333333, 160: 8.439073333333333, 161: 8.439073333333333, 162: 8.439073333333333, 163: 8.439073333333333, 164: 8.439073333333333, 165: 8.439073333333333, 166: 8.439073333333333, 167: 8.439073333333333, 168: 8.439073333333333, 169: 8.439073333333333, 170: 8.439073333333333, 171: 8.439073333333333, 172: 8.439073333333333, 173: 8.439073333333333, 174: 8.439073333333333, 175: 8.439073333333333, 176: 8.439073333333333, 177: 8.439073333333333, 178: 8.439073333333333, 179: 8.439073333333333, 180: 8.439073333333333, 181: 8.439073333333333, 182: 8.439073333333333, 183: 8.439073333333333, 184: 8.439073333333333, 185: 8.439073333333333, 186: 8.439073333333333, 187: 8.439073333333333, 188: 8.439073333333333, 189: 8.439073333333333, 190: 8.439073333333333, 191: 8.439073333333333, 192: 8.439073333333333, 193: 8.439073333333333, 194: 8.439073333333333, 195: 8.439073333333333, 196: 8.439073333333333, 197: 8.439073333333333, 198: 8.439073333333333, 199: 8.439073333333333, 200: 8.439073333333333, 201: 8.439073333333333, 202: 8.439073333333333, 203: 8.439073333333333, 204: 8.439073333333333, 205: 8.439073333333333, 206: 8.439073333333333, 207: 8.439073333333333, 208: 8.439073333333333, 209: 8.439073333333333, 210: 8.439073333333333, 211: 8.439073333333333, 212: 8.439073333333333, 213: 8.439073333333333, 214: 8.439073333333333, 215: 8.439073333333333, 216: 8.439073333333333, 217: 8.439073333333333, 218: 8.439073333333333, 219: 8.439073333333333, 220: 8.439073333333333, 221: 8.439073333333333, 222: 8.439073333333333, 223: 8.439073333333333, 224: 8.439073333333333, 225: 8.439073333333333, 226: 8.439073333333333, 227: 8.439073333333333, 228: 8.439073333333333, 229: 8.439073333333333, 230: 8.439073333333333, 231: 8.439073333333333, 232: 8.439073333333333, 233: 8.439073333333333, 234: 8.439073333333333, 235: 8.439073333333333, 236: 8.439073333333333, 237: 8.439073333333333, 238: 8.439073333333333, 239: 8.439073333333333, 240: 8.439073333333333, 241: 8.439073333333333, 242: 8.439073333333333, 243: 8.439073333333333, 244: 8.439073333333333, 245: 8.439073333333333, 246: 8.439073333333333, 247: 8.439073333333333, 248: 8.439073333333333, 249: 8.439073333333333, 250: 8.439073333333333, 251: 8.439073333333333, 252: 8.439073333333333, 253: 8.439073333333333, 254: 8.439073333333333, 255: 8.439073333333333, 256: 8.439073333333333, 257: 8.439073333333333, 258: 8.439073333333333, 259: 8.439073333333333, 260: 8.439073333333333, 261: 8.439073333333333, 262: 8.439073333333333, 263: 8.439073333333333, 264: 8.439073333333333, 265: 8.439073333333333, 266: 8.439073333333333, 267: 8.439073333333333, 268: 8.439073333333333, 269: 8.439073333333333, 270: 8.439073333333333, 271: 8.439073333333333, 272: 8.439073333333333, 273: 8.439073333333333, 274: 8.439073333333333, 275: 8.439073333333333, 276: 8.439073333333333, 277: 8.439073333333333, 278: 8.439073333333333, 279: 8.439073333333333, 280: 8.439073333333333, 281: 8.439073333333333, 282: 8.439073333333333, 283: 8.439073333333333, 284: 8.439073333333333, 285: 8.439073333333333, 286: 8.439073333333333, 287: 8.439073333333333, 288: 8.439073333333333, 289: 8.439073333333333, 290: 8.439073333333333, 291: 8.439073333333333, 292: 8.439073333333333, 293: 8.439073333333333, 294: 8.439073333333333, 295: 8.439073333333333, 296: 8.439073333333333, 297: 8.439073333333333, 298: 8.439073333333333, 299: 8.439073333333333, 300: 8.439073333333333, 301: 8.439073333333333, 302: 8.439073333333333, 303: 8.439073333333333, 304: 8.439073333333333, 305: 8.439073333333333, 306: 8.439073333333333, 307: 8.439073333333333, 308: 8.439073333333333, 309: 8.439073333333333, 310: 8.439073333333333, 311: 8.439073333333333, 312: 8.439073333333333, 313: 8.439073333333333, 314: 8.439073333333333, 315: 8.439073333333333, 316: 8.439073333333333, 317: 8.439073333333333, 318: 8.439073333333333, 319: 8.439073333333333, 320: 8.439073333333333, 321: 8.439073333333333, 322: 8.439073333333333, 323: 8.439073333333333, 324: 8.439073333333333, 325: 8.439073333333333, 326: 8.439073333333333, 327: 8.439073333333333, 328: 8.439073333333333, 329: 8.439073333333333, 330: 8.439073333333333, 331: 8.439073333333333, 332: 8.439073333333333, 333: 8.439073333333333, 334: 8.439073333333333, 335: 8.439073333333333, 336: 8.439073333333333, 337: 8.439073333333333, 338: 8.439073333333333, 339: 8.439073333333333, 340: 8.439073333333333, 341: 8.439073333333333, 342: 8.439073333333333, 343: 8.439073333333333, 344: 8.439073333333333, 345: 8.439073333333333, 346: 8.439073333333333, 347: 8.439073333333333, 348: 8.439073333333333, 349: 8.439073333333333, 350: 8.439073333333333, 351: 8.439073333333333, 352: 8.439073333333333, 353: 8.439073333333333, 354: 8.439073333333333, 355: 8.439073333333333, 356: 8.439073333333333, 357: 8.439073333333333, 358: 8.439073333333333, 359: 8.439073333333333, 360: 8.439073333333333, 361: 8.439073333333333, 362: 8.439073333333333, 363: 8.439073333333333, 364: 8.439073333333333, 365: 8.439073333333333, 366: 8.439073333333333, 367: 8.439073333333333, 368: 8.439073333333333, 369: 8.439073333333333, 370: 8.439073333333333, 371: 8.439073333333333, 372: 8.439073333333333, 373: 8.439073333333333, 374: 8.439073333333333, 375: 8.439073333333333, 376: 8.439073333333333, 377: 8.439073333333333, 378: 8.439073333333333, 379: 8.439073333333333, 380: 8.439073333333333, 381: 8.439073333333333, 382: 8.439073333333333, 383: 8.439073333333333, 384: 8.439073333333333, 385: 8.439073333333333, 386: 8.439073333333333, 387: 8.439073333333333, 388: 8.439073333333333, 389: 8.439073333333333, 390: 8.439073333333333, 391: 8.439073333333333, 392: 8.439073333333333, 393: 8.439073333333333, 394: 8.439073333333333, 395: 8.439073333333333, 396: 8.439073333333333, 397: 8.439073333333333, 398: 8.439073333333333, 399: 8.439073333333333, 400: 8.439073333333333, 401: 8.439073333333333, 402: 8.439073333333333, 403: 8.439073333333333, 404: 8.439073333333333, 405: 8.439073333333333, 406: 8.439073333333333, 407: 8.439073333333333, 408: 8.439073333333333, 409: 8.439073333333333, 410: 8.439073333333333, 411: 8.439073333333333, 412: 8.439073333333333, 413: 8.439073333333333, 414: 8.439073333333333, 415: 8.439073333333333, 416: 8.439073333333333, 417: 8.439073333333333, 418: 8.439073333333333, 419: 8.439073333333333, 420: 8.439073333333333, 421: 8.439073333333333, 422: 8.439073333333333, 423: 8.439073333333333, 424: 8.439073333333333, 425: 8.439073333333333, 426: 8.439073333333333, 427: 8.439073333333333, 428: 8.439073333333333, 429: 8.439073333333333, 430: 8.439073333333333, 431: 8.439073333333333, 432: 8.439073333333333, 433: 8.439073333333333, 434: 8.439073333333333, 435: 8.439073333333333, 436: 8.439073333333333, 437: 8.439073333333333, 438: 8.439073333333333, 439: 8.439073333333333, 440: 8.439073333333333, 441: 8.439073333333333, 442: 8.439073333333333, 443: 8.439073333333333, 444: 8.439073333333333, 445: 8.439073333333333, 446: 8.439073333333333, 447: 8.439073333333333, 448: 8.439073333333333, 449: 8.439073333333333, 450: 8.439073333333333, 451: 8.439073333333333, 452: 8.439073333333333, 453: 8.439073333333333, 454: 8.439073333333333, 455: 8.439073333333333, 456: 8.439073333333333, 457: 8.439073333333333, 458: 8.439073333333333, 459: 8.439073333333333, 460: 8.439073333333333, 461: 8.439073333333333, 462: 8.439073333333333, 463: 8.439073333333333, 464: 8.439073333333333, 465: 8.439073333333333, 466: 8.439073333333333, 467: 8.439073333333333, 468: 8.439073333333333, 469: 8.439073333333333, 470: 8.439073333333333, 471: 8.439073333333333, 472: 8.439073333333333, 473: 8.439073333333333, 474: 8.439073333333333, 475: 8.439073333333333, 476: 8.439073333333333, 477: 8.439073333333333, 478: 8.439073333333333, 479: 8.439073333333333, 480: 8.439073333333333, 481: 8.439073333333333, 482: 8.439073333333333, 483: 8.439073333333333, 484: 8.439073333333333, 485: 8.439073333333333, 486: 8.439073333333333, 487: 8.439073333333333, 488: 8.439073333333333, 489: 8.439073333333333, 490: 8.439073333333333, 491: 8.439073333333333, 492: 8.439073333333333, 493: 8.439073333333333, 494: 8.439073333333333, 495: 8.439073333333333, 496: 8.439073333333333, 497: 8.439073333333333, 498: 8.439073333333333, 499: 8.439073333333333, 500: 8.439073333333333, 501: 8.439073333333333, 502: 8.439073333333333, 503: 8.439073333333333, 504: 8.439073333333333, 505: 8.439073333333333, 506: 8.439073333333333, 507: 8.439073333333333, 508: 8.439073333333333, 509: 8.439073333333333, 510: 8.439073333333333, 511: 8.439073333333333, 512: 8.439073333333333, 513: 8.439073333333333, 514: 8.439073333333333, 515: 8.439073333333333, 516: 8.439073333333333, 517: 8.439073333333333, 518: 8.439073333333333, 519: 8.439073333333333, 520: 8.439073333333333, 521: 8.439073333333333, 522: 8.439073333333333, 523: 8.439073333333333, 524: 8.439073333333333, 525: 8.439073333333333, 526: 8.439073333333333, 527: 8.439073333333333, 528: 8.439073333333333, 529: 8.439073333333333, 530: 8.439073333333333, 531: 8.439073333333333, 532: 8.439073333333333, 533: 8.439073333333333, 534: 8.439073333333333, 535: 8.439073333333333, 536: 8.439073333333333, 537: 8.439073333333333, 538: 8.439073333333333, 539: 8.439073333333333, 540: 8.439073333333333, 541: 8.439073333333333, 542: 8.439073333333333, 543: 8.439073333333333, 544: 8.439073333333333, 545: 8.439073333333333, 546: 8.439073333333333, 547: 8.439073333333333, 548: 8.439073333333333, 549: 8.439073333333333, 550: 8.439073333333333, 551: 8.439073333333333, 552: 8.439073333333333, 553: 8.439073333333333, 554: 8.439073333333333, 555: 8.439073333333333, 556: 8.439073333333333, 557: 8.439073333333333, 558: 8.439073333333333, 559: 8.439073333333333, 560: 8.439073333333333, 561: 8.439073333333333, 562: 8.439073333333333, 563: 8.439073333333333, 564: 8.439073333333333, 565: 8.439073333333333, 566: 8.439073333333333, 567: 8.439073333333333, 568: 8.439073333333333, 569: 8.439073333333333, 570: 8.439073333333333, 571: 8.439073333333333, 572: 8.439073333333333, 573: 8.439073333333333, 574: 8.439073333333333, 575: 8.439073333333333, 576: 8.439073333333333, 577: 8.439073333333333, 578: 8.439073333333333, 579: 8.439073333333333, 580: 8.439073333333333, 581: 8.439073333333333, 582: 8.439073333333333, 583: 8.439073333333333, 584: 8.439073333333333, 585: 8.439073333333333, 586: 8.439073333333333, 587: 8.439073333333333, 588: 8.439073333333333, 589: 8.439073333333333, 590: 8.439073333333333, 591: 8.439073333333333, 592: 8.439073333333333, 593: 8.439073333333333, 594: 8.439073333333333, 595: 8.439073333333333, 596: 8.439073333333333, 597: 8.439073333333333, 598: 8.439073333333333, 599: 8.439073333333333, 600: 8.439073333333333, 601: 8.439073333333333, 602: 8.439073333333333, 603: 8.439073333333333, 604: 8.439073333333333, 605: 8.439073333333333, 606: 8.439073333333333, 607: 8.439073333333333, 608: 8.439073333333333, 609: 8.439073333333333, 610: 8.439073333333333, 611: 8.439073333333333, 612: 8.439073333333333, 613: 8.439073333333333, 614: 8.439073333333333, 615: 8.439073333333333, 616: 8.439073333333333, 617: 8.439073333333333, 618: 8.439073333333333, 619: 8.439073333333333, 620: 8.439073333333333, 621: 8.439073333333333, 622: 8.439073333333333, 623: 8.439073333333333, 624: 8.439073333333333, 625: 8.439073333333333, 626: 8.439073333333333, 627: 8.439073333333333, 628: 8.439073333333333, 629: 8.439073333333333, 630: 8.439073333333333, 631: 8.439073333333333, 632: 8.439073333333333, 633: 8.439073333333333, 634: 8.439073333333333, 635: 8.439073333333333, 636: 8.439073333333333, 637: 8.439073333333333, 638: 8.439073333333333, 639: 8.439073333333333, 640: 8.439073333333333, 641: 8.439073333333333, 642: 8.439073333333333, 643: 8.439073333333333, 644: 8.439073333333333, 645: 8.439073333333333, 646: 8.439073333333333, 647: 8.439073333333333, 648: 8.439073333333333, 649: 8.439073333333333, 650: 8.439073333333333, 651: 8.439073333333333, 652: 8.439073333333333, 653: 8.439073333333333, 654: 8.439073333333333, 655: 8.439073333333333, 656: 8.439073333333333, 657: 8.439073333333333, 658: 8.439073333333333, 659: 8.439073333333333, 660: 8.439073333333333, 661: 8.439073333333333, 662: 8.439073333333333, 663: 8.439073333333333, 664: 8.439073333333333, 665: 8.439073333333333, 666: 8.439073333333333, 667: 8.439073333333333, 668: 8.439073333333333, 669: 8.439073333333333, 670: 8.439073333333333, 671: 8.439073333333333, 672: 8.439073333333333, 673: 8.439073333333333, 674: 8.439073333333333, 675: 8.439073333333333, 676: 8.439073333333333, 677: 8.439073333333333, 678: 8.439073333333333, 679: 8.439073333333333, 680: 8.439073333333333, 681: 8.439073333333333, 682: 8.439073333333333, 683: 8.439073333333333, 684: 8.439073333333333, 685: 8.439073333333333, 686: 8.439073333333333, 687: 8.439073333333333, 688: 8.439073333333333, 689: 8.439073333333333, 690: 8.439073333333333, 691: 8.439073333333333, 692: 8.439073333333333, 693: 8.439073333333333, 694: 8.439073333333333, 695: 8.439073333333333, 696: 8.439073333333333, 697: 8.439073333333333, 698: 8.439073333333333, 699: 8.439073333333333, 700: 8.439073333333333, 701: 8.439073333333333, 702: 8.439073333333333, 703: 8.439073333333333, 704: 8.439073333333333, 705: 8.439073333333333, 706: 8.439073333333333, 707: 8.439073333333333, 708: 8.439073333333333, 709: 8.439073333333333, 710: 8.439073333333333, 711: 8.439073333333333, 712: 8.439073333333333, 713: 8.439073333333333, 714: 8.439073333333333, 715: 8.439073333333333, 716: 8.439073333333333, 717: 8.439073333333333, 718: 8.439073333333333, 719: 8.439073333333333, 720: 8.439073333333333, 721: 8.439073333333333, 722: 8.439073333333333, 723: 8.439073333333333, 724: 8.439073333333333, 725: 8.439073333333333, 726: 8.439073333333333, 727: 8.439073333333333, 728: 8.439073333333333, 729: 8.439073333333333, 730: 8.439073333333333, 731: 8.439073333333333, 732: 8.439073333333333, 733: 8.439073333333333, 734: 8.439073333333333, 735: 8.439073333333333, 736: 8.439073333333333, 737: 8.439073333333333, 738: 8.439073333333333, 739: 8.439073333333333, 740: 8.439073333333333, 741: 8.439073333333333, 742: 8.439073333333333, 743: 8.439073333333333, 744: 8.439073333333333, 745: 8.439073333333333, 746: 8.439073333333333, 747: 8.439073333333333, 748: 8.439073333333333, 749: 8.439073333333333, 750: 8.439073333333333, 751: 8.439073333333333, 752: 8.439073333333333, 753: 8.439073333333333, 754: 8.439073333333333, 755: 8.439073333333333, 756: 8.439073333333333, 757: 8.439073333333333, 758: 8.439073333333333, 759: 8.439073333333333, 760: 8.439073333333333, 761: 8.439073333333333, 762: 8.439073333333333, 763: 8.439073333333333, 764: 8.439073333333333, 765: 8.439073333333333, 766: 8.439073333333333, 767: 8.439073333333333, 768: 8.439073333333333, 769: 8.439073333333333, 770: 8.439073333333333, 771: 8.439073333333333, 772: 8.439073333333333, 773: 8.439073333333333, 774: 8.439073333333333, 775: 8.439073333333333, 776: 8.439073333333333, 777: 8.439073333333333, 778: 8.439073333333333, 779: 8.439073333333333, 780: 8.439073333333333, 781: 8.439073333333333, 782: 8.439073333333333, 783: 8.439073333333333, 784: 8.439073333333333, 785: 8.439073333333333, 786: 8.439073333333333, 787: 8.439073333333333, 788: 8.439073333333333, 789: 8.439073333333333, 790: 8.439073333333333, 791: 8.439073333333333, 792: 8.439073333333333, 793: 8.439073333333333, 794: 8.439073333333333, 795: 8.439073333333333, 796: 8.439073333333333, 797: 8.439073333333333, 798: 8.439073333333333, 799: 8.439073333333333, 800: 8.439073333333333, 801: 8.439073333333333, 802: 8.439073333333333, 803: 8.439073333333333, 804: 8.439073333333333, 805: 8.439073333333333, 806: 8.439073333333333, 807: 8.439073333333333, 808: 8.439073333333333, 809: 8.439073333333333, 810: 8.439073333333333, 811: 8.439073333333333, 812: 8.439073333333333, 813: 8.439073333333333, 814: 8.439073333333333, 815: 8.439073333333333, 816: 8.439073333333333, 817: 8.439073333333333, 818: 8.439073333333333, 819: 8.439073333333333, 820: 8.439073333333333, 821: 8.439073333333333, 822: 8.439073333333333, 823: 8.439073333333333, 824: 8.439073333333333, 825: 8.439073333333333, 826: 8.439073333333333, 827: 8.439073333333333, 828: 8.439073333333333, 829: 8.439073333333333, 830: 8.439073333333333, 831: 8.439073333333333, 832: 8.439073333333333, 833: 8.439073333333333, 834: 8.439073333333333, 835: 8.439073333333333, 836: 8.439073333333333, 837: 8.439073333333333, 838: 8.439073333333333, 839: 8.439073333333333, 840: 8.439073333333333, 841: 8.439073333333333, 842: 8.439073333333333, 843: 8.439073333333333, 844: 8.439073333333333, 845: 8.439073333333333, 846: 8.439073333333333, 847: 8.439073333333333, 848: 8.439073333333333, 849: 8.439073333333333, 850: 8.439073333333333, 851: 8.439073333333333, 852: 8.439073333333333, 853: 8.439073333333333, 854: 8.439073333333333, 855: 8.439073333333333, 856: 8.439073333333333, 857: 8.439073333333333, 858: 8.439073333333333, 859: 8.439073333333333, 860: 8.439073333333333, 861: 8.439073333333333, 862: 8.439073333333333, 863: 8.439073333333333, 864: 8.439073333333333, 865: 8.439073333333333, 866: 8.439073333333333, 867: 8.439073333333333, 868: 8.439073333333333, 869: 8.439073333333333, 870: 8.439073333333333, 871: 8.439073333333333, 872: 8.439073333333333, 873: 8.439073333333333, 874: 8.439073333333333, 875: 8.439073333333333, 876: 8.439073333333333, 877: 8.439073333333333, 878: 8.439073333333333, 879: 8.439073333333333, 880: 8.439073333333333, 881: 8.439073333333333, 882: 8.439073333333333, 883: 8.439073333333333, 884: 8.439073333333333, 885: 8.439073333333333, 886: 8.439073333333333, 887: 8.439073333333333, 888: 8.439073333333333, 889: 8.439073333333333, 890: 8.439073333333333, 891: 8.439073333333333, 892: 8.439073333333333, 893: 8.439073333333333, 894: 8.439073333333333, 895: 8.439073333333333, 896: 8.439073333333333, 897: 8.439073333333333, 898: 8.439073333333333, 899: 8.439073333333333, 900: 8.439073333333333, 901: 8.439073333333333, 902: 8.439073333333333, 903: 8.439073333333333, 904: 8.439073333333333, 905: 8.439073333333333, 906: 8.439073333333333, 907: 8.439073333333333, 908: 8.439073333333333, 909: 8.439073333333333, 910: 8.439073333333333, 911: 8.439073333333333, 912: 8.439073333333333, 913: 8.439073333333333, 914: 8.439073333333333, 915: 8.439073333333333, 916: 8.439073333333333, 917: 8.439073333333333, 918: 8.439073333333333, 919: 8.439073333333333, 920: 8.439073333333333, 921: 8.439073333333333, 922: 8.439073333333333, 923: 8.439073333333333, 924: 8.439073333333333, 925: 8.439073333333333, 926: 8.439073333333333, 927: 8.439073333333333, 928: 8.439073333333333, 929: 8.439073333333333, 930: 8.439073333333333, 931: 8.439073333333333, 932: 8.439073333333333, 933: 8.439073333333333, 934: 8.439073333333333, 935: 8.439073333333333, 936: 8.439073333333333, 937: 8.439073333333333, 938: 8.439073333333333, 939: 8.439073333333333, 940: 8.439073333333333, 941: 8.439073333333333, 942: 8.439073333333333, 943: 8.439073333333333, 944: 8.439073333333333, 945: 8.439073333333333, 946: 8.439073333333333, 947: 8.439073333333333, 948: 8.439073333333333, 949: 8.439073333333333, 950: 8.439073333333333, 951: 8.439073333333333, 952: 8.439073333333333, 953: 8.439073333333333, 954: 8.439073333333333, 955: 8.439073333333333, 956: 8.439073333333333, 957: 8.439073333333333, 958: 8.439073333333333, 959: 8.439073333333333, 960: 8.439073333333333, 961: 8.439073333333333, 962: 8.439073333333333, 963: 8.439073333333333, 964: 8.439073333333333, 965: 8.439073333333333, 966: 8.439073333333333, 967: 8.439073333333333, 968: 8.439073333333333, 969: 8.439073333333333, 970: 8.439073333333333, 971: 8.439073333333333, 972: 8.439073333333333, 973: 8.439073333333333, 974: 8.439073333333333, 975: 8.439073333333333, 976: 8.439073333333333, 977: 8.439073333333333, 978: 8.439073333333333, 979: 8.439073333333333, 980: 8.439073333333333, 981: 8.439073333333333, 982: 8.439073333333333, 983: 8.439073333333333, 984: 8.439073333333333, 985: 8.439073333333333, 986: 8.439073333333333, 987: 8.439073333333333, 988: 8.439073333333333, 989: 8.439073333333333, 990: 8.439073333333333, 991: 8.439073333333333, 992: 8.439073333333333, 993: 8.439073333333333, 994: 8.439073333333333, 995: 8.439073333333333, 996: 8.439073333333333, 997: 8.439073333333333, 998: 8.439073333333333, 999: 8.439073333333333
# }
#                               }
# schemes= ['GA, |Paths|=3', 'GA, |Paths|=6', 'GA, |Paths|=1', 'Hop-based shortest path, |Paths|=3', 'Hop-based shortest path, |Paths|=1', 'Hop-based shortest path, |Paths|=6']
# selected_epochs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]

# tickets_on_x_axis  =[0,2,3,4,5,6,7]
# x_axis_points = tickets_on_x_axis
# ploting_simple_y_as_x("Generations of GA","W-EGR (in thousands)",
#                           14, 14, 14,
#                           14, 2, 2,
#                           0,
#                           10.188540000000001,
#                           schemes,
#                           each_scheme_each_step_value,
#                           selected_epochs,selected_epochs,
#                           False,True,
#                           False,1,
#                           10,"plots/test.pdf",
#                           True,5,3.3)

# In[33]:


# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
 
    
def plot_stacked_bar_plot(x_axis_label,y_axis_label,x_axis_font_size, 
                          y_axis_font_size,x_axis_tick_font_size,y_axis_tick_font_size,
                          x_axis_pad, y_axis_pad,schemes,
                          stached_labels,each_scheme_stack_bar_values,each_scheme_stack_bar2_values,
                          x_axis_label_rotation_degree,legend_flag,legend_font_size,
                          legend_num_column,barWidth,plot_name,figure_width,figure_height,
                         each_org_weight,each_org_id):
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label,x_axis_font_size, 
                          y_axis_font_size,x_axis_tick_font_size,y_axis_tick_font_size,
                                         x_axis_pad, y_axis_pad,figure_width,figure_height)
    # y-axis in bold
    # rc('font', weight='bold')

    # Values of each group
    bars1 = [12, 28, 1]
    bars2 = [28, 7, 16]
    bars3 = [25, 3, 23]

    # Heights of bars1 + bars2
    bars = np.add(bars1, bars2).tolist()
#     print("bars",bars)
    # The position of the bars on the x-axis
#     r = [0,1,2]
    r = []
    for i in range(len(schemes)):
        r.append(i+1)
    r = [0,1,2,3]
    
    r2 = []
    for i in range(len(schemes)):
        r2.append(i+1)
    r2 = [0.3,1.3,2.3,3.3]
    # Names of group and bar width
#     schemes = ['A','B','C']
    my_class_labels = []
    
    colors = ["Red","Indianred","Green","Lime","Blue","cornflowerblue"]
    #bars = [[12, 28, 1],[28, 7, 16],[25, 3, 23]]
    zero_value_list = [0 for item in schemes]
    zero_value_list2 = [0 for item in schemes]
    each_stack_values = {}
#     print("each_scheme_stack_bar_values ",each_scheme_stack_bar_values)
    for stack_label in stached_labels: 
#         print("for stack ",stack_label)
        bar_values = []
        for scheme in schemes:
            stack_label_value = each_scheme_stack_bar_values[scheme][stack_label]
#             print("we have %s for scheme %s "%(stack_label_value,scheme))
            bar_values.append(stack_label_value)
        each_stack_values[stack_label] = bar_values
        
        
    each_stack2_values = {}
#     print("each_scheme_stack_bar_values ",each_scheme_stack_bar_values)
    for stack_label in stached_labels: 
#         print("for stack ",stack_label)
        bar_values2 = []
        for scheme in schemes:
            stack_label_value2 = each_scheme_stack_bar2_values[scheme][stack_label]
#             print("we have %s for scheme %s "%(stack_label_value,scheme))
            bar_values2.append(stack_label_value2)
        each_stack2_values[stack_label] = bar_values2
    color_index = 0
    for stack_label in stached_labels: 
        if stack_label not in my_class_labels:
            weight_of_org = each_org_weight[stack_label]
            k = each_org_id[stack_label]
            new_label = 'w_'+str(k)+"="+str(weight_of_org)+", True EGR"
#             my_class_labels.append(stack_label+", True EGR")
            my_class_labels.append(new_label)
            my_class_labels.append(str(stack_label)+", W-EGR")
        if color_index==0:
            print("we are adding for stack_label %s values %s and %s "%(stack_label,
                                                                        each_stack_values[stack_label],
                                                                       each_stack2_values[stack_label]))
            plt.bar(r, each_stack_values[stack_label],align='center',
                    color=colors[color_index], edgecolor='white', width=barWidth)
            bars = np.add(zero_value_list,each_stack_values[stack_label]).tolist()
            color_index+=1
            plt.bar(r2, each_stack2_values[stack_label],align='center', 
                    color=colors[color_index], edgecolor='white', width=barWidth)
            bars2 = np.add(zero_value_list2,each_stack2_values[stack_label]).tolist()
#             print("color is %s "%(colors[color_index]))
        else:
            print("2 we are adding for stack_label %s values %s and %s "%(stack_label,
                                                                          each_stack_values[stack_label],
                                                                         each_stack2_values[stack_label]))
            plt.bar(r, each_stack_values[stack_label],align='center',bottom=bars, color=colors[color_index], edgecolor='white', width=barWidth)
            bars = np.add(bars, each_stack_values[stack_label]).tolist()
            color_index+=1
#             print("2 color is %s "%(colors[color_index]))
            plt.bar(r2, each_stack2_values[stack_label],align='center',bottom=bars2,
                    color=colors[color_index], edgecolor='white', width=barWidth)
            bars2 = np.add(bars2, each_stack2_values[stack_label]).tolist()
        color_index+=1
    # Create brown bars
#     plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)
#     # Create green bars (middle), on top of the first ones
#     plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)
#     # Create green bars (top)
#     plt.bar(r, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)


    print("my_class_labels ",my_class_labels)
    if legend_flag:
        plt.legend([label for label in my_class_labels ],fontsize=legend_font_size, ncol=legend_num_column,handleheight=2.4, labelspacing=0.02)

    # Custom X axis
    plt.xticks(r, schemes,fontsize=x_axis_font_size,rotation=x_axis_label_rotation_degree)
    # plt.xlabel("group")
    plt.minorticks_on()
    plt.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(plot_name)
    plt.show()

# In[34]:


# unique_generation_ids = {0, 1, 2, 200, 20}
# unique_organizations = ['Organization 1', 'Organization 2', 'Organization 3']
# unique_schemes = ['GA', 'Greedy-Hop', 'Greedy-$\\frac{1}{EGR}$', 'Greedy-$\\frac{1}{EGR^2}$']
# each_scheme_each_organization_value= {'GA': {'Organization 1': 30.112435634935228, 'Organization 2': 28.138472725833953, 'Organization 3': 35.843656767710065}, 'Greedy-Hop': {'Organization 1': 25.945176622573843, 'Organization 2': 22.719768559535435, 'Organization 3': 29.528382149134185}, 'Greedy-$\\frac{1}{EGR}$': {'Organization 1': 25.990786911963397, 'Organization 2': 22.5544759190397, 'Organization 3': 27.62399838251156}, 'Greedy-$\\frac{1}{EGR^2}$': {'Organization 1': 2, 'Organization 2': 2, 'Organization 3': 2}}
# each_scheme_each_organization_value2= {'GA': {'Organization 1': 27.112435634935228, 'Organization 2': 25.138472725833953, 'Organization 3': 31.843656767710065}, 'Greedy-Hop': {'Organization 1': 21.945176622573843, 'Organization 2': 17.719768559535435, 'Organization 3': 21.528382149134185}, 'Greedy-$\\frac{1}{EGR}$': {'Organization 1': 21.990786911963397, 'Organization 2': 18.5544759190397, 'Organization 3': 21.62399838251156}, 'Greedy-$\\frac{1}{EGR^2}$': {'Organization 1': 1, 'Organization 2': 1, 'Organization 3': 1}}
# each_org_id = {'Organization 1':1, 'Organization 2':2, 'Organization 3':3}
# each_org_weight = {'Organization 1':1, 'Organization 2':1, 'Organization 3':1}
# plot_stacked_bar_plot("Schemes","True EGR (in thousands)",18,18,20,20,0, 0,
#                       unique_schemes,
#                       unique_organizations,each_scheme_each_organization_value,
#                       each_scheme_each_organization_value2,
#                       0,True,14,1,0.2,
#                       "plots/true_EGR_each_org_stacked_bar_plot_with_rate_cons.pdf",
#                       10,10,
#                      each_org_weight,each_org_id)

# In[ ]:




# In[ ]:




# In[ ]:


def plot_multiple_lines_different_x_axis_values(x_axis_label,y_axis_label,x_axis_label_font_size,
                                                y_axis_label_font_size,
                                                x_axis_pad,y_axis_pad,
                                                all_possible_x_axis_values,
                                                approach_compression_average_values,
                                                legend_font_size,plot_name,
                                                plot_width,plot_height):
    import numpy as np
#     from matplotlib.pylab import plt #load plot library
    import matplotlib.pyplot as plt
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label,
                                         x_axis_label_font_size,
                                         y_axis_label_font_size,
                                         x_axis_label_font_size,
                                         y_axis_label_font_size,
                                         x_axis_pad,y_axis_pad,
                                         plot_width,plot_height)
    
    # indicate the output of plotting function is printed to the notebook
#     %matplotlib inline 
    colors = ['BLACK', 'RED', 'MAROON','BLUE','OLIVE','LIME','AQUA','GREEN','TEAL','YELLOW']
#     try:
    style=["-","-.",":","-","--"]
    index = 0
    my_class_labels = []
    items_index = 0
    line_index = 0
#     print(len(x))
    my_class_labels = []
    for approach,compression_averages in approach_compression_average_values.items():
        if approach == 'overla_related':
            approach = 'overlap_related'
#             try:
        x_axis_values = compression_averages['compression_values']
        y_axis_values = compression_averages['average_values']
#                 print('**** these are x and y axis values ',approach,x_axis_values,y_axis_values)
#         if 'control' in approach and 'no' not in approach:
#             my_class_labels.append('Concurrency control')
#         else:
#             my_class_labels.append('No concurrency control')
        plt.plot(x_axis_values, y_axis_values)
        #ymin, ymax = ylim()  # return the current ylim
#                 ylim((0, 1))   # set the ylim to ymin, ymax
#                 ylim(0, 1)     # set the ylim to ymin, ymax
#                 #plt.xlim([0, max(x_values)])
#                 plt.ylim([0, 1])
        plt.xlim([0, max(all_possible_x_axis_values)])

        plt.plot(x_axis_values, y_axis_values,color=colors[index],
                 linestyle=style[line_index],marker=markers[index],
                 markevery=(0.0,0.1),linewidth=4.0, markersize=5,
                 markerfacecolor='blue',markeredgewidth='5', 
                 markeredgecolor='black', label=approach)
        if index == len(colors)-1:
            index = 0
        else:
            index = index +1

        if line_index ==len(style)-1:
            line_index = 0
        else:
            line_index = line_index +1
#             except ValueError:
#                 print("this is the valueerror",ValueError)
#     if len(my_class_labels)>1:
#         plt.legend([label for label in my_class_labels ],oc="upper left",fontsize=30)
#         plt.plot([1,2,3,4,5], [1,2,4,5,6])
#         plt.plot([1,5,7,9,11], [1,2,4,5,6])
#         plt.plot([1,3,5,6], [1,2,4,5])
    plt.ylim(ymin=0) 
    plt.legend(fontsize=legend_font_size)
    plt.savefig(plot_name)
    plt.show()
#     except ValueError:
#         print("this is the valueerror2",ValueError)

# In[ ]:



    
    


# In[ ]:


# each_scheme_stack_bar_values = {"scheme1":{"org1":1,"org2":3,"org3":1},
#                                "scheme2":{"org1":3,"org2":1,"org3":4}
                                
#                                }
# barWidth = 0.1
# plot_stacked_bar_plot("x_axis_label","y_axis_label",["scheme1","scheme2"],
#                       ["org1","org2","org3"],each_scheme_stack_bar_values,True,15,1,barWidth,"plot_name")

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:


def messages_in_human_redable(messages_in_last):
    messages_in_hr = []
    
    for num in messages_in_last:
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        hr_format =  '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
        messages_in_hr.append(hr_format)
    return messages_in_hr

# In[ ]:



    
def plot_bar_chart(x_axis_label,y_axis_label,cdf_info_dictionary_over_multi_item,rows_keys,schemes,plot_name):
#     cdf_info_dictionary_over_multi_item= {20:{'before_path_exploration':60,'path_exploration':40},
#                                          60:{'before_path_exploration':60,'path_exploration':40},
#                                          180:{'before_path_exploration':60,'path_exploration':40},
#                                          540:{'before_path_exploration':60,'path_exploration':40},
#                                          1620:{'before_path_exploration':60,'path_exploration':40}}
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    x_vector = []
    header = []
    each_row_values = {}
    for scheme in schemes:
        for row in rows_keys:
            percentage = cdf_info_dictionary_over_multi_item[scheme][row]
            if scheme not in x_vector:
                x_vector.append(scheme)
            if row not in header:
                header.append(row)
            try:
                each_row_values[row].append(percentage)
            except:
                each_row_values[row]=[percentage]
                
    dataset= [x_vector,each_row_values[rows_keys[0]],each_row_values[rows_keys[1]]]
    print("data set is ",dataset)
    print("dataset[1] ",dataset[1])
    print("dataset[2]" ,dataset[2])
    dataset = [['1k','5k'],[6, 1,4],[5, 4,1]]
#     dataset[0] =['1k','5k']
#     dataset[1] = [6, 1,4]
#     dataset[2] = [5, 4,1]
    dataset = np.array(dataset, dtype=object)
    X_AXIS = dataset[0]
    global global_font_size
    fig = matplotlib.pyplot.gcf()
    configs = dataset[0]
    N = len(configs)
    ind = np.arange(N)
    width = 0.2
    width = 0.2
    bar_width = 0.2

    plt.xticks(rotation=90)
    
    p1 = plt.bar(ind, dataset[1], width, color='blue')
    p2 = plt.bar(ind, dataset[2], width, bottom=dataset[1], color='red')
    plt.xticks(ind, X_AXIS, fontsize=global_font_size)
#     plt.xticks(rotation=90)
    plt.legend((p1[0], p2[0]), (header[0], header[1]), fontsize=global_font_size, ncol=4, framealpha=0, fancybox=True)
    plt.savefig(plot_name, format='pdf', dpi=1200)
    plt.show()
    

        
    
    
    

# In[ ]:


# # table_sizes_dictionary={}
# table_sizes_dictionary = {'1k':{'org1':6,'org2':2,"org3":10},
#                           '5k':{'org1':1,'org2':3,"org3":5},
                          
#                          }
# cross_all_topologies_table_sizes = ['1k','5k']
# print ('cross_all_topologies_table_sizes',cross_all_topologies_table_sizes)
# plot_bar_chart('x_axis','Time(sec)',table_sizes_dictionary,['org1','org2',"org3"],
#                cross_all_topologies_table_sizes,
#                'plots/orgs_bar_plot_test.pdf')



# In[ ]:





# In[ ]:


def plot_bar_plot(x_axis_label,y_axis_label,each_scheme_each_x_axis_label_values,x_axis_values,x_axis_labels,x_axis_label_rotation_degree,plot_file_name):

    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    
#     import matplotlib
#     import matplotlib.pyplot as plt
    #import numpy as np

    o = ''
    #labels = ['1', '2', '3', '4', '5']
    #print 'invalid_routes_percentage_based_on_rho_compression.keys()[0]',invalid_routes_percentage_based_on_rho_compression.keys()[0]
    #print 'invalid_routes_percentage_based_on_rho_compression[invalid_routes_percentage_based_on_rho_compression.keys()[0]]',invalid_routes_percentage_based_on_rho_compression[invalid_routes_percentage_based_on_rho_compression.keys()[0]]
    
    compression_times = len(each_scheme_each_x_axis_label_values[list(each_scheme_each_x_axis_label_values.keys())[0]])
    labels = []
    for item in range(1,(compression_times)+1):
        labels.append('e'+str(item))
    labels = x_axis_labels
    
    legends = []
    

    ind = np.arange(len(labels))
    x = np.arange(len(labels))  # the label locations
    width = 0.15  # the width of the bars
    #print 'x - width/3',x - width/3
    #print 'x + width/3',x + width/3
#     fig, ax = plt.subplots()
    margin_value = 0
    print("************ ",ind)
    width = 0.2  # the width of the bars
    colors = ['GREEN','BLACK', 'RED','BLUE','LIME','YELLOW', 'MAROON','OLIVE','AQUA','TEAL']
    color_index = 0
    for scheme, values in each_scheme_each_x_axis_label_values.items():
        #print('values are ', ind+margin_value,',', invalid_percentage_based_on_overlap ,',', width,',',  o+':'+str(overlap))
#         print('values are ',len(invalid_percentage_based_on_overlap),invalid_percentage_based_on_overlap)
        values_for_this_scheme = []
        for x_axis_label in x_axis_values:
            values_for_this_scheme.append(each_scheme_each_x_axis_label_values[scheme][x_axis_label])
        rects1= plt.bar(ind+margin_value-0.2, values_for_this_scheme ,width,  label=scheme,color = colors[color_index])
#         print('******** these are the values *****:',ind+margin_value, values_for_this_scheme ,width,  o+':'+str(overlap), colors[color_index])
        margin_value = margin_value+0.2
        legends.append(scheme)
        color_index = color_index +1

    
    plt.tight_layout()
    new_ticks = [ str(y) for y in labels]
    plt.xticks(x, new_ticks,rotation = x_axis_label_rotation_degree,fontsize=31)
    plt.legend([label for label in legends ], loc='upper left',fontsize=30)
#     s.plot( 
#         kind='bar', 
#         color=my_colors,
#     )
    plt.savefig(plot_file_name)
    plt.show()

# In[ ]:


# each_scheme_each_x_axis_label_values = {"Genetic":{0:10,1:14,2:15},"Huristic":{0:5,1:10,2:11}}
# plot_bar_plot("x_axis_label","y_axis_label",each_scheme_each_x_axis_label_values,
#               [0,1,2],[0,1,2],
#               0,
#               "plots/test_bar_plot")


# In[ ]:




# In[ ]:


def plotting_two_y_axis(x_axis_label,y_axis_label1,y_axis_label2,
                        x_axis_values_for_y1,
                        x_axis_values_for_y2,y_axis_values1,y_axis_values2,x_axis_label_fot_size,y_axis_values_font_size,
                       legend_font_size,plot_name):
    # create figure and axis objects with subplots()
    fig,ax = plt.subplots()
    # make a plot
    ax.plot(x_axis_values_for_y1,
            y_axis_values1,
            color="red", 
            marker="o")
    # set x-axis label
    ax.set_xlabel(x_axis_label, fontsize = x_axis_label_fot_size)
    # set y-axis label
    ax.set_ylabel(y_axis_label1,
                  color="red",
                  fontsize=y_axis_values_font_size)
    
    
    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(x_axis_values_for_y2, y_axis_values2,color="blue",marker="o")
    ax2.set_ylabel(y_axis_label2,color="blue",fontsize=y_axis_values_font_size)
    
#     plt.ylim(0, y_axis_provided_max_value)
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(plot_name,bbox_inches='tight')
    plt.show()
    
#     plt.show()
#     # save the plot as a file
#     fig.savefig(plot_name,
#                 format='jpeg',
#                 dpi=100,
#                 bbox_inches='tight')
# plotting_two_y_axis("x_axis_label","y_axis_label1","y_axis_label2",
#                         [0,1,2,3,4,5,6],
#                         [0,1,2,3,4,5,6],
#                     [4,6,8,10,12,14,16],[0.1,0.2,0.5,0.1,0.9,0.1,0.3],15,15,
#                        15,"plots/two_y_axis_plot.pdf")

# In[ ]:




# In[ ]:


# each_scheme_x_axis_y_axis_values1 = {"org1":{"x_axis_values":[0,1,2,3],"y_axis_values":[4,6,8,10]},
#                                     "org2":{"x_axis_values":[0,1,2,3],"y_axis_values":[8,1,6,4]},
#                                     "org3":{"x_axis_values":[0,1,2,3],"y_axis_values":[8,6,4,2]}}

# each_scheme_x_axis_y_axis_values2 = {"org1":{"x_axis_values":[0,1,2,3],"y_axis_values":[.4,.6,.8,.10]},
#                                     "org2":{"x_axis_values":[0,1,2,3],"y_axis_values":[.8,.1,.6,.4]},
#                                     "org3":{"x_axis_values":[0,1,2,3],"y_axis_values":[.8,.6,.4,.2]}}
# each_scheme_x_axis_y_axis_values1 = {"org1":{"x_axis_values":[0,1,2,3],"y_axis_values":[4,6,8,10]},
#                                     }

# each_scheme_x_axis_y_axis_values2 = {"org1":{"x_axis_values":[0,1,2,3],"y_axis_values":[.4,.6,.8,.10]},
#                                   }
# plotting_multi_scheme_two_y_axis("x_axis_label","y_axis_label1","y_axis_label2",
#                         each_scheme_x_axis_y_axis_values1,each_scheme_x_axis_y_axis_values2,15,15,True,
#                        15,3,"plots/multi_scheme_tw0_y_axis.pdf")

# In[ ]:




# In[ ]:





def plot_3D_surface(x_axis_label,y_axis_label,z_axis_label,x_axis_values,y_axis_values,z_axis_values,x_axis_font_size,y_axis_font,
                z_axis_font,x_axis_labelpad,y_axis_labelpad,z_axis_labelpad,plot_name):
    
    
    
    print("we are going to plot 3D")
    fig = plt.figure(num=1, clear=True)
    fig = plt.figure()
    font_size = 33
    plt.figure(figsize=(8,8))
    global_mark_every = 1
    #matplotlib.rcParams['text.usetex'] = True
    fig.set_size_inches(16, 8, forward=True)
    
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    processing_propagation_pairs = [[1,1],[1,1]]
    x = np.array([[1, 3], [2, 4]])
    x = np.array(x_axis_values)
    y = np.array(y_axis_values)
    z = np.array(z_axis_values)
    print("X %s Y %s Z %s "%(x,y,z))
    ax.plot_surface(x, y, z)
    #ax.set(xlabel='x', ylabel='y', zlabel='z')
    ax.set_xlabel(x_axis_label,fontsize=x_axis_font_size,labelpad=x_axis_labelpad)
    ax.set_ylabel(y_axis_label,fontsize=y_axis_font,labelpad=y_axis_labelpad)
    ax.set_zlabel(z_axis_label,fontsize=z_axis_font,labelpad=z_axis_labelpad)
    fig.tight_layout()
    fig.savefig(plot_name)
    plt.show()
# plot_CD_surface()

# In[ ]:



    
def min_max_mean_median_plot(x_axis_label,y_axis_label,x_values,convergence_times,log_or_not,plot_name):

    try:
        compresson_factors = []
        average_Convergence_times = []
        plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
        labels = []
        labels.append(' ')
        list_of_list = []
        color_index = 0
        colors = ['black','red','blue','green']
        index = 0
        import numpy as np
        x = np.arange(len(x_values))+1
        for each_rho_value in x_values:
            
            
            convergences = convergence_times[each_rho_value]
            my_list_of_convergences = []
            for item in convergences:
                my_list_of_convergences.append(float(item))
            #print my_list_of_convergences
            #print sum(my_list_of_convergences)
            #print sum(my_list_of_convergences) / len(my_list_of_convergences)
            
            average_Convergence_times.append(sum(my_list_of_convergences)/len(my_list_of_convergences))
            compresson_factors.append(each_rho_value)
            labels.append(str(each_rho_value))
            costs = []
            import math
            from math import log
            for item in convergences:
                if log_or_not == 'log':
                    costs.append(log(item)/log(2))
                else:
                    costs.append(float(item))
            #print 'this should  not have negative values' ,  costs
            costs = tuple(costs)
            list_of_list.append(costs)
        #plt.xlabel('concurrency rate', fontsize=26)
        #plt.ylabel('Convergence time(s)',fontsize=26)
        #print list_of_list
        
        import numpy as np
        positions = np.arange(len(list_of_list)) + 1
        plt.boxplot([item for item in list_of_list], positions=positions,showmeans=True)
        
        #plt.plot(compresson_factors, average_Convergence_times,color=colors[color_index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20)
        plt.plot(x, average_Convergence_times,color="black",marker=markers[0],linewidth=4.0,markersize=20)
         
        index = index +1
        
        color_index = color_index +1
        xy = np.arange(len(labels))
        new_ticks = [ str(x) for x in labels]
        plt.xticks(xy, new_ticks,fontsize=34)
        axes = plt.gca()
        
#         axes.set_ylim([0,1])

        plt.savefig(plot_name)
    except ValueError:
        print (ValueError)

def scatter_plot_with_correlation_line(plt,x, y, graph_filepath,human_readable_format):

    # Scatter plot
    plt.scatter(x, y)
    
    # Add correlation line
    axes = plt.gca()
    m, b = np.polyfit(x, y, 1)
    X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
    plt.plot(X_plot, m*X_plot + b, '-',color = 'black')
    if human_readable_format:
        new_ticks = messages_in_human_redable(x)
        plt.xticks(x, new_ticks,fontsize=28)
    # Save figure
    plt.xticks(rotation=90)
    plt.savefig(graph_filepath, dpi=300, format='pdf', bbox_inches='tight')

def scatter(x_axis_title,y_axis_title,y_axis_values,x_axis_values,saved_file_name,human_readable_format):
    from scipy.stats import linregress

    xtitle = x_axis_title
    
    ytitle = y_axis_title
    
    plt = set_plotting_global_attributes(xtitle,ytitle)
#     print len(convergences_in_last_detection_case),len(messages_in_last_detection_case)
#     
    g1 = (x_axis_values, numpy.array(y_axis_values))
    data = (g1)

    colors = ("black", "green",'red')
    # Create plot
    ax = fig.add_subplot(1, 1,1)
    svalue = 700
    [i.set_linewidth(3.1) for i in ax.spines.itervalues()]
    ax.scatter(x_axis_values,numpy.array(y_axis_values) , c='black',s=svalue,linewidth=2.0, marker = "+")
    new_ticks = []
    x = np.arange(len(x_axis_values))
    
    #plt.savefig(saved_file_name)
    
    scatter_plot_with_correlation_line(plt,x_axis_values,y_axis_values, saved_file_name,human_readable_format)
    
    
def scatter_with_multiple_colors(x_axis_y_axis_values_over_lines,x_axis_values_key,y_axis_values_key,x_axis_label,y_axis_label,log_scale,plot_file_name):
    data = []
    groups = []
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    
    
    for key,edit_distance_cost_info in x_axis_y_axis_values_over_lines.items():
        x_axis_values = x_axis_y_axis_values_over_lines[key][x_axis_values_key]
        y_axis_values = x_axis_y_axis_values_over_lines[key][y_axis_values_key]
        g1 = (x_axis_values, numpy.array(y_axis_values))
        data.append(g1)
        groups.append(key)
    #g2 = (old_amended_typos_distance, numpy.array(old_amended_typos_cost))
    #g3 = (new_typos_distance, numpy.array(new_typos_cost))
    
    #data = (g1, g2,g3)
    colors = ("black", "green",'red','blue')
    #groups = ("pre-2000 gTLDs",'2000-2012 gTLDs' ,"post-2012 gTLDs") 

    # Create plot
    import random
    ax = fig.add_subplot(1, 1,1)
    #ax.set_yscale("log")
    svalue = 700
    from math import exp, expm1
    import math
    for data, color, group in zip(data, colors, groups):
        x, y = data
        #print type(x),type(y)
        #print y
        #svalue = random.randint(400,701)
        #print 'svalue',svalue
        y_tmp = []
        for item in y:
            from math import exp, expm1
            import math
            from math import log
            if log_scale:
                y_tmp.append(log(item)/log(10))
            else:
                y_tmp.append((item))
        ax.scatter(x, y_tmp, c=color,s=svalue,alpha=0.5 ,label=group)
        #print 'the values for x and y are ',x, y_tmp
        #ax.set_yscale('log')
        
        svalue = svalue -300
#     from matplotlib import rcParams
    
#     plt.grid(True)
#     rcParams.update({'figure.autolayout': True})    
#     rcParams.update({'figure.autolayout': True})
#     #label_size = 29
#     plt.rcParams['xtick.labelsize'] = label_size 
#     plt.rcParams['ytick.labelsize']=label_size
    #plt.xlabel('Edit Distance', fontsize=33,labelpad=30)
    #plt.ylabel('Price of typo candidates(log scale, base: 10)',fontsize=33,labelpad=30)
    if len(x_axis_y_axis_values_over_lines) >1:
        plt.legend(loc=5,fontsize=28)
    plt.xticks(rotation=0)
#     plt.tight_layout()
    #plt.title('scatter plot of typo registration cost based on edit distance',fontsize=25)
    plt.savefig(plot_file_name)
    
    plt.show()
    




# In[ ]:




# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
def set_3D_plotting_global_attributes(x_axis_label,y_axis_label,z_axis_label):
    import matplotlib.pyplot as plt
    global global_font_size
    global figure_width
    global figure_highth
    global space_from_x_y_axis
    global style
    global markers
    global csfont
    global descriptions
    font_size = 44
    plt.figure(figsize=(8,8))
    global fig
    global global_mark_every
    global_mark_every = 1
    #matplotlib.rcParams['text.usetex'] = True
    fig = plt.figure()
    fig.set_size_inches(16, 8, forward=True)
    global style
    #matplotlib.rcParams['text.usetex'] = True
    global markers
    
    global descriptions

    label_size = 40
    #matplotlib.rcParams['text.usetex'] = True
    csfont = {'fontname':'Times New Roman'}
    #write your code related to basemap here
    #plt.title('title',**csfont)
    plt.rcParams['xtick.labelsize'] = label_size 
    #matplotlib.rcParams['text.usetex'] = True
    plt.rcParams['ytick.labelsize']= label_size
    #matplotlib.rcParams['text.usetex'] = True
    plt.xlabel(x_axis_label, fontsize=36,labelpad=20)
    #matplotlib.rcParams['text.usetex'] = True
    plt.ylabel(y_axis_label,fontsize=36,labelpad=20)
    plt.zlabel('Convergence delay',fontsize=36,labelpad=20)
    plt.grid(True)
    plt.tight_layout()
    #matplotlib.rcParams['text.usetex'] = True
    #plt.ylim(ymin=0) 
    return plt

def plot_multi_dimention_results(plot_name):
    #plt = set_3D_plotting_global_attributes('Propagation delay','Processing delay','Convergence delay')
    # propagation_delay = list(np.linspace(-4, 4, 100))
    # processing_delay = list(np.linspace(-4, 4, 100))
    #X, Y, Z = [1,2,3,4,5,6,7,8,9,10],[5,6,2,3,13,4,1,2,4,8],[2,3,3,3,5,7,9,11,9,10]
    X, Y = [1,2,4,10,40,80,160,320],[0.016,0.1,0.5,1,2,4,8]#milliseconds
    propagation_delay, processing_delay = np.meshgrid(X, Y)
    # print(X,Y)
    convergence_delay = np.array((propagation_delay* processing_delay))
    # X, Y, Z = [1,2,3,4,5,6,7,8,9,10],[5,6,2,3,13,4,1,2,4,8],[2,3,3,3,5,7,9,11,9,10]
    # Z = (np.sin((X**2 + Y**2)/4)).tolist() 
    print('propagation_delay, processing_delay,convergence_delay',propagation_delay, processing_delay,convergence_delay)
    convergence_delay_values= []
    for pro in X:
        for processing in Y:
            #print('pro*processing',pro,processing)
            if pro <=4 and processing <=0.1:
                CD = 2000
                convergence_delay_values.append(2000)
            else:
                convergence_delay_values.append(2000 + 10* (pro+processing))
                CD = 2000 + 10* (pro+processing)
            #print('propagation,processing, CD',pro,processing,CD)
    a = np.array(convergence_delay_values)
    print(type(convergence_delay),type(a))
    #print(convergence_delay)
    #print(a)
    fig = plt.figure()
    font_size = 33
    plt.figure(figsize=(8,8))
    global_mark_every = 1
    #matplotlib.rcParams['text.usetex'] = True
    fig.set_size_inches(16, 8, forward=True)
    ax = Axes3D(fig)
    #ax = plt.axes(projection='3d')
#     x = np.arange(len(X))
#     new_ticks = [ str(y) for y in X]
#     plt.xticks(x, new_ticks,fontsize=20)
#     plt.grid(True)
    plt.tight_layout()
#     ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)
    ax.plot_surface(propagation_delay, processing_delay, convergence_delay, rstride=1, cstride=1, cmap=cm.viridis)
#     ax.plot_wireframe(propagation_delay, processing_delay, convergence_delay,color = 'blue')
    
#     ax.contour3D(propagation_delay, processing_delay, convergence_delay, 50, cmap='binary')
    ax.set_xlabel('Propagation delay',fontsize=32,labelpad=31)
    ax.set_ylabel('Processing delay',fontsize=32,labelpad=31)
    ax.set_zlabel('Convergence delay',fontsize=32,labelpad=22)
    #ax.view_init(60, 35)
    plt.savefig(plot_name)
    plt.show()

# In[ ]:




# In[ ]:




# In[ ]:


   
def plot_multiple_line_plot(data_dictionary,x_axis_label,y_axis_label,x_axis_values,y_axis_values,plot_name,value_attached_to_line_name):
    
    colors = ['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL']
    style=["-","--","-.",":","-"]
    color_index = 0
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    
    my_dic = {}
    my_class_labels = []
    x = np.arange(len(x_axis_values))
    sizes = []
    index = 0
    
    for y_axis_value in y_axis_values:
        
        values = []
        for x_axis_value in x_axis_values:
            
            try:
                values.append(data_dictionary[y_axis_value][x_axis_value])
            except:
                pass
        
        if value_attached_to_line_name:
            sizes.append(str(value_attached_to_line_name)+' '+str(y_axis_value))
        else:
            sizes.append(str(y_axis_value))
        #print x_axis_values,values
        plt.plot(x_axis_values, values,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20)
        index = index +1
        color_index = color_index +1
    my_class_labels = sizes
    #plt.xlabel('MRAI (sec)', fontsize=34,labelpad=34)
    #plt.ylabel('Convergence Time (sec)',fontsize=34,labelpad=34)
    plt.grid(True)
#     plt.tight_layout()
    #plt.ylim(ymin=0) 
    plt.xlim(xmin=0) 
    new_ticks = [ str(y) for y in x_axis_values]
    #plt.xticks(x, new_ticks,fontsize=34)
    #matplotlib.rcParams.update({'font.size': 34})
    plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=30)
    plt.savefig(plot_name)
    plt.show()

def plot_multiple_line_plot_log_scale_on_x_axis(data_dictionary,x_axis_label,y_axis_label,x_axis_values,y_axis_values,plot_name,value_attached_to_line_name):
    
    colors = ['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL']
    style=["-","--","-.",":","-"]
    color_index = 0
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    
    my_dic = {}
    my_class_labels = []
    x = np.arange(len(x_axis_values))
    sizes = []
    index = 0
    
    for y_axis_value in y_axis_values:
        
        values = []
        for x_axis_value in x_axis_values:
            
            try:
                values.append(data_dictionary[y_axis_value][x_axis_value])
            except:
                pass
        
        if value_attached_to_line_name:
            sizes.append(str(value_attached_to_line_name)+' '+str(y_axis_value))
        else:
            sizes.append(str(y_axis_value))
        #print x_axis_values,values
        plt.plot(x_axis_values, values,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20)
        index = index +1
        color_index = color_index +1
    my_class_labels = sizes
    #plt.xlabel('MRAI (sec)', fontsize=34,labelpad=34)
    #plt.ylabel('Convergence Time (sec)',fontsize=34,labelpad=34)
    plt.grid(True)
#     plt.tight_layout()
    #plt.ylim(ymin=0) 
    plt.xlim(xmin=0) 
    new_ticks = [ str(y) for y in x_axis_values]
    plt.xticks(x, new_ticks,fontsize=34)
    matplotlib.rcParams.update({'font.size': 34})
    plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=30)
    plt.savefig(plot_name)
    plt.show()
    

    
def plot_convergence(Convergene_time_dictionary,MRAI_VALUES4,topology_size4,x_axis_label,y_axis_label,real_expectation,convergence_messages,label,type_of_convergence,plot_name):
    #print 'Convergene_time_dictionary is',Convergene_time_dictionary
    #print 'MRAI_VALUES4,topology_size4',MRAI_VALUES4,topology_size4
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    colors = ['BLACK', 'RED', 'BLUE','GREEN','MAROON','AQUA','OLIVE','LIME','TEAL']
    style=[ 'solid', 'dashed', 'dashdot', 'dotted',"-","--","-.",":",'dashed','solid', 'dashed', 'dashdot']
    color_index = 0
#     my_dic = {}
    my_dic = {}
    my_class_labels = []
    x = np.arange(len(MRAI_VALUES4))
    sizes = []
    index = 0
    #print 'Convergene_time_dictionary',Convergene_time_dictionary
    for topology_size in topology_size4:
        topology_size = str(topology_size)
        Convergence_times = []
        for mrai in MRAI_VALUES4:
            mrai = str(mrai)
            try:
                #print 'Convergene_time_dictionary[(topology_size)][mrai]',Convergene_time_dictionary[(topology_size)][mrai]
                
                Convergence_times.append(Convergene_time_dictionary[(topology_size)][int(mrai)])
            except:
                #print ValueError
                pass
        #print 'Convergence_times',Convergence_times
        sizes.append('propagation delay='+str(topology_size))
        plt.plot(x, Convergence_times,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20,markerfacecolor='blue',markeredgewidth='5', markeredgecolor='black')
        #plt.plot(x_axis_values, values,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20)

        index = index +1
        color_index = color_index +1
    my_class_labels = sizes
    #matplotlib.rcParams['text.usetex'] = True
    #plt.xlabel('MRAI (sec)', fontsize=34,labelpad=34)
    #plt.ylabel('Convergence Time (sec)',fontsize=34,labelpad=34)
    plt.grid(True)
    #matplotlib.rcParams['text.usetex'] = True
#     plt.tight_layout()
    plt.xlim([0, max(x)+0.1])
    #matplotlib.rcParams['text.usetex'] = True
    new_ticks = [ str(y) for y in MRAI_VALUES4]
    plt.xticks(x, new_ticks,fontsize=34)
    #matplotlib.rcParams.update({'font.size': 34})
    if len(my_class_labels)>1:
        plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=30)
    plt.savefig(plot_name)
    #matplotlib.rcParams['text.usetex'] = True  
    plt.show()
def plot_convergence_detection_alg_overhead(x_axix_label,y_axix_label,dictionary_keys_in_order,Read_and_Detection_time_with_convergence_Det_Alg,topologies,x_axis_new_tickets,log_scale,plot_name):
    
 
    colors = ['BLACK', 'RED', 'BLUE','GREEN','MAROON','AQUA','OLIVE','LIME','TEAL']
    style=[ 'solid', 'dashed', 'dashdot', 'dotted',"-","--","-.",":",'dashed']
    plt = set_plotting_global_attributes(x_axix_label,y_axix_label)
    #print Read_and_Detection_time_with_convergence_Det_Alg
    my_dic = {}


    my_class_labels = []

    
    x = np.arange(len(topologies))
    print('we have % as our x '%(x))
    sizes = []
    #plt.gca().set_color_cycle(['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL'])


    #print 'Convergene_time_dictionary',Convergene_time_dictionary
    index = 0
    color_index =0
    for real_detection_algorithm in dictionary_keys_in_order:
        label_of_result = str(real_detection_algorithm)
        Convergence_times = []
        import math
        from math import log
        
        for topology in topologies:
            topology = str(topology)
#             if log_scale:
                
#                 value = log(Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)])/log(2)
                
#                 print Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)],value
#             else:
            print(label_of_result,int(topology))
            value  = Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)]
            try:
                Convergence_times.append(value)
                
            except:
                pass
        sizes.append(str(label_of_result))
        print("these are the x and y axis values",Convergence_times,label_of_result)
        plot(x, Convergence_times,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=6.0, markersize=10,markerfacecolor='black',markeredgewidth='5', markeredgecolor='blue')
        index +=1
        color_index +=1
        if color_index >=len(colors):
            color_index = 1
        if index >= len(style):
            index = 2
        
        
        
    new_x_labels = []
    for item in topologies:
        if int(item) ==50:
            new_x_labels.append(inf)
        else:
            new_x_labels.append(item)

    plt.xticks(x,new_x_labels)

    
    my_class_labels = sizes

    plt.grid(True)
    plt.ylim(ymin=0)
    plt.ylim(ymin=0)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.tight_layout()
    new_ticks = [ str(y) for y in topologies]
    plt.xticks(x, x_axis_new_tickets,fontsize=28)
    plt.grid(True)
    plt.tight_layout()
    if log_scale:
        plt.yscale('log')
#     plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=28)
    #plt.legend([label for label in my_class_labels ],fontsize=23)
    plt.legend([label for label in my_class_labels ],fontsize=25, ncol=1,handleheight=2.4, labelspacing=0.05)
    
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    plt.savefig(plot_name)
    plt.show()
    

def ploting_simple_y_as_x_with_vertical_lines(x_axix_label,y_axix_label,dictionary_keys_in_order,Read_and_Detection_time_with_convergence_Det_Alg,topologies,tickets_on_x_axis,log_scale,plot_name):
    
 
    colors = ['BLACK', 'RED', 'BLUE','GREEN','MAROON','AQUA','OLIVE','LIME','TEAL']
    style=[ 'solid', 'dashed', 'dashdot', 'dotted',":",'solid', 'dashed', 'dashdot']
    plt = set_plotting_global_attributes(x_axix_label,y_axix_label)
    #print Read_and_Detection_time_with_convergence_Det_Alg
    my_dic = {}


    my_class_labels = []

    
#     x = np.arange(len(topologies))
    x = np.arange(max(topologies))
    x = []
    for point_x_axis in topologies:
        x.append(int(point_x_axis))
    x.sort()
    print('we have %s as our x '%(x))
    sizes = []
    #plt.gca().set_color_cycle(['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL'])

    #print 'Convergene_time_dictionary',Convergene_time_dictionary
    index = 0
    color_index =0
    for real_detection_algorithm in dictionary_keys_in_order:
        label_of_result = str(real_detection_algorithm)
        Convergence_times = []
        import math
        from math import log
        
        for topology in topologies:
            topology = str(topology)
#             if log_scale:
                
#                 value = log(Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)])/log(2)
                
#                 print Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)],value
#             else:
            print('scheme %s x_axis value %s, result for this point %s '%(real_detection_algorithm,label_of_result,int(topology)))
            value  = Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)]
            try:
                Convergence_times.append(value)
                
            except:
                pass
        sizes.append(str(label_of_result))
        print("these are the x and y axis values",Convergence_times,label_of_result)
        plot(x, Convergence_times,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=6.0, markersize=10,markerfacecolor='black',markeredgewidth='5', markeredgecolor='blue')
        
        index = index +1
        color_index+=1
        if color_index >=len(colors):
            color_index = 1
        if index >= len(style):
            index = 2
            
#         if color_index >= len(colors):
#             index = 0
        
        
    
    # x coordinates for the lines
    xcoords = [10, 30]
    # colors for the lines
    colors = ['k','r']

    for xc,c in zip(xcoords,colors):
        plt.axvline(x=xc, label='k = {}'.format(xc), c=c)
    my_class_labels = sizes

    plt.grid(True)
    plt.ylim(ymin=0)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.tight_layout()
#     new_ticks = [ str(y) for y in topologies]
#     plt.xticks(x, new_ticks,fontsize=32)
    plt.grid(True)
#     fig, ax = plt.subplots()
#     plt.grid(which='major', linestyle='-', linewidth='0.2', color='red')

    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='black')

    plt.tight_layout()
    if log_scale:
        plt.yscale('log')
#     plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=28)
#     plt.legend([label for label in my_class_labels ],fontsize=23)
    plt.legend([label for label in my_class_labels ],fontsize=25, ncol=2,handleheight=2.4, labelspacing=0.05)
    
#     plt.xticks(range(0, len(tickets_on_x_axis) * 2, 2), tickets_on_x_axis)
#     plt.xlim(-2, len(tickets_on_x_axis)*2)
    #plt.ylim(0, 1)
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    
    
    plt.savefig(plot_name)
    plt.show()    


    
    
def ploting_simple_lines_printed_version(x_axix_label,y_axix_label,dictionary_keys_in_order,Read_and_Detection_time_with_convergence_Det_Alg,topologies,log_scale,plot_name):
    
 
    colors = ['BLACK', 'BLACK','RED', 'BLUE','GREEN','MAROON','AQUA','OLIVE','LIME','TEAL','PURPLE','PINK','CYAN']
    style=[ 'solid','dotted','dashed',"dashdot","-.", 'dashed' ,'solid', 'dashed', 'dashdot']
    
    plt = set_plotting_global_attributes(x_axix_label,y_axix_label)
    #print Read_and_Detection_time_with_convergence_Det_Alg
    my_dic = {}


    my_class_labels = []

    
#     x = np.arange(len(topologies))
    x = np.arange(max(topologies))
    x = []
    for point_x_axis in topologies:
        x.append(int(point_x_axis))
    x.sort()
    print('we have %s as our x '%(x))
    sizes = []
    #plt.gca().set_color_cycle(['BLACK', 'RED', 'MAROON', 'YELLOW','OLIVE','LIME','GREEN','AQUA','TEAL'])


    #print 'Convergene_time_dictionary',Convergene_time_dictionary
    index = 0
    color_index =0
    for real_detection_algorithm in dictionary_keys_in_order:
        label_of_result = str(real_detection_algorithm)
        Convergence_times = []
        import math
        from math import log
        
        for topology in topologies:
            topology = str(topology)
#             if log_scale:
                
#                 value = log(Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)])/log(2)
                
#                 print Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)],value
#             else:
            print(label_of_result,int(topology))
            value  = Read_and_Detection_time_with_convergence_Det_Alg[label_of_result][int(topology)]
            try:
                Convergence_times.append(value)
                
            except:
                pass
        sizes.append(str(label_of_result))
        print("these are the x and y axis values",Convergence_times,label_of_result)
#         plot(x, Convergence_times,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=6.0, markersize=10,markerfacecolor='black',markeredgewidth='5', markeredgecolor='blue')
        plot(x, Convergence_times,colors[color_index],linestyle=style[index],markevery=(0.0,0.1),linewidth=6.0, markersize=10,markerfacecolor='black')
        
        index = index +1
        color_index+=1
        if color_index >=len(colors):
            color_index = 1
        if index >= len(style):
            index = 2
            
#         if color_index >= len(colors):
#             index = 0
        
    
    my_class_labels = sizes

    plt.grid(True)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.tight_layout()
#     new_ticks = [ str(y) for y in topologies]
#     plt.xticks(x, new_ticks,fontsize=32)
    plt.grid(True)
    plt.tight_layout()
    if log_scale:
        plt.yscale('log')
#     plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=28)
#     plt.legend([label for label in my_class_labels ],fontsize=23)
    plt.legend([label for label in my_class_labels ],fontsize=25,ncol=1,handleheight=2.4, labelspacing=0.05)
    

    plt.savefig(plot_name)
    plt.show()    
    
def plot_simple_points_multiple_lines(x_axis_label,y_axis_label,Convergene_time_dictionary,MRAI_VALUES4,topology_size4,plot_name):

    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    colors = ['BLACK', 'RED', 'BLUE','GREEN','MAROON', 'YELLOW','OLIVE','LIME','AQUA','TEAL']
    style=["-","--","-.",":","-"]
    color_index = 0
#     my_dic = {}
    my_dic = {}
    my_class_labels = []
    x = np.arange(len(MRAI_VALUES4))
    sizes = []
    index = 0
    #print 'Convergene_time_dictionary',Convergene_time_dictionary
    for topology_size in topology_size4:
        topology_size = (topology_size)
        Convergence_times = []
        for mrai in MRAI_VALUES4:
            mrai = (mrai)
            try:
                #print 'Convergene_time_dictionary[(topology_size)][mrai]',Convergene_time_dictionary[(topology_size)][mrai]
                
                Convergence_times.append(Convergene_time_dictionary[(topology_size)][(mrai)])
            except:
                #print ValueError
                pass
        #print 'Convergence_times',Convergence_times
        sizes.append(str(topology_size))
        plt.plot(x, Convergence_times,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20)
        #plt.plot(x_axis_values, values,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20)

        index = index +1
        color_index = color_index +1
    my_class_labels = sizes
    #plt.xlabel('MRAI (sec)', fontsize=34,labelpad=34)
    #plt.ylabel('Convergence Time (sec)',fontsize=34,labelpad=34)
    plt.grid(True)

#     plt.tight_layout()
    plt.xlim([0, max(x)+0.1])

    new_ticks = [ str(y) for y in MRAI_VALUES4]
    plt.xticks(x, new_ticks,fontsize=34)
    #matplotlib.rcParams.update({'font.size': 34})
    plt.legend([label for label in my_class_labels ],fontsize=30)
    plt.savefig(plot_name)
    plt.show()
    

# In[ ]:




# In[ ]:




# In[ ]:


# data_dictionary_MRAI_0  = {20:{0:.003,1:0.7,2:0.9,4:1.3,8:1.8,16:2.5,32:3.4},
#                            60:{0:0.008,1:1.2,2:1.7,4:2.6,8:3.2,16:4.9,32:6.4},
#                            180:{0:0.01,1:1.6,2:2.5,4:3.5,8:4.3,16:6.3,32:8.3},
#                            540:{0:0.9,1:2.1,2:3.2,4:4.3,8:5.7,16:8.6,32:10.4},
#                            1200:{0:2.02,1:3.2,2:4.2,4:5.3,8:7.4,16:9.3,32:14.6}
                                
#                    }


# # with open('circa_final_results_for_mrai_experiment.csv', "rb") as f:
# #     reader = csv.reader(f, delimiter=",")
# #     for line in (reader):
# #         data_dictionary_MRAI_0[int(line[1])][int(line[0])] = float(line[2])

# x_axis_values_mrai_1 = [0,1,2,4,8,16,32]
# prefix_set_mrai_1 = [20,60,180,540,1200]

# #plot_multiple_line_plot_log_scale_on_x_axis(data_dictionary_MRAI_0,'MRAI(sec)','Convergence time(sec)',x_axis_values_mrai_1,prefix_set_mrai_1,'convergence_time_of_topologies_mrai','# of nodes')
# plot_convergence(data_dictionary_MRAI_0,x_axis_values_mrai_1,prefix_set_mrai_1,'real','convergence_messages','last_detection','cc-last_detection')


# In[ ]:


# x_axis_y_axis_values_over_lines={'down':{'convergence':[1.1,2.02,3.5],'messages':[100,200,300]},
#                                  'up':{'convergence':[2.1,3.02,4.5],'messages':[150,270,399]}}

# x_axis_values_key = 'messages'
# y_axis_values_key = 'convergence'
# x_axis_label = 'Sent messages'
# y_axis_label = 'Convergence time'
# plot_file_name = 'plots_for_delay/up_down_event_convergence_differentiation.pdf'
# log_scale = False
# scatter_with_multiple_colors(x_axis_y_axis_values_over_lines,x_axis_values_key,y_axis_values_key,x_axis_label,y_axis_label,log_scale,plot_file_name)




# In[ ]:



def plot_multiple_methods_linear(each_method_values,x_values,methods_keys,plat_name):
    #print 'Convergene_time_dictionary is',Convergene_time_dictionary
    #print 'MRAI_VALUES4,topology_size4',MRAI_VALUES4,topology_size4
    plt = set_plotting_global_attributes('MRAI (sec)','Convergence time(sec)')
    colors = ['BLACK', 'RED', 'BLUE','GREEN','MAROON', 'YELLOW','OLIVE','LIME','AQUA','TEAL']
    style=["-","--","-.",":","-"]
    color_index = 0
#     my_dic = {}
    my_dic = {}
    my_class_labels = []
    x = np.arange(len(x_values))
    sizes = []
    index = 0
    #print 'Convergene_time_dictionary',Convergene_time_dictionary
    for topology_size in methods_keys:
        topology_size = str(topology_size)
        Convergence_times = []
        for mrai in x_values:
            mrai = str(mrai)
            try:
                #print 'Convergene_time_dictionary[(topology_size)][mrai]',Convergene_time_dictionary[(topology_size)][mrai]
                
                Convergence_times.append(each_method_values[int(topology_size)][int(mrai)])
            except:
                #print ValueError
                pass
        #print 'Convergence_times',Convergence_times
        sizes.append(str(topology_size))
        print('x, Convergence_times',x, Convergence_times)
        plt.plot(x, Convergence_times,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20,markerfacecolor='blue',markeredgewidth='5', markeredgecolor='black')
        #plt.plot(x_axis_values, values,colors[color_index],linestyle=style[index],marker=markers[index],markevery=(0.0,0.1),linewidth=4.0, markersize=20)

        index = index +1
        color_index = color_index +1
    my_class_labels = sizes
    #matplotlib.rcParams['text.usetex'] = True
    #plt.xlabel('MRAI (sec)', fontsize=34,labelpad=34)
    #plt.ylabel('Convergence Time (sec)',fontsize=34,labelpad=34)
    plt.grid(True)
    #matplotlib.rcParams['text.usetex'] = True
#     plt.tight_layout()
    plt.xlim([0, max(x)+0.1])
    #matplotlib.rcParams['text.usetex'] = True
    new_ticks = [ str(y) for y in x_values]
    plt.xticks(x, new_ticks,fontsize=34)
    #matplotlib.rcParams.update({'font.size': 34})
    plt.legend([label for label in my_class_labels ], loc='upper left',fontsize=30)
    plt.savefig(plat_name)
    #matplotlib.rcParams['text.usetex'] = True  
    plt.show()

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



        
def multiple_lines_cdf(x_axis_label,y_axis_label,cdf_info_dictionary_over_multi_item,log,plot_name,list_of_keys,y_min_value,y_max_value):

    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    for scheme, values in cdf_info_dictionary_over_multi_item.items():
        x_axis_min_value = min(values)
        x_axis_max_value = min(values)
    for scheme, values in cdf_info_dictionary_over_multi_item.items():
        #print(scheme,min(reductions), max(reductions),reductions)
        if min(values)<x_axis_min_value:
            x_axis_min_value = min(values)
        if  max(values)>x_axis_max_value:
            x_axis_max_value =  max(values)
#     print("******* this is the x_axis_min_value ******* ",x_axis_min_value)
#     for scheme in cdf_info_dictionary_over_multi_item.keys():
#         cdf_info_dictionary_over_multi_item[scheme][x_axis_min_value-(x_axis_min_value/1000000000000)] = 0
#     print('cdf_info_dictionary_over_multi_item ',cdf_info_dictionary_over_multi_item)
    colors = ['BLACK', 'RED', 'GREEN','BLUE','MAROON','OLIVE','LIME','AQUA','TEAL','YELLOW']
    #colors = ['BLACK', 'RED','BLUE','MAROON','OLIVE','LIME','AQUA','TEAL','YELLOW']
    
    style=["-","-.",":","-","--"]
    
    index = 0
    my_class_labels = []
    items_index = 0
    line_index = 0
    max_value_on_x_axis = []
    for key in list_of_keys:
        #print key
        this_scheme_min_value_on_x_axis = 0
        for scheme, values in cdf_info_dictionary_over_multi_item.items():
            if scheme ==key:
                #print(scheme,min(reductions), max(reductions),reductions)
                if min(values)>this_scheme_min_value_on_x_axis:
                    this_scheme_min_value_on_x_axis = min(values)
                
#                 print("******* this is the x_axis_min_value of scheme  ******* ",scheme,this_scheme_min_value_on_x_axis)
#                 for scheme2 in cdf_info_dictionary_over_multi_item.keys():
#                     if scheme2 ==key:
#                 cdf_info_dictionary_over_multi_item[key][this_scheme_min_value_on_x_axis] = this_scheme_min_value_on_x_axis
        
        
        my_class_labels.append(key)
        cdf_info_dictionary = cdf_info_dictionary_over_multi_item[key]


        #     cdf_info_dictionary = {1:8,3:4,2:4,4:1}
        x_values = list(cdf_info_dictionary.keys())
        #print ('x values are ',x_values,type(x_values))
        x_values.sort()
        max_value_on_x_axis.append(max(x_values))
        #print(x_values,type(x_values))
        CDF_values = get_arrs(list(x_values),cdf_info_dictionary)
        #print ('CDF_values,x_values',key,CDF_values,x_values)
        new_x_values = []
        
        new_cdf_values = []
#         new_x_values.append(0)
        new_x_values.append(this_scheme_min_value_on_x_axis- this_scheme_min_value_on_x_axis/10000000000000000000)
        for x_value_passed in x_values:
            new_x_values.append(x_value_passed)
#         new_cdf_values.append(0)
        new_cdf_values.append(0)
        for CDF_v in CDF_values:
            new_cdf_values.append(CDF_v)
        CDF_values = new_cdf_values
        x_values = new_x_values
        items_index = items_index +1


        ymin, ymax = ylim()  # return the current ylim
        ylim((0, 1))   # set the ylim to ymin, ymax
        ylim(0, 1)     # set the ylim to ymin, ymax
        ylim(y_min_value,y_max_value)
        plt.xlim([0, max(max_value_on_x_axis)])

        plt.xlim([0, x_axis_max_value])
#         print ('key, x_values , CDF_values are',key,x_values,CDF_values)
        plt.plot(x_values, CDF_values,color=colors[index],linestyle=style[line_index],marker=markers[index],markevery=(0.0,0.1),linewidth=6.0, markersize=20,markerfacecolor='blue',markeredgewidth='5', markeredgecolor='black')
        if index == len(colors)-1:
            index = 0
        else:
            index = index +1
        
        if line_index ==len(style)-1:
            line_index = 0
        else:
            line_index = line_index +1
        #plt.plot(x_values, CDF_values,color=colors[index],linestyle=style.next(),marker=markers[index],linewidth=2.0, markersize=20)
    if len(my_class_labels)>1:
        plt.legend([label for label in my_class_labels ],fontsize=26)
    plt.savefig(plot_name)
    plt.show()

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



def simple_plot(x_data,y_data,x_axis_label,y_axis_label,plot_name,x_data2,y_data2):
    
    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    
   
    plt.plot(x_data2, y_data2,color="black",marker=markers[0],markevery=(0.0,0.1),linewidth=4.0, markersize=20)
    #plt.boxplot([item for item in list_of_list],positions=x_data,showmeans=True,widths=(0,10, 10, 10,0),meanline=True)
    
    
    plt.grid(True)
#     plt.tight_layout()
#     new_ticks = [ (y) for y in x_data]
#     plt.xticks(x_data, new_ticks,fontsize=39)
#     plt.ylim(ymin=0) 
#     plt.xlim(xmin=0) 
    plt.savefig(plot_name,bbox_inches='tight')
    plt.show()
    

# In[ ]:



# simple_plot([0,500,1500,4500,18000],[0,1,2,3],'Number of prefixes','Concurrency control \n overhead(msec)','plots/concurrency_control_overhead.pdf',[0,500,1500,4500,18000],[0,100,200,350,700])




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:


# cdf_info_dictionary_over_multi_item = OrderedDict()
# rho = r'$\rho$'
# list_of_keys = ['random','neighborhood','degree']

# cdf_info_dictionary_over_multi_item = {
#                                        'random':{20:20,16:30,14:20,9:10,8:10,4:4,3:4,2:2,0:0},
#     'neighborhood':{21:20,18:30,15:20,13:10,12:10,4:4,3:4,2:2,0:0},
#     'degree':{27:20,23:30,20:20,18:10,14:10,4:4,3:4,2:2,0:0}            
#                                     }
# multiple_lines_cdf('Improvement rate','cumulative fraction \n of root cause events',cdf_info_dictionary_over_multi_item,False,'plots_for_delay/CDF_on_utilization.pdf',list_of_keys)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



        
def multiple_lines_cdf_test(x_axis_label,y_axis_label,cdf_info_dictionary_over_multi_item,log,plot_name,list_of_keys):

    plt = set_plotting_global_attributes(x_axis_label,y_axis_label)
    
    
    
    colors = ['BLUE','BLACK', 'RED', 'MAROON','OLIVE','LIME','AQUA','GREEN','TEAL','YELLOW']
    
    style=["-","-.",":","-","--"]
    index = 0
    my_class_labels = []
    items_index = 0
    line_index = 0
    for key in list_of_keys:
        #print key
        my_class_labels.append(key)
        cdf_info_dictionary = cdf_info_dictionary_over_multi_item[key]


        #     cdf_info_dictionary = {1:8,3:4,2:4,4:1}
        x_values = list(cdf_info_dictionary.keys())
        #print ('x values are ',x_values,type(x_values))
        x_values.sort()
        
        #print(x_values,type(x_values))
        CDF_values = get_arrs(list(x_values),cdf_info_dictionary)
        #print ('CDF_values,x_values',key,CDF_values,x_values)
        new_x_values = []
        new_cdf_values = []
        
        #print (items_index)
#         new_cdf_values.append(0.0)
#         new_x_values.append(x_items[items_index])
        #print ('x_values',x_values)
        for i in range(0,int(min(x_values))):
            new_cdf_values.append(0.0)
            new_x_values.append(i)
        #print ('min(CDF_values)',min(CDF_values))
#         if min(CDF_values)>0.1:
#             #print ('min(CDF_values)>0.1',min(CDF_values),0.1)
#             #print (10*min(CDF_values))
#             #for i in range(1,y_items[items_index]):
#             for i in range(0,int(10*min(CDF_values))):
#                 #print (i,items_index)
#                 #new_cdf_values.append(float(i)/10)
#                 new_cdf_values.append(float(i)/10)
#                 #new_x_values.append(x_items[items_index])
#                 new_x_values.append(min(x_values))
#         items_index = items_index +1
#         for item in CDF_values:
#             new_cdf_values.append(item)
#         for item in x_values:
#             new_x_values.append(item)
        x_values = new_x_values
        CDF_values = new_cdf_values
        #print (CDF_values,x_values)

        ymin, ymax = ylim()  # return the current ylim
        ylim((0, 1))   # set the ylim to ymin, ymax
        ylim(0, 1)     # set the ylim to ymin, ymax
        #plt.xlim([0, max(x_values)])
        plt.ylim([0, 1])
        if min(x_values) <0:
            
            plt.xlim([min(x_values), max(x_values)])
        else:
            plt.xlim([0, max(x_values)])
        
        print ('x_values is ',x_values)
        plt.plot(x_values, CDF_values,color=colors[index],linestyle=style[line_index],marker=markers[index],markevery=(0.0,0.1),linewidth=6.0, markersize=20,markerfacecolor='blue',markeredgewidth='5', markeredgecolor='black')
        if index == len(colors)-1:
            index = 0
        else:
            index = index +1
        
        if line_index ==len(style)-1:
            line_index = 0
        else:
            line_index = line_index +1
        #plt.plot(x_values, CDF_values,color=colors[index],linestyle=style.next(),marker=markers[index],linewidth=2.0, markersize=20)
    if len(my_class_labels)>1:
        plt.legend([label for label in my_class_labels ],fontsize=33)
    plt.savefig(plot_name)
    plt.show()

# cdf_info_dictionary_over_multi_item = {
                                       
                                       
#                                        'MRAI 2 sec'  :{4:60,3:30,2:7,0:0,1:3,6:0},
# #                                         'conc. control without transient mode'  :{0.2:80,0.2:10,0.1:5,0:0,0.1:5},
#                                         'batch processing'  :{5:60,3:30,2:1,4:9,0:0,6:0},
#                                         'MRAI zero'  :{6:60,5:30,4:5,0:0,2:5}
#                                     }
# list_of_keys = ['batch processing','MRAI zero','MRAI 2 sec']




# #         print(delay_repeatings[19806.0])
# # for i in range(1,70):
# #     cdf_info_dictionary_over_multi_item['third approach'][1000]=i
    
# # for i in range(1,60):
# #     cdf_info_dictionary_over_multi_item['first approach'][800]=i

# multiple_lines_cdf('Frequency of path changing','Cumulutive fraction of \n router-prefix pairs',cdf_info_dictionary_over_multi_item,False,'plots/CDF_on_path_changing.pdf',list_of_keys)
# # multiple_lines_cdf_test('Frequency of path changing','Cumulutive fraction of \n router-prefix pairs',cdf_info_dictionary_over_multi_item,False,'plots/CDF_on_path_changing.pdf',list_of_keys)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



    


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:


# #runs of the experimens: batch_processing_exp_800_prefixes_link_delay_inter_phy_machines,MRAI_0_exp_800_prefixes_link_delay_inter_phy_machines,MRAI_2_exp_800_prefixes_link_delay_inter_phy_machines,MRAI_200m_exp_800_prefixes_link_delay_inter_phy_machines,MRAI_0_exp_800_prefixes_8mic_p_link_delay_inter_phy_machines,batch_processing_exp_100_prefixes_8mic_p_link_delay_inter_phy_machines
# #MRAI_0_exp_800_prefixes_14mic_p_link_delay_inter_33_phy_machines,MRAI_0_exp_800_prefixes_link_delay_inter_phy_machines,batch_processing_exp_800_prefixes_link_delay_inter_phy_machines,batch_processing_exp_800_prefixes_14mic_p_link_delay_inter_48_phy_machines,MRAI_200m_exp_800_prefixes_link_delay_inter_phy_machines
# #202109,52320-link_down,45474,4637-link_up,7552,9498-link_down,7552,9498-link_up,
# result_file_name = 'batch_processing_result.csv'
# result_file_name= 'MRAIs_result.csv'
# result_file_name = 'each_scheme_each_link_convergence_time_result_500.csv'
# result_file_name = 'each_scheme_each_link_convergence_time_result_40.csv'
# # result_file_name = 'each_scheme_each_link_mean_convergence_time_result_500.csv'
# # result_file_name='all_schemes_result.csv'
# # result_file_name = 'MRAI_0_batch_processing_p=4_24_result.csv'
# topology = '40'
# each_scheme_key = {'batch_processing_p=4':'batch processing,p=4\u03BCs',
#                    'batch_processing_p=24':'batch processing,p=24\u03BCs',
#                    'batch_processing_p=12':'batch processing,p=12\u03BCs',
#                    'batch_processing_p=14':'batch processing,p=12\u03BCs',
#                    'batch_processing_p=54':'batch processing,p=54\u03BCs',
#                    'batch_processing_p=50':'batch processing,p=50\u03BCs',
#                    'fixed_batch_processing_p=54':'fixed batch processing,p=54\u03BCs',
#                    'fixed_batch_processing_p=4':'fixed batch processing,p=4\u03BCs',
#                    'batch_processing_p=104':'batch processing,p=104\u03BCs',
#                    'BP_p=4':'batch processing,p=4\u03BCs',
#                    'BP_p=54':'batch processing,p=54\u03BCs',
#                    '[batch_processing_p=104':'batch processing,p=104\u03BCs',
#                    '[batch_processing_p=54':'batch processing,p=54\u03BCs',
#                    'simple_batch_processing_p=4':'simple batch processing,p=4\u03BCs',
#                    'simple_batch_processing_p=54' :'simple batch processing,p=54\u03BCs',
#                     'enhanced_batch_processing_p=54':'enhanced_batch_processing,p=54\u03BCs',
#                   'MRAI=0_p=4':'FIFO NMRAI,p=4\u03BCs',
#                    'MRAI=0_p=24':'MRAI=0,p=24\u03BCs',
#                    'MRAI_0_p=104':'MRAI=0,p=104\u03BCs',
#                    'MRAI=0_p=104':'MRAI=0,p=104\u03BCs',
#                    '[MRAI=0_p=20':'MRAI=0,p=20\u03BCs',
#                   '[MRAI=0_p=12':'MRAI=0,p=12\u03BCs',
#                    '[MRAI=0_p=50':'MRAI=0,p=50\u03BCs',
#                    'MRAI=0_p=20':'MRAI=0,p=20\u03BCs',
#                    'MRAI=0_p=122':'MRAI=0,p=122\u03BCs',
#                    'MRAI=10_p=4':'MRAI=10ms,p=4\u03BCs',
#                    'MRAI=100_p=50':'MRAI=100ms,p=50\u03BCs',
#                    'MRAI=0_p=204':'MRAI=0,p=204\u03BCs',
#                   'MRAI=0_p=12':'MRAI=0,p=12\u03BCs',
#                   'MRAI_200ms=p=4':'MRAI=200ms,p=4\u03BCs','MRAI_200ms_p=4':'MRAI=200ms,p=4\u03BCs','MRAI=200ms_p=4':'MRAI=200ms, p=4\u03BCs',
#                   'MRAI=2_p=4':'MRAI=2s,p=4\u03BCs',
#                    'MRAI=2':'MRAI=2s,p=4\u03BCs',
#                    'MRAI=2_p=12':'MRAI=2s,p=12\u03BCs',
#                    'MRAI_30':'MRAI=30s,p=4\u03BCs',
#                    'batch':'batch,p=54\u03BCs',
#                    'MRAI=0_p=54':'MRAI=0,p=54\u03BCs',
#                    'MRAI=0_p=50':'FIFO NMRAI,p=50\u03BCs',
#                    'MRAI=0_p=16':'MRAI=0,p=16\u03BCs',
#                    '[MRAI=0_p=54':'MRAI=0,p=54\u03BCs',
#                    'MRAI_600':'MRAI=600ms,p=4\u03BCs',
#                    'MRAI=600_p=4':'MRAI=600ms,p=4\u03BCs',
#                   'MRAI=600_p=24':'MRAI=600ms,p=24\u03BCs',
#                  'MRAI=30_p=4':'MRAI=30s,p=4\u03BCs',
#                    'MRAI=2_p=54':'MRAI=2s,p=54\u03BCs',
#                    'MRAI=2_p=50':'MRAI=2s,p=50\u03BCs',
#                     'MRAI=6_p=50':'work.cons.=5,p=50\u03BCs',
#                   'MRAI=200_p=4' :'MRAI=200ms,p=4\u03BCs',
#                    'MRAI=4_p=50':'MRAI=0 plus work.cons.,p=54\u03BCs',
#                    'MRAI=4_p=4':'MRAI=4s,p=4\u03BCs',
#                    'MRAI=10_p=54':'MRAI=10ms,p=54\u03BCs',
#                   'MRAI=600_p=54' :'MRAI=600ms,p=54\u03BCs',
#                    'MRAI=4_p=50' :'infinit_work.c.MRAI=100,p=50\u03BCs',
#                    'MRAI=6002_p=54' :'MRAI=600ms per peer,p=54\u03BCs',
#                   '[MRAI=2_p=12':'MRAI=2s,p=12\u03BCs'}
# for mean_median in ['mean','median']:
#     schemes_in_order = []
#     each_approach_each_link_convergence_time = {}
#     with open(result_file_name, "r") as f:
#         reader = csv.reader(f, delimiter=",")
#         for line in (reader):
#             scheme= each_scheme_key[line[0]]
#             if scheme not in schemes_in_order:
#                 schemes_in_order.append(scheme)
#             each_approach_each_link_convergence_time[scheme]= {}
#     link_delays = []
#     print('schemes_in_order',schemes_in_order)
#     with open(result_file_name, "r") as f:
#         reader = csv.reader(f, delimiter=",")
#         for line in (reader):
            
#             scheme= each_scheme_key[line[0]]
#             link_delay = int(line[1])

#     #             link_delay = 1
#             if link_delay not in link_delays:
#                 link_delays.append(link_delay)
#             if mean_median =='mean':
#                 convergence_time = round(float(line[3]),4)
#             else:
#                 convergence_time = round(float(line[2]),4)

#                 #         if link_delay == 4 and scheme =='batch_processing_800':
#     #             convergence_time = each_approach_each_link_convergence_time['batch_processing_800'][10]-0.08
#     #         if '8' in scheme:
#     #             if 'MRAI' in scheme:
#     #                 scheme = "MRAI 0, p= 8\u03BCs"
#     #             else:
#     #                 scheme = "batch processing, p=8\u03BCs"
#     #         else:
#     #             if 'batch_processing_100' in scheme:
#     #                 scheme = "batch processing(100), p= 8\u03BCs"
#     #             else:
#     #                 scheme = scheme+", p= 4\u03BCs"

#             each_approach_each_link_convergence_time[scheme][link_delay] = convergence_time
#     print(each_approach_each_link_convergence_time)
#     dictionary_keys_in_order  = ["Batch processing delay","No MRAI scheme","MRAI=2 sec","MRAI=4 sec","MRAI=30 sec"]
#     link_delays = sort(link_delays)
#     dictionary_keys_in_order  = ["Batch processing delay","No MRAI scheme","MRAI=2 sec","MRAI=4 sec","MRAI=1 sec"]
#     # plot_convergence_detection_alg_overhead('Link delay(msec)','Convergence(sec)',dictionary_keys_in_order,Read_and_Detection_time_with_convergence_Det_Alg,topologies,False,'plots/CD_link_delay.pdf')
#     plot_convergence_detection_alg_overhead('Propagation delay(msec) log scale',mean_median+' of convergence delay(msec)',schemes_in_order,each_approach_each_link_convergence_time,link_delays,False,'plots/'+mean_median+'_CD_link_delay_real_'+topology+'.pdf')
#     ploting_simple_y_as_x('Propagation delay(msec)',mean_median+' of convergence delay(msec)',schemes_in_order,each_approach_each_link_convergence_time,link_delays,False,'plots/'+mean_median+'_CD_link_delay_real_no_log_on_x_axis'+topology+'.pdf')
# print("done")

# print(2%10)


# # MRAI_4_exp_800_prefixes_54mic_p_link_delay_inter_48_phy_machines/MRAI_MRAI_0/topology_size_500$ cp -r 1 2
# # these are the x and y axis values [25.0373125, 25.02177777777778] batch processing,p=54μs


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# 

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:


def check_if_event_has_CD_for_all_x_axises(scheme,each_approach_each_x_axis_each_y_value,x_axis_values):
    #print(x_axis_values,list(each_approach_each_x_axis_each_y_value[scheme].keys()) )
    for item in x_axis_values:
        if item not in list(each_approach_each_x_axis_each_y_value[scheme].keys()):
            #print('return Fasle')
            return False
    #print('return True')
    return True
    

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



