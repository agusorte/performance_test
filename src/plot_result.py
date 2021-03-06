import numpy as np
import matplotlib.pyplot as plt

#rate =10
means= (0.099920 , 0.100356547519 , 0.099923, 0.100672315578  )

#rate = 100
#means= (0.009924 , 0.0102241849899 , 0.009920,  0.0102731633186  )

#rate = 1
#means= (0.999924  ,  1.00145886161  , 0.999906 ,  1.0013303566  )


ind = np.arange(len(means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, means, width,
                color='SkyBlue', label='time')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('c++&&c++', 'c++&&python', 'python&&python', 'python&&c++'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
# autolabel(rects2, "right")

plt.show()